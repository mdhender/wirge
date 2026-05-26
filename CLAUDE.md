# CLAUDE.md

Guidance for working in the **wirge** repository. See `README.md` for the
project overview.

## What this repo is

`wirge` is the documentation project for **Epimethean Challenge**, a play-by-email
strategy game. It contains documentation and the Hugo site that publishes it —
**no engine code**.

- This repo: <https://github.com/mdhender/wirge> (docs + Hugo site).
- The game engine and web app live in a **separate** repo,
  [`pyre`](https://github.com/mdhender/pyre). Do not add engine code here.
- The documentation here is the **authoritative specification** for `pyre`. When
  the code and the docs disagree, the docs are correct and the code gets fixed.

## Naming and IP rules (important)

- The game's public name is **"Epimethean Challenge."** Use it everywhere the
  project speaks in its own voice (the README, the published site, our docs).
- James Colombo owns both the original rule book and the name **"Empyrean
  Challenge."** We have rights to the book's *content* (with his permission) but
  **not** to the name.
- Therefore, in files we author, do **not** brand anything "Empyrean Challenge."
  Name "Empyrean Challenge" only when restating James Colombo's ownership (e.g.
  `user-manual/LICENSE.md`).
- Spell the owner's name **"James Colombo"** (not "Columbo").
- Attribute the author as **"Michael D Henderson"** (with the middle initial) in
  copyright lines, front matter, and docs.

## The original user manual (`user-manual/`) is sacred

`user-manual/` holds the original *Empyrean Challenge* rule book. It is **internal
reference only** and is **never published** to the site.

- **Do** fix typographical errors when found.
- **Do not** edit it for clarity, style, or flow.
- **Do not** "fix" contradictions or ambiguities in the rules.
- Resolve unclear or contradictory rules in **our** documentation (the Diátaxis
  docs), never by changing the manual.
- Treat the manual's own notices (e.g. `forward.md`) as part of the original
  document — leave their wording intact apart from typo fixes.

## Documentation conventions

- Our documentation follows the [Diátaxis](https://diataxis.fr) framework, split
  into four modes: `tutorial/` (learning), `how-to/` (tasks), `reference/`
  (information), `explanation/` (understanding). Put new content in the mode that
  matches its purpose; don't mix modes in one page.
- The site is built with [Hugo](https://gohugo.io) (Extended) using the
  [Hextra](https://imfing.github.io/hextra/) theme, pulled in as a Hugo module
  (`go.mod`/`go.sum` pin the version). Follow whatever Markdown style and
  conventions Hugo/Hextra prefer, **including front matter**, as documentation is
  created. We'll adopt Hextra features (e.g. shortcodes) as the need arises.
- Published content lives under `content/`, organized into the four Diátaxis
  directories (each with an `_index.md`; `weight` in front matter sets sidebar
  order). `user-manual/` and `notes/` stay **outside** `content/` so they are
  never published.
- Build/preview: `hugo server` (preview at http://localhost:1313), `hugo`
  (build into `public/`, which is git-ignored). Update the theme with
  `hugo mod get -u ./...`.

## What is published vs. internal

| Path | Published? | Notes |
| ---- | ---------- | ----- |
| `content/` (`tutorial/`, `how-to/`, `reference/`, `explanation/`) | Yes | Our Diátaxis docs (CC BY-NC-SA 4.0) |
| `user-manual/` | **No** | Sacred reference; all rights reserved (James Colombo) |
| `notes/` | **No** | Working notes |

## Licensing

Two separately licensed bodies of work (see `LICENSE.md`):

- `user-manual/` — © 1978 Vern Holford, owned by James Colombo; all rights
  reserved; included with permission.
- Everything else — © 2026 Michael D Henderson, CC BY-NC-SA 4.0
  (`LICENSE-docs.md`).

Commercial use of any material requires separate written permission from the
respective copyright holder.
