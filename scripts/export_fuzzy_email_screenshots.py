#!/usr/bin/env python3
"""Export rendered lesson HTML emails and capture PNG screenshots."""

from __future__ import annotations

import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[2] / "fuzzy-funicular-source"
OUT = Path(__file__).resolve().parents[1] / "public" / "assets" / "fuzzy-funicular"
LESSONS = (1, 25, 40)


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


def capture_with_playwright(html_paths: list[tuple[str, Path]]) -> None:
    from playwright.sync_api import sync_playwright  # noqa: PLC0415

    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 820, "height": 900})
        for name, html_path in html_paths:
            page.goto(html_path.as_uri(), wait_until="networkidle")
            container = page.locator(".container")
            container.wait_for(state="visible")

            top_path = OUT / f"fuzzy-funicular-email-{name}-top.png"
            container.screenshot(path=str(top_path))

            page.evaluate(
                """() => {
                const content = document.querySelector('.content');
                if (content) content.scrollIntoView({ block: 'start' });
            }"""
            )
            drills_path = OUT / f"fuzzy-funicular-email-{name}-drills.png"
            page.locator(".content").screenshot(path=str(drills_path))

        browser.close()


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
        print(f"Wrote {path}")

    capture_with_playwright(html_paths)
    print(f"Screenshots saved to {OUT}")


if __name__ == "__main__":
    main()
