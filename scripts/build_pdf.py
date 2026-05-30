#!/usr/bin/env python3
"""Build the Hugo single-file PDF HTML and render it with WeasyPrint."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from html import escape
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GENERATED_DATA = ROOT / "pdf" / "data" / "pdf" / "manifest.json"


def run(command: list[str], *, cwd: Path = ROOT) -> None:
    print("+ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def read_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)

    if isinstance(raw, list):
        pages = raw
        metadata: dict[str, Any] = {}
    elif isinstance(raw, dict):
        pages = raw.get("pages")
        metadata = {key: value for key, value in raw.items() if key != "pages"}
    else:
        raise SystemExit(f"{path} must contain either a JSON array or object")

    if not isinstance(pages, list) or not pages:
        raise SystemExit(f"{path} must contain a non-empty list of pages")

    normalized_pages: list[dict[str, str]] = []
    for index, item in enumerate(pages, start=1):
        if isinstance(item, str):
            page_path = item
        elif isinstance(item, dict) and isinstance(item.get("path"), str):
            page_path = item["path"]
        else:
            raise SystemExit(f"{path}: page {index} must be a string or object with a path")

        page_path = page_path.removeprefix("content/").lstrip("/")
        if not page_path.endswith(".md"):
            raise SystemExit(f"{path}: page {index} must point to a Markdown file: {page_path}")
        if ".." in Path(page_path).parts:
            raise SystemExit(f"{path}: page {index} may not contain '..': {page_path}")

        content_file = ROOT / "content" / page_path
        if not content_file.is_file():
            raise SystemExit(f"{path}: page {index} does not exist: content/{page_path}")

        normalized_pages.append({"path": page_path})

    return {
        "title": metadata.get("title", "Epimethean Challenge"),
        "subtitle": metadata.get("subtitle", "Offline documentation"),
        "version": metadata.get("version") or os.environ.get("DOC_VERSION") or git_version(),
        "buildDate": metadata.get("buildDate") or datetime.now(timezone.utc).date().isoformat(),
        "pages": normalized_pages,
    }


def git_version() -> str:
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--always", "--dirty"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "local"
    return result.stdout.strip() or "local"


def write_hugo_data(payload: dict[str, Any]) -> None:
    GENERATED_DATA.parent.mkdir(parents=True, exist_ok=True)
    with GENERATED_DATA.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def build_html(args: argparse.Namespace) -> None:
    command = [
        args.hugo,
        "--config",
        "hugo.toml,pdf/config.toml",
        "--environment",
        "pdf",
        "--destination",
        str(args.destination),
      ]
    if args.clean_destination:
        command.append("--cleanDestinationDir")
    run(command)


def chapter_id(page_path: str) -> str:
    stem = page_path.removesuffix(".md").replace("/", "-")
    slug = "".join(character.lower() if character.isalnum() else "-" for character in stem)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return f"chapter-{slug.strip('-')}"


def normalize_link_path(href: str) -> tuple[str, str]:
    path, separator, fragment = href.partition("#")
    path = path.split("?", 1)[0]
    for prefix in ("./", "../"):
        while path.startswith(prefix):
            path = path.removeprefix(prefix)
    path = path.removeprefix("/").removeprefix("docs/")
    path = path.removesuffix("/")
    path = path.removesuffix(".html").removesuffix(".md")
    return path, fragment if separator else ""


def rewrite_internal_links(html_path: Path, pages: list[dict[str, str]]) -> None:
    page_targets = {
        item["path"].removesuffix(".md"): f"#{chapter_id(item['path'])}"
        for item in pages
    }

    class Rewriter(HTMLParser):
        def __init__(self) -> None:
            super().__init__(convert_charrefs=False)
            self.parts: list[str] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            self.parts.append(self._format_tag(tag, attrs, closed=False))

        def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            self.parts.append(self._format_tag(tag, attrs, closed=True))

        def handle_endtag(self, tag: str) -> None:
            self.parts.append(f"</{tag}>")

        def handle_data(self, data: str) -> None:
            self.parts.append(data)

        def handle_entityref(self, name: str) -> None:
            self.parts.append(f"&{name};")

        def handle_charref(self, name: str) -> None:
            self.parts.append(f"&#{name};")

        def handle_comment(self, data: str) -> None:
            self.parts.append(f"<!--{data}-->")

        def handle_decl(self, decl: str) -> None:
            self.parts.append(f"<!{decl}>")

        def _format_tag(self, tag: str, attrs: list[tuple[str, str | None]], *, closed: bool) -> str:
            rewritten: list[tuple[str, str | None]] = []
            for name, value in attrs:
                if tag == "a" and name == "href" and value:
                    value = rewrite_href(value)
                rewritten.append((name, value))
            suffix = " /" if closed else ""
            return f"<{tag}{format_attrs(rewritten)}{suffix}>"

    def rewrite_href(href: str) -> str:
        if href.startswith(("#", "http://", "https://", "mailto:", "tel:")):
            return href
        path, fragment = normalize_link_path(href)
        if path in page_targets:
            return f"#{fragment}" if fragment else page_targets[path]
        return href

    def format_attrs(attrs: list[tuple[str, str | None]]) -> str:
        output = []
        for name, value in attrs:
            if value is None:
                output.append(f" {name}")
            else:
                output.append(f' {name}="{escape(value, quote=True)}"')
        return "".join(output)

    parser = Rewriter()
    parser.feed(html_path.read_text(encoding="utf-8"))
    html_path.write_text("".join(parser.parts), encoding="utf-8")


def build_pdf(html_path: Path, pdf_path: Path) -> None:
    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise SystemExit(
            "WeasyPrint is not installed. Install it with "
            "`python -m pip install -r requirements-pdf.txt`."
        ) from exc

    if not html_path.is_file():
        raise SystemExit(f"PDF HTML was not generated: {html_path}")

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))
    print(f"wrote {pdf_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "pdf" / "manifest.json")
    parser.add_argument("--destination", type=Path, default=ROOT / "public")
    parser.add_argument("--html", type=Path, default=ROOT / "public" / "pdf" / "book.html")
    parser.add_argument("--pdf", type=Path, default=ROOT / "public" / "pdf" / "documentation.pdf")
    parser.add_argument("--hugo", default=os.environ.get("HUGO", "hugo"))
    parser.add_argument("--html-only", action="store_true", help="Generate book.html but skip WeasyPrint")
    parser.add_argument("--pdf-only", action="store_true", help="Render an existing book.html with WeasyPrint")
    parser.add_argument("--clean-destination", action="store_true", help="Pass --cleanDestinationDir to Hugo")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.manifest = args.manifest.resolve()
    args.destination = args.destination.resolve()
    args.html = args.html.resolve()
    args.pdf = args.pdf.resolve()

    if not args.pdf_only:
        payload = read_manifest(args.manifest)
        write_hugo_data(payload)
        build_html(args)
        rewrite_internal_links(args.html, payload["pages"])

    if not args.html_only:
        build_pdf(args.html, args.pdf)

    return 0


if __name__ == "__main__":
    sys.exit(main())
