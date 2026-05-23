#!/usr/bin/env python3
"""Export lesson email previews as fixed 16:9 crops (header + top of body)."""

from __future__ import annotations

import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[2] / "fuzzy-funicular-source"
OUT = Path(__file__).resolve().parents[1] / "public" / "assets" / "fuzzy-funicular"
LESSONS = (1, 25, 40)
VIEWPORT_WIDTH = 640
# CSS pixels from top of .container — gradient header + start of lesson body
CLIP_HEIGHT = 260
OUTPUT_SIZE = (800, 450)  # 16:9 portfolio dimensions


def html_from_lesson(lesson_number: int) -> str:
    sys.path.insert(0, str(SOURCE / "scripts"))
    from send_daily_lesson import (  # noqa: PLC0415
        build_message,
        discover_lesson_files,
        load_json,
        render_markdown_lesson,
        validate_lesson_schema,
    )

    lessons_root = SOURCE / "lessons"
    lesson_files = discover_lesson_files(lessons_root)
    match = next((p for n, p in lesson_files if n == lesson_number), None)
    if match is None:
        raise FileNotFoundError(f"lesson-{lesson_number} not found")

    payload = load_json(match)
    validate_lesson_schema(payload, str(match))
    markdown = render_markdown_lesson(lesson_number, payload)
    subject = f"Spanish Daily Lesson {lesson_number} - {payload['pattern_id']}"
    message = build_message("learner@example.com", "learner@example.com", subject, markdown)

    for part in message.walk():
        if part.get_content_type() == "text/html":
            return part.get_content()
    raise RuntimeError("No HTML part in message")


def crop_to_16_9(src: Path, dest: Path) -> None:
    from PIL import Image  # noqa: PLC0415

    img = Image.open(src).convert("RGB")
    target_w, target_h = OUTPUT_SIZE
    target_ratio = target_w / target_h
    w, h = img.size
    crop_h = min(h, int(w / target_ratio))
    img = img.crop((0, 0, w, crop_h))
    img = img.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
    img.save(dest, format="PNG", optimize=True)


def capture_container_top(page, raw_path: Path) -> None:
    container = page.locator(".container")
    container.wait_for(state="visible")
    box = container.bounding_box()
    if not box:
        raise RuntimeError("Could not measure .container")
    page.screenshot(
        path=str(raw_path),
        clip={
            "x": box["x"],
            "y": box["y"],
            "width": box["width"],
            "height": CLIP_HEIGHT,
        },
    )


def capture_with_playwright(html_paths: list[tuple[str, Path]]) -> None:
    from playwright.sync_api import sync_playwright  # noqa: PLC0415

    OUT.mkdir(parents=True, exist_ok=True)
    raw_dir = OUT / "_raw"
    raw_dir.mkdir(exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(
            viewport={"width": VIEWPORT_WIDTH, "height": 700},
            device_scale_factor=1,
        )
        for name, html_path in html_paths:
            page.goto(html_path.as_uri(), wait_until="networkidle")
            raw_path = raw_dir / f"{name}.png"
            final_path = OUT / f"fuzzy-funicular-email-{name}.png"
            capture_container_top(page, raw_path)
            crop_to_16_9(raw_path, final_path)
            print(f"{final_path.name} -> {OUTPUT_SIZE[0]}x{OUTPUT_SIZE[1]}")
        browser.close()

    import shutil

    shutil.rmtree(raw_dir, ignore_errors=True)


def resize_asset(path: Path, max_width: int = 800) -> None:
    from PIL import Image  # noqa: PLC0415

    if not path.exists():
        return
    img = Image.open(path)
    if img.width <= max_width:
        return
    ratio = max_width / img.width
    new_size = (max_width, int(img.height * ratio))
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    img.save(path, format="PNG", optimize=True)


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Source repo not found: {SOURCE}")

    tmp = OUT / "_html_previews"
    tmp.mkdir(parents=True, exist_ok=True)
    html_paths: list[tuple[str, Path]] = []

    for num in LESSONS:
        html = html_from_lesson(num)
        path = tmp / f"lesson-{num}.html"
        path.write_text(html, encoding="utf-8")
        html_paths.append((f"lesson-{num:02d}", path))

    capture_with_playwright(html_paths)

    for tech in (
        "fuzzy-funicular-01-structure.png",
        "fuzzy-funicular-02-workflow.png",
    ):
        resize_asset(OUT / tech)

    # Remove legacy tall email filenames
    for old in OUT.glob("fuzzy-funicular-email-*-top.png"):
        old.unlink(missing_ok=True)
    for old in OUT.glob("fuzzy-funicular-email-*-drills.png"):
        old.unlink(missing_ok=True)

    import shutil

    shutil.rmtree(tmp, ignore_errors=True)
    print(f"Done. Assets in {OUT}")


if __name__ == "__main__":
    main()
