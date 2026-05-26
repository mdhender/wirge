# wirge

**wirge** is the documentation project for **Epimethean Challenge**, a
play-by-email strategy game. It produces a static documentation website and
serves as the authoritative specification for the game.

The game engine and web app are developed separately in
[pyre](https://github.com/mdhender/pyre). This repository (`wirge`) contains only
the documentation and the Hugo site that publishes it — no engine code. This
repository is hosted at <https://github.com/mdhender/wirge>.

## Goals

- **Accessible** — published as a static website anyone can read.
- **Usable** — organized following the [Diátaxis](https://diataxis.fr)
  documentation framework.
- **Authoritative** — the documentation here is the source of truth for
  implementing the game in `pyre`. When the code and the docs disagree, the docs
  win and the code gets fixed.

## Documentation structure

The published documentation follows [Diátaxis](https://diataxis.fr), which
divides documentation into four modes:

| Directory      | Diátaxis mode  | Orientation         |
| -------------- | -------------- | ------------------- |
| `tutorial/`    | Tutorials      | Learning-oriented   |
| `how-to/`      | How-to guides  | Task-oriented       |
| `reference/`   | Reference      | Information-oriented |
| `explanation/` | Explanation    | Understanding-oriented |

## The original user manual (`user-manual/`)

The `user-manual/` directory holds the original game rule book (© 1978 Vern
Holford, owned by James Colombo). It is **internal reference material only** and
is **not** published to the website.

We treat the original manual as sacred:

- We **do** correct typographical errors as we find them.
- We do **not** edit it for clarity.
- We do **not** "fix" contradictions or ambiguities in the rules.

Where the original rules are unclear or contradictory, we resolve that in *our*
documentation (the Diátaxis docs above) — never by changing the manual.

## Building the site

The site is built with [Hugo](https://gohugo.io) (Extended) using the
[Hextra](https://imfing.github.io/hextra/) theme, which is pulled in as a Hugo
module (see `go.mod`). We expect to adopt Hextra features such as shortcodes
over time, as the need arises.

Requirements: Hugo Extended and Go (for the module-based theme).

```sh
hugo server   # local preview at http://localhost:1313
hugo          # build the static site into public/
hugo mod get -u ./...   # update the Hextra theme module
```

### Layout

```text
wirge/
├── hugo.toml          # Hugo + Hextra site configuration
├── go.mod / go.sum    # Hugo module deps (pins the Hextra theme version)
├── content/           # published site content (Diátaxis)
│   ├── _index.md
│   ├── tutorial/
│   ├── how-to/
│   ├── reference/
│   └── explanation/
├── user-manual/       # original manual — internal reference, NOT published
├── notes/             # working notes — NOT published
├── deploy/            # sample Nginx / Caddy configs (serve public/ under /docs)
├── README.md          # this file
├── CLAUDE.md          # guidance for working in this repo
├── LICENSE.md         # licensing overview
└── LICENSE-docs.md    # CC BY-NC-SA 4.0 text for the project documentation
```

The four Diátaxis directories live under `content/`, so Hugo publishes them.
`user-manual/` and `notes/` stay outside `content/` so Hugo never publishes
them.

## License

This repository contains two separately licensed bodies of work:

- **The original user manual** (`user-manual/`) — © 1978 Vern Holford, owned by
  James Colombo. All rights reserved; included with permission. Not covered by
  the Creative Commons license below.
- **All other documentation** — © 2026 Michael D Henderson, licensed under
  [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Commercial use of any material in this repository requires separate written
permission from the respective copyright holder(s).

See [`LICENSE.md`](LICENSE.md) for full details.
