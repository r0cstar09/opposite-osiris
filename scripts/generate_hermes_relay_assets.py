#!/usr/bin/env python3
"""Generate Hermes Relay portfolio assets from the cloned source repo."""

from __future__ import annotations

from pathlib import Path

SOURCE = Path(__file__).resolve().parents[2] / "hermes-relay-source"
OUT = Path(__file__).resolve().parents[1] / "public" / "assets" / "hermes-relay"
BRIEFING = SOURCE / "json_output" / "2025-12-31" / "hermes_briefing_2025-12-31.html"
OUTPUT_SIZE = (800, 450)
VIEWPORT_WIDTH = 640
CLIP_HEIGHT = 300


def crop_to_16_9(src: Path, dest: Path) -> None:
    from PIL import Image

    img = Image.open(src).convert("RGB")
    target_w, target_h = OUTPUT_SIZE
    ratio = target_w / target_h
    w, h = img.size
    crop_h = min(h, int(w / ratio))
    img = img.crop((0, 0, w, crop_h))
    img = img.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
    img.save(dest, format="PNG", optimize=True)


def capture_briefing() -> None:
    from playwright.sync_api import sync_playwright

    if not BRIEFING.exists():
        raise FileNotFoundError(f"Briefing HTML not found: {BRIEFING}")

    raw = OUT / "_briefing_raw.png"
    final = OUT / "hermes-relay-briefing-preview.png"
    OUT.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_WIDTH, "height": 700})
        page.goto(BRIEFING.as_uri(), wait_until="networkidle")
        box = page.locator(".container").bounding_box()
        if not box:
            raise RuntimeError("Could not find .container in briefing HTML")
        page.screenshot(
            path=str(raw),
            clip={
                "x": box["x"],
                "y": box["y"],
                "width": box["width"],
                "height": CLIP_HEIGHT,
            },
        )
        browser.close()

    crop_to_16_9(raw, final)
    raw.unlink(missing_ok=True)
    print(f"Wrote {final}")


def render_code_image(path: Path, title: str, subtitle: str, body: str) -> None:
    from PIL import Image, ImageDraw, ImageFont

    BG, PANEL, BORDER = (15, 23, 42), (30, 41, 59), (51, 65, 85)
    TEXT, MUTED, ACCENT = (226, 232, 240), (148, 163, 184), (96, 165, 250)
    PAD, LINE_H, WIDTH = 28, 20, 1280

    font = ImageFont.load_default()
    title_font = font
    img = Image.new("RGB", (WIDTH, 400), BG)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((12, 12, WIDTH - 12, 388), radius=12, fill=PANEL, outline=BORDER)
    y = PAD
    draw.text((PAD, y), title, fill=TEXT, font=title_font)
    y += 24
    draw.text((PAD, y), subtitle, fill=MUTED, font=font)
    y += 32
    for line in body.splitlines()[:14]:
        draw.text((PAD, y), line[:110], fill=TEXT if not line.strip().startswith("#") else ACCENT, font=font)
        y += LINE_H
    img.save(path, optimize=True)


def render_structure() -> None:
    body = """hermes-relay/
├── hermes-relay.py           # RSS ingest + dedupe
├── llm_score_and_summarize.py # Vertex Gemini scoring + HTML
├── orchestrator.py            # runs both scripts in order
├── hermes_signal_YYYY-MM-DD.json
├── json_output/YYYY-MM-DD/
│   ├── hermes_llm_top3_*.json
│   └── hermes_briefing_*.html
└── .github/workflows/hermes-relay.yml"""
    render_code_image(
        OUT / "hermes-relay-01-structure.png",
        "hermes-relay",
        "Repository layout",
        body,
    )


def render_workflow() -> None:
    yml = (SOURCE / ".github/workflows" / "hermes-relay.yml").read_text(encoding="utf-8")
    lines = yml.splitlines()[:36]
    body = "\n".join(lines).replace("${{ secrets.GCP_SA_KEY }}", "***")
    render_code_image(
        OUT / "hermes-relay-02-workflow.png",
        ".github/workflows/hermes-relay.yml",
        "Scheduled + manual dispatch, Vertex auth, orchestrator",
        body,
    )


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Clone not found: {SOURCE}")

    OUT.mkdir(parents=True, exist_ok=True)
    render_structure()
    render_workflow()
    print("Wrote structure + workflow PNGs")

    try:
        capture_briefing()
    except Exception as exc:
        print(f"Briefing screenshot skipped: {exc}")


if __name__ == "__main__":
    main()
