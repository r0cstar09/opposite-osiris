#!/usr/bin/env python3
"""Generate portfolio screenshots for fuzzy-funicular (no secrets)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "public" / "assets" / "fuzzy-funicular"
SOURCE = Path(__file__).resolve().parents[2] / "fuzzy-funicular-source"

BG = (15, 23, 42)
PANEL = (30, 41, 59)
BORDER = (51, 65, 85)
TEXT = (226, 232, 240)
MUTED = (148, 163, 184)
ACCENT = (96, 165, 250)
GREEN = (74, 222, 128)
YELLOW = (250, 204, 21)
LINE_H = 22
PAD = 28


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Menlo.ttc",
        "/Library/Fonts/Menlo.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size=size, index=1 if bold and path.endswith(".ttc") else 0)
            except OSError:
                try:
                    return ImageFont.truetype(path, size=size)
                except OSError:
                    continue
    return ImageFont.load_default()


def wrap_lines(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        if not raw:
            lines.append("")
            continue
        words = raw.split(" ")
        current = ""
        for word in words:
            trial = word if not current else f"{current} {word}"
            if draw.textlength(trial, font=font) <= max_width:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def render_code_image(
    filename: str,
    title: str,
    subtitle: str,
    body: str,
    *,
    width: int = 1280,
    highlight: dict[str, str] | None = None,
) -> None:
    font = load_font(15)
    title_font = load_font(18, bold=True)
    sub_font = load_font(13)
    draw_probe = ImageDraw.Draw(Image.new("RGB", (width, 100)))
    max_text_width = width - PAD * 2
    lines = wrap_lines(body, font, max_text_width, draw_probe)

    height = PAD * 2 + 56 + len(lines) * LINE_H + 16
    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle((12, 12, width - 12, height - 12), radius=12, fill=PANEL, outline=BORDER, width=1)
    draw.text((PAD, PAD), title, font=title_font, fill=TEXT)
    draw.text((PAD, PAD + 28), subtitle, font=sub_font, fill=MUTED)

    y = PAD + 56
    for line in lines:
        color = TEXT
        if highlight:
            for key, c in highlight.items():
                if key in line:
                    color = c
                    break
        draw.text((PAD, y), line, font=font, fill=color)
        y += LINE_H

    img.save(OUT / filename, optimize=True)


def read_excerpt(path: Path, start: int, end: int) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(lines[start - 1 : end])


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    structure = """fuzzy-funicular/
├── README.md
├── lessons/                 # lesson-1 … lesson-64 (JSON + Markdown)
├── scripts/
│   └── send_daily_lesson.py # validate, select, render, send
├── requirements.txt
└── .github/workflows/
    └── send-daily-lesson.yml"""

    render_code_image(
        "fuzzy-funicular-01-structure.png",
        "fuzzy-funicular",
        "Repository layout",
        structure,
        highlight={"send_daily_lesson.py": ACCENT, "send-daily-lesson.yml": YELLOW},
    )

    workflow = read_excerpt(
        SOURCE / ".github/workflows/send-daily-lesson.yml", 1, 48
    ).replace("${{ secrets.ICLOUD_EMAIL }}", "***@***")
    workflow = workflow.replace("${{ secrets.ICLOUD_APP_PASSWORD }}", "***")
    workflow = workflow.replace("${{ secrets.RECIPIENT_EMAIL }}", "***@***")

    render_code_image(
        "fuzzy-funicular-02-workflow.png",
        ".github/workflows/send-daily-lesson.yml",
        "Scheduled delivery with validation gate",
        workflow,
        highlight={"--validate-all": GREEN, "cron": YELLOW},
    )

    script = read_excerpt(SOURCE / "scripts/send_daily_lesson.py", 77, 137)
    script += "\n\n# ... validate_lesson_schema(), render_markdown_lesson(), send via SMTP"
    render_code_image(
        "fuzzy-funicular-03-script-selection.png",
        "scripts/send_daily_lesson.py",
        "Date/cadence lesson selection",
        script,
        highlight={"select_lesson_file": ACCENT, "LESSON_CADENCE_DAYS": YELLOW},
    )

    lesson_json = read_excerpt(SOURCE / "lessons/lesson-40/lesson.json", 1, 38)
    render_code_image(
        "fuzzy-funicular-04-lesson-json.png",
        "lessons/lesson-40/lesson.json",
        "Structured drill schema (excerpt)",
        lesson_json,
        highlight={"cognitive_shift": ACCENT, "controlled_recombination": GREEN},
    )

    validate_out = """$ python scripts/send_daily_lesson.py --validate-all
OK lesson-1: lessons/lesson-1/lesson.json
OK lesson-2: lessons/lesson-2/lesson.json
OK lesson-3: lessons/lesson-3/lesson.json
...
OK lesson-10: lessons/lesson-10/lesson.json
OK lesson-12: lessons/lesson-12/lesson.json
...
OK lesson-64: lessons/lesson-64/lesson.json

63 lessons validated (lesson-11 folder pending JSON)."""

    render_code_image(
        "fuzzy-funicular-05-validate-output.png",
        "Terminal",
        "Fail-fast validation before any send",
        validate_out,
        highlight={"OK": GREEN, "--validate-all": ACCENT},
    )

    dry_run = """$ python scripts/send_daily_lesson.py --lesson-number 40 --dry-run
Selected lesson file: lessons/lesson-40/lesson.json

# Spanish Daily Lesson 40

**Pattern ID:** PRETERITE_IMPERFECT_DECISION_FRAMES_40
**Difficulty:** A2-B1
**Target Pattern:** Choose imperfect for background…

## 1) cognitive_shift

- **English trap:** Using one generic past tense for everything…
- **Spanish logic:** Spanish splits past meaning into scene/background…

### 5 natural examples
1. Cuando era nino, vivia cerca del centro.
2. Ayer llegue tarde a la reunion.
3. Estudiaba cuando me llamaste."""

    render_code_image(
        "fuzzy-funicular-06-dryrun-preview.png",
        "Terminal — dry run",
        "Rendered Markdown lesson preview (no email sent)",
        dry_run,
        highlight={"--dry-run": ACCENT, "cognitive_shift": GREEN},
    )

    # Hero thumbnail: workflow automation
    hero = Image.open(OUT / "fuzzy-funicular-02-workflow.png")
    hero = hero.resize((960, int(hero.height * 960 / hero.width)), Image.Resampling.LANCZOS)
    hero.save(OUT / "fuzzy-funicular-hero.png", optimize=True)
    print(f"Wrote screenshots to {OUT}")


if __name__ == "__main__":
    main()
