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
- Within a section, set each page's `weight` from its position in
  `user-manual/toc.json` (the manual's canonical order) **times 10** — e.g. "Game
  Set Up" is 4th in the toc, so `content/reference/game-setup.md` is `weight: 40`.
  This keeps pages in the manual's order and leaves gaps so new pages slot in
  without renumbering.
- Build/preview: `hugo server` (preview at http://localhost:1313), `hugo`
  (build into `public/`, which is git-ignored). Update the theme with
  `hugo mod get -u ./...`.

## Recording clarifications vs. rule changes

The manual stays untouched; everything we decide is captured **in place, in our
own voice, in the relevant `content/` page** — there is no separate changelog.
Three tiers, distinguished by Hextra callout type, keep "we clarified" separate
from "we changed the rules":

1. **Clarification** — resolving an ambiguity or pinning down a special case
   *without changing the rule*. Write it into the reference prose. When it
   deserves to be set apart, use an **`info` callout** with a bolded topic label
   (not a warning), e.g. `content/reference/exploration.md` "**Movement between
   stars of one system.**"
2. **Deviation or addition** — anywhere we genuinely depart from or add to the
   rule book. Use a **`warning` callout** opening with a standard bolded phrase:
   **"Differs from the rule book."**, **"Not in the rule book."**, or **"Not in
   this version."** State what the book says, what we do instead, and why.
   Material unit/code changes also get an entry in the "Differences from the rule
   book" section of `content/reference/units.md`, and old→new term mappings go in
   the glossary.
3. **Open question** — anything not yet pinned down. Use a **`warning` callout**
   (or inline) opening with **`TODO:`**.

**Never correct a rule silently.** If our number or formula disagrees with the
printed book, always flag it — but pick the tier by *intent*. A typo (where the
book's own worked example agrees with us) is a tier-1 clarification, e.g. the
energy-weapon `(F / D)` note in `content/reference/combat.md`. A deliberate change
is a tier-2 deviation. When the disagreement is a downstream *consequence* of a
model change we already made (e.g. reclassifying a binary star-to-star hop from
the manual's "interstellar jump" to our in-system `move`, which makes its 0.2-ly
distance an in-system case), reconcile every page the change touches so they state
one rule — don't leave one page asserting the pre-change version.

## Deploying

**Only deploy when the user explicitly asks.** Deploying publishes to the live
site; never run a deploy on your own initiative, even after committing or
pushing. Wait for an explicit instruction to deploy.

The live site (<https://ec.pbbgaming.com/docs/>) is built **on the server** from a
git checkout — the server publishes the commit it pulls, not your working tree.
Everyday flow:

1. Commit and **push to `main`** first. Unpushed work won't go live, and a deploy
   without a preceding push just republishes stale content.
2. Run `deploy/deploy-docs.sh` from your laptop. It SSHes to the server and runs
   `/opt/wirge/deploy.sh`, which `git pull --ff-only`s and rebuilds `public/` with
   `hugo --gc --minify`.
3. Verify: `curl -sI https://ec.pbbgaming.com/docs/ | head -1` (expect `200`).

See `deploy/README.md` for the full runbook and one-time server setup.

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
