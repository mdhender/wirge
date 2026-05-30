# CONTROL-OF-PLANETS-TODO — Convert "Control of Planets" to a reference page

Plan for converting `user-manual/control-of-planets.md` (the manual's chapter 13)
into a published Diátaxis **reference** page at
`content/reference/control-of-planets.md`.

This plan is split into three small, independently reviewable tasks. Task 1
writes the page content; task 2 wires it into the site; task 3 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in CONTROL-OF-PLANETS-TODO.md. Update the task
status to DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; Taking control + Controlled planets + Relinquishing | DONE |
| 2 — Wire the page into the site and apply weight | DONE |
| 3 — Build, verify, and consistency pass | DONE |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`.

---

## Goal

Produce one authoritative reference page describing control of planets: how a
nation establishes control, how simultaneous control is resolved, what a nation
must do to colonize a planet another nation controls (bombard/capture, or
permission for considerations), and how control is relinquished. The page must
match the house style of the existing reference pages and must **not** duplicate
rules that already live elsewhere (combat capture, trade stations, colony
establishment, the victory condition) — it links to them instead.

## Source material

`user-manual/control-of-planets.md` is the source. Read it in full first. It is
short — three sub-sections:

1. **Taking Control** — control requires an orbiting or surface colony, or a
   trade station, at the planet; the nation declares rulership with a control
   order; when two nations send control orders for the same planet on the same
   turn, the computer randomly selects one to establish the colony and rule, and
   the other order is aborted.
2. **Controlled Planets** — to colonize a planet another nation controls, a
   nation may (a) bombard or capture the existing colony, or (b) request
   permission by diplomatic message, agreeing to whatever consideration the ruler
   wants. Considerations listed: a large initial fee; a percentage of mined
   resources; a quarterly or annual fee in gold; or sole buying and selling
   through the ruler's trade station, if the ruler has one.
3. **Relinquishing Planets** — a nation may relinquish control at any time with an
   uncontrol order.

Do **not** edit the source — `user-manual/` is sacred (see `CLAUDE.md`); resolve
any unclear rule in our docs, never by changing the manual.

There is **no** `notes/` file for control of planets; there is no supplementary
prep to mine for this conversion.

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| Orbiting/surface colony as the basis of control; how colonies are established | `colonies-and-ships.md` (`#comparison`, `#establishment`) |
| A trade station may also establish control (it is an orbiting colony) | `trade.md#trade-stations`; `colonies-and-ships.md#comparison` |
| The planet being controlled; the planet-side summary of control | `planets.md#control` |
| "controls the most planets" / 100-planet threshold is the win condition | `victory-conditions.md` |
| Bombard or capture the existing colony to take a controlled planet | `combat.md#bombardment`; `combat.md#captured-colonies` |
| Sole buying/selling at the ruler's trade station as a consideration | `trade.md#trade-stations` |
| Request permission by **diplomatic message** | Communication (section 14 — **not yet converted**; see Dependency below) |
| Control order, uncontrol order, colonizing-permission order (how to order) | `writing-orders.md` (stub — page-level link only) |

State the control/relinquish/permission **rules** authoritatively here; link out
for everything in the overlap map. In particular, do **not** re-document how a
colony bombards or is captured (owned by `combat.md`), what a trade station is
(owned by `trade.md`), or how a colony is established (owned by
`colonies-and-ships.md`).

## Dependency to flag (correct the stale assumption)

The original framing of this conversion listed Combat, Communication, and Trade
as three not-yet-converted siblings. That is **stale** — verify against the repo:

- **Combat is converted.** `combat.md` (weight 120) exists with full anchors,
  including `#bombardment` and `#captured-colonies`. Link them with normal
  `relref` — do **not** leave a TODO callout for combat.
- **Trade is converted.** `trade.md` (weight 90) exists with `#trade-stations`.
  Link it with a normal `relref` for the "ruler's trade station" consideration.
- **Communication is the only genuine pending dependency.** There is **no**
  `communication.md` (section 14 is unconverted). The "request permission by
  diplomatic message" rule references it. Do **not** invent a link: state the
  rule in prose and leave a `{{< callout type="warning" >}}` TODO to wire a
  `relref` to the Communication reference page (Diplomatic Messages, the manual's
  14.2) once it exists.

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Map the
manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| "player" | **nation** |
| Ruler / "the planet's ruler" | ruler (the nation that controls the planet) |
| Control order | control order (link `writing-orders.md`, page level) |
| Uncontrol order | uncontrol order (link `writing-orders.md`, page level) |
| Request permission (diplomatic message) | colonizing-permission order / diplomatic message (Communication pending) |
| Orbiting or surface colony | orbiting or surface colony (link `colonies-and-ships.md`) |
| Trade station | trade station (link `trade.md#trade-stations`) |
| Consideration / condition | consideration |
| Gold (quarterly/annual fee) | `GOLD` |
| Mined resources (a percentage of) | mined resources (`METS` / `NMTS` — link `mining.md` only if natural) |

Note: the existing sibling pages (`victory-conditions.md`, the `planets.md`
Control section, the glossary **Control** entry) currently say "player". Use
**nation** in this new page per the house rule; where task 2 already edits the
glossary **Control** entry, align it to "nation" too. Do not undertake a broad
"player → nation" rewrite of the other DONE pages here — that is out of scope.

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Control of Planets`.
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Trade stations]({{< relref "trade.md#trade-stations" >}})`.
- **Markdoc shortcodes:** the source has none, but if any `{% %}` Markdoc
  shortcode is encountered, fold it into prose, a table cell, or a
  `{{< callout type="info" >}}` block. No Markdoc shortcodes may survive in the
  output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications,
  `{{< callout type="warning" >}}` for `TODO`s about unconverted material (here:
  the Communication link).
- **Codes** in backticks (`GOLD`, and any others used).
- **No rule duplication:** state the control rules authoritatively here; link out
  for combat capture, trade stations, colony establishment, and the victory
  condition.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Page weight and ordering (resolved)

Weights equal the section's **1-indexed position in `user-manual/toc.json`** × 10.
That position counts `Forward` as 1, so it runs **one ahead** of the published
Working-Index number in `content/_index.md` (which starts at `1 - INTRODUCTION`,
`Forward` being unpublished). Control of Planets is Working-Index **13** but
**toc item 14**, so its weight is **140**. This matches the Working-Index step the
existing reference pages already follow (Espionage `130`, **Control of Planets
`140`**, Communication would be `150`).

No collision and no re-weighting of other pages is required: `140` is free.
`control-of-planets` (140) sorts immediately after `espionage` (130) and before
any future `communication` (150) and `victory-conditions` (160).

## Link targets — existing vs. pending

- **Existing, link at the right anchor:**
  - `colonies-and-ships.md` (`#comparison`, `#establishment`) — colonies/trade
    stations as the basis of control.
  - `trade.md#trade-stations` — a trade station may control; the ruler's station
    consideration.
  - `planets.md#control` — the planet-side summary of control (reciprocal; task 2
    wires the existing `planets.md` Control-section TODO to point here).
  - `victory-conditions.md` — controlling planets is the win condition (DONE
    page).
  - `combat.md` (`#bombardment`, `#captured-colonies`) — bombard/capture a
    controlled planet's colony.
  - `glossary.md` — Control / control order / uncontrol order / ruler entries.
- **Existing stub, link at page level only:** `writing-orders.md` (Control Orders
  17.2.17, Un-Control Orders 17.2.18, Colonizing Permission 17.2.21 — the stub
  has no per-order anchors yet; link the page, not an anchor).
- **Pending / not yet converted:** Communication (section 14) has **no** page.
  Leave a `{{< callout type="warning" >}}` TODO for the Diplomatic Messages link
  rather than inventing one.

## Anchors this page must expose

The Working-Index sub-items 13.1–13.3 link to these heading slugs; use them so the
wiring in task 2 resolves:

| Working Index item | Anchor |
| ------------------ | ------ |
| 13 — Control of Planets (page top) | `control-of-planets.md` |
| 13.1 — Taking Control | `#taking-control` |
| 13.2 — Controlled Planets | `#controlled-planets` |
| 13.3 — Relinquishing Planets | `#relinquishing-planets` |

---

## Task 1 — Create the page; Taking control + Controlled planets + Relinquishing

**Status:** DONE

**Scope:** create `content/reference/control-of-planets.md` with front matter, a
short intro, and the three sections.

**Steps:**

1. Front matter: `title: Control of Planets`, `weight: 140`.
2. Intro (1–2 sentences, reference tone): control is a nation's claim over a
   planet, held through a colony or trade station there; it underlies the
   [victory condition]({{< relref "victory-conditions.md" >}}). Keep it austere —
   no "why" or strategy.
3. `## Taking control` (anchor `#taking-control`): a nation establishes control of
   a planet by having an orbiting or surface colony — or a
   [trade station]({{< relref "trade.md#trade-stations" >}}) — there (link
   `colonies-and-ships.md#establishment` / `#comparison` for what a colony is and
   how it is established) and declaring rulership with a **control order** (link
   `writing-orders.md`, page level). When two nations send control orders for the
   same planet on the same turn, the computer randomly selects one to establish
   the colony and become ruler; the other nation's order is aborted.
4. `## Controlled planets` (anchor `#controlled-planets`): to colonize a planet
   another nation controls, a nation has two options:
   - **Bombard or capture** the ruler's colony — link
     [Bombardment]({{< relref "combat.md#bombardment" >}}) and
     [Captured colonies]({{< relref "combat.md#captured-colonies" >}}); do not
     restate combat mechanics.
   - **Request permission** by diplomatic message, agreeing to the ruler's
     considerations. List the considerations the manual gives: a large initial
     fee; a percentage of mined resources; a quarterly or annual fee in `GOLD`;
     or sole buying and selling through the ruler's
     [trade station]({{< relref "trade.md#trade-stations" >}}). Point ordering to
     [Writing Orders]({{< relref "writing-orders.md" >}}) (colonizing-permission
     order, page level).

   The diplomatic-message channel itself is Communication (section 14), not yet
   converted — state the rule in prose and add:

   ```
   {{< callout type="warning" >}}
   **TODO:** Link the Communication reference page (Diplomatic Messages) here with
   a `relref` once that page exists.
   {{< /callout >}}
   ```

5. `## Relinquishing planets` (anchor `#relinquishing-planets`): a nation may
   relinquish control of a planet at any time with an **uncontrol order** (link
   `writing-orders.md`, page level).

**Acceptance criteria:**

- `content/reference/control-of-planets.md` exists with valid front matter
  (`weight: 140`).
- All three sections present with the anchors `#taking-control`,
  `#controlled-planets`, `#relinquishing-planets`.
- Control basis (colony / trade station) and the simultaneous-control random
  resolution are stated; combat capture, trade stations, and colony
  establishment are **linked, not restated**.
- The considerations list is faithful to the source (`GOLD` for the fee).
- Combat (`#bombardment`, `#captured-colonies`) and Trade (`#trade-stations`) are
  linked with real `relref`s; only the Communication link is a warning-callout
  TODO.
- Reference tone throughout (states rules; no step-by-step "you should"); no
  `{% … %}` Markdoc shortcodes; "nation" per the mapping; no "Empyrean
  Challenge".

---

## Task 2 — Wire the page into the site and apply weight

**Status:** TODO

**Scope:** make the page reachable and link the Working-Index lines, the planet
Control section, and the glossary now that the page exists. No new body content.

**Steps:**

1. **Working Index** in `content/_index.md`: replace the bare-text lines with
   `relref` links —
   - `13 - CONTROL OF PLANETS` → `control-of-planets.md` (page top);
   - `13.1 - Taking Control` → `control-of-planets.md#taking-control`;
   - `13.2 - Controlled Planets` → `control-of-planets.md#controlled-planets`;
   - `13.3 - Relinquishing Planets` →
     `control-of-planets.md#relinquishing-planets`.
2. **`planets.md` Control section**: the `## Control` section currently says "see
   Control of Planets for the full rules" in plain text and carries a
   `{{< callout type="warning" >}}` TODO to wire that link once the page exists.
   Replace the plain-text reference with a
   `[Control of Planets]({{< relref "control-of-planets.md" >}})` link and
   **remove** the TODO callout. Preserve the rest of the section's wording.
3. **Glossary** (`glossary.md`):
   - Update the existing **Control** entry (currently "A player's claim …", no
     `relref`) to use **nation** and link
     `[Control of Planets]({{< relref "control-of-planets.md" >}})`.
   - Add a **Control order** entry → `control-of-planets.md#taking-control`
     (and/or `writing-orders.md` page level).
   - Add an **Uncontrol order** entry →
     `control-of-planets.md#relinquishing-planets`. Place it alphabetically near
     the existing `U` entries (Unemployables / Unit / Unskilled worker).
   - Add a **Ruler** entry — the nation that controls a planet —
     → `control-of-planets.md`.
   - The existing **Trade station** entry already notes it "can also establish
     control of a planet"; optionally add a `relref` to
     `control-of-planets.md#taking-control`. Keep all entries alphabetical and
     consistent with the existing glossary style.
4. **Reciprocal link** (optional, only if genuinely helpful): `victory-conditions.md`
   may link `control-of-planets.md` for what "control" means. Preserve the host
   page's wording; just add the `relref`. Do not otherwise edit the DONE
   victory-conditions page.

**Acceptance criteria:**

- `content/_index.md` no longer has bare `CONTROL OF PLANETS` / `Taking Control`
  / `Controlled Planets` / `Relinquishing Planets` text for items 13–13.3; all
  resolve via `relref`.
- `planets.md` Control section links the new page and no longer carries the
  Control-of-Planets TODO callout.
- Glossary **Control** entry links the new page and says "nation"; new
  **Control order**, **Uncontrol order**, and **Ruler** entries link correctly
  and stay alphabetical.
- Any reciprocal link added resolves and preserves the host page's wording.

---

## Task 3 — Build, verify, and consistency pass

**Status:** DONE

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build with **no** `relref` "not found"
   errors and no duplicate-weight warnings.
2. Grep the changed pages for leftover Markdoc shortcodes (`{%`), broken/relative
   Markdown links, and the string "Empyrean Challenge".
3. Confirm sidebar order: `control-of-planets` (140) sits after `espionage` (130)
   and before `victory-conditions` (160).
4. Confirm every `relref` in the new page targets an existing file and that each
   anchor (`#establishment`, `#comparison`, `#trade-stations`, `#bombardment`,
   `#captured-colonies`, `#control`) resolves, and that the Working-Index anchors
   (`#taking-control`, `#controlled-planets`, `#relinquishing-planets`) match the
   headings the page actually emits.
5. Confirm exactly one remaining TODO callout on the page — the Communication /
   Diplomatic Messages link — and that no combat or trade dependency was left as
   a TODO (both are converted and must be linked).
6. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed),
   no engine code added, no duplication of rules owned by `combat.md`,
   `trade.md`, or `colonies-and-ships.md`.

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- Sidebar shows `control-of-planets` after `espionage`.
- The page reads as authoritative reference and defers (via links) to the pages
  in the overlap map for shared rules; the only TODO is the pending Communication
  link.

---

## Out of scope

- The Combat, Communication, and Trade reference pages themselves — their own
  plans/conversions. (Combat and Trade are already DONE and are linked here;
  Communication is pending and is a warning-callout TODO only.)
- Re-documenting combat capture/bombardment (owned by `combat.md`), trade
  stations (owned by `trade.md`), or colony establishment (owned by
  `colonies-and-ships.md`) — link to them.
- Writing the control-order / uncontrol-order / colonizing-permission order detail
  (owned by the future `writing-orders.md` build) — link at page level only.
- A broad "player → nation" rewrite of the other DONE pages (`victory-conditions.md`,
  `planets.md`); only the glossary **Control** entry edited in task 2 is aligned
  to "nation".
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/control-of-planets.md`.
