# COMMUNICATION-TODO — Convert "Communication" to a reference page

Plan for converting `user-manual/communication.md` (the manual's chapter 14)
into a published Diátaxis **reference** page at
`content/reference/communication.md`.

This plan is split into three small, independently reviewable tasks. Task 1
writes the page content; task 2 wires it into the site; task 3 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in COMMUNICATION-TODO.md. Update the task status
to DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; News Service + Diplomatic Messages + Enforcement | DONE |
| 2 — Wire the page into the site and apply weight | DONE |
| 3 — Build, verify, and consistency pass | DONE |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`.

---

## Goal

Produce one authoritative reference page describing communication: the **news
service** that runs on every home-planet market and trade station (what it prints
and who may insert into / receive it), **diplomatic messages** (how they are
addressed and the contact rule that lets them begin), and the fact that treaties
and agreements are **enforced by nations, not the engine**. The page must match
the house style of the existing reference pages and must **not** duplicate rules
that already live elsewhere (what a trade station or home-planet market is, what a
colony/ship is, what warfare or a trade report is) — it links to them instead.

## Source material

`user-manual/communication.md` is the source. Read it in full first. It is short —
three sub-sections:

1. **News Service** — each home-planet market and trade station has a news
   service. It prints: ship departures and arrivals; any warfare at that market's
   or trade station's planet; a trade report; and any inserted messages. Inserted
   messages must pertain to the game and should not be of too great a length. The
   parties who may insert messages and receive the news are: home-planet rulers;
   owners of colonies on the trade station's planet; and ships visiting the home
   planet or trade-station planet. Visiting ships may use the news service **only
   while visiting**.
2. **Diplomatic Messages** — sent in with a nation's turn; may be as long as
   desired. They may be addressed to a nation's name, ID number, ship ID number,
   or colony ID number; they need not be signed. They can be sent only if the
   sender has a ship or colony on/at the same planet where the recipient has a
   ship or colony. Once contact is established, messages may continue even when
   the parties are no longer in contact (the manual's flavor reason: members of
   the rulers' families have been exchanged).
3. **Enforcement of Treaties and Agreements** — all agreements reached through
   diplomacy must be enforced by the nation; the engine does not enforce them.

Do **not** edit the source — `user-manual/` is sacred (see `CLAUDE.md`); resolve
any unclear rule in our docs, never by changing the manual.

There is **no** `notes/` file for communication; there is no supplementary prep to
mine for this conversion.

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| The news service lives on **home-planet markets** | `trade.md#home-planet-markets` |
| The news service lives on **trade stations** | `trade.md#trade-stations` |
| The "trade report" the news prints | `trade.md` |
| "any warfare at that planet" the news prints | `combat.md` |
| "ship departures and arrivals" the news prints | `exploration.md#ship-movement` |
| Home-planet **rulers**; nations as rulers of a planet | `control-of-planets.md` |
| Owners of **colonies** on the station's planet; how colonies are established | `colonies-and-ships.md` (`#comparison`, `#establishment`) |
| **Ships** as message endpoints / visitors | `colonies-and-ships.md#comparison` |
| Inserting a message = a **news-release** order; the diplomatic-message order | `writing-orders.md` (stub — page-level link only) |
| Requesting colonizing permission **by diplomatic message** | `control-of-planets.md#controlled-planets` (reciprocal — wire its pending TODO; see Dependency) |

State the news-service / diplomatic-message / enforcement **rules**
authoritatively here; link out for everything in the overlap map. In particular,
do **not** re-document what a trade station or home-planet market is (owned by
`trade.md`), what a colony or ship is (owned by `colonies-and-ships.md`), what
warfare is (owned by `combat.md`), or who a ruler is (owned by
`control-of-planets.md`).

## Dependency check (correct the stale assumption)

The framing handed to this conversion listed **Trade** (Working-Index 8) and
**Control of Planets** (Working-Index 13) as not-yet-converted siblings to link at
page level or stub with `{{< callout type="warning" >}}` TODOs. That is **stale** —
verify against the repo before writing:

- **Trade is converted.** `trade.md` (weight 90) exists with `#trade-stations`
  and `#home-planet-markets` anchors. Link them with normal `relref`s — the news
  service physically lives on those two. Do **not** leave a TODO callout for
  trade.
- **Control of Planets is converted.** `control-of-planets.md` (weight 140)
  exists with `#controlled-planets`. Link it with a normal `relref` for "rulers"
  and the colonizing-permission cross-reference. Do **not** leave a TODO callout
  for control of planets.
- **Combat and Exploration are converted** (`combat.md` weight 120;
  `exploration.md`, with `#ship-movement`). Link them with normal `relref`s for
  the "warfare" and "ship departures/arrivals" the news prints.

Net result: unlike the Control-of-Planets conversion (which had Communication as a
genuine pending dependency), this page has **no pending dependency** — every link
target already exists. The only page-level (anchorless) link is the
`writing-orders.md` stub. **No `{{< callout type="warning" >}}` TODO should remain
on the finished page.** If, on writing, you find a target that genuinely does not
exist, prefer prose + a warning-callout TODO over inventing an anchor.

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Map the
manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| "player" | **nation** |
| "player's name, I.D. No." | nation name or nation ID |
| "ship ID No." | ship ID |
| "colony ID No." | colony ID |
| Home planet rulers | home-planet rulers (link `control-of-planets.md`) |
| Home planet market | home-planet market (link `trade.md#home-planet-markets`) |
| Trade station | trade station (link `trade.md#trade-stations`) |
| News service | news service |
| Inserted message / message inserted | inserted message; ordered with a news-release order (link `writing-orders.md`, page level) |
| Diplomatic message | diplomatic message (ordered with the nation's turn) |
| Trade report | trade report (link `trade.md`) |
| Warfare at the planet | warfare / combat (link `combat.md`) |
| Ship departures and arrivals | ship movement (link `exploration.md#ship-movement`) |
| Treaty / agreement | treaty; agreement (nation-enforced) |

Note: some sibling pages still say "player" in places. Use **nation** in this new
page per the house rule; do **not** undertake a broad "player → nation" rewrite of
other pages here — that is out of scope. Only the glossary entries this plan adds
or edits (task 2) are written in the "nation" voice.

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Communication`.
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Home planet markets]({{< relref "trade.md#home-planet-markets" >}})`.
- **Markdoc shortcodes:** the source has none, but if any `{% %}` Markdoc
  shortcode is encountered, fold it into prose, a table cell, or a
  `{{< callout type="info" >}}` block. No Markdoc shortcodes may survive in the
  output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications (e.g. the
  "contact persists once established" flavor note, restated factually). A
  `{{< callout type="warning" >}}` TODO is expected to be **unnecessary** here —
  see the Dependency check; do not add one unless you find a genuinely missing
  target.
- **Codes** in backticks where a code applies (this page is mostly prose; codes
  are sparse — e.g. none of news-service content maps to a unit code).
- **No rule duplication:** state the communication rules authoritatively here;
  link out for trade stations / markets, colonies, ships, warfare, the trade
  report, and rulers.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Page weight and ordering (resolved)

Weights equal the section's **1-indexed position in `user-manual/toc.json`** × 10.
That position counts `Forward` as 1, so it runs **one ahead** of the published
Working-Index number in `content/_index.md` (which starts at `1 - INTRODUCTION`,
`Forward` being unpublished). Communication is Working-Index **14** but **toc item
15**, so its weight is **150**. This matches the Working-Index step the existing
reference pages already follow (Control of Planets `140`, **Communication `150`**,
Victory Conditions `160`).

No collision and no re-weighting of other pages is required: `150` is free.
`communication` (150) sorts immediately after `control-of-planets` (140) and
before `victory-conditions` (160).

## Link targets — all already exist

- **Existing, link at the right anchor:**
  - `trade.md#home-planet-markets` and `trade.md#trade-stations` — where the news
    service lives; the trade report.
  - `combat.md` — the "warfare at that planet" the news prints.
  - `exploration.md#ship-movement` — the "ship departures and arrivals" the news
    prints.
  - `control-of-planets.md` (`#controlled-planets`) — home-planet rulers;
    colonizing permission requested by diplomatic message.
  - `colonies-and-ships.md` (`#comparison`, `#establishment`) — colonies and ships
    as message endpoints and as the basis for who may use the news service.
  - `glossary.md` — News service / Diplomatic message / News release / Treaty
    entries (task 2).
- **Existing stub, link at page level only:** `writing-orders.md` (News Release
  17.2.12 and the diplomatic-message order; the stub has no per-order anchors yet
  — link the page, not an anchor). Note: this is `content/reference/writing-orders.md`;
  there is **no** `how-to/writing-orders.md`.
- **Pending / not yet converted:** none for this page (see the Dependency check).

## Anchors this page must expose

The Working-Index sub-items 14.1–14.3 will link to these heading slugs; use them
so the wiring in task 2 resolves:

| Working Index item | Anchor |
| ------------------ | ------ |
| 14 — Communication (page top) | `communication.md` |
| 14.1 — News Service | `#news-service` |
| 14.2 — Diplomatic Messages | `#diplomatic-messages` |
| 14.3 — Enforcement of Treaties and Agreements | `#enforcement-of-treaties-and-agreements` |

---

## Task 1 — Create the page; News Service + Diplomatic Messages + Enforcement

**Status:** DONE

**Scope:** create `content/reference/communication.md` with front matter, a short
intro, and the three sections.

**Steps:**

1. Front matter: `title: Communication`, `weight: 150`.
2. Intro (1–2 sentences, reference tone): communication between nations happens
   through the **news service** carried by home-planet markets and trade stations,
   and through **diplomatic messages** sent with a nation's turn. Keep it austere —
   no "why" or strategy.
3. `## News Service` (anchor `#news-service`): every
   [home-planet market]({{< relref "trade.md#home-planet-markets" >}}) and
   [trade station]({{< relref "trade.md#trade-stations" >}}) has a news service. It
   prints: ship departures and arrivals (link
   [ship movement]({{< relref "exploration.md#ship-movement" >}})); any
   [warfare]({{< relref "combat.md" >}}) at that planet; a trade report (link
   [Trade]({{< relref "trade.md" >}})); and any inserted messages. Inserted
   messages must pertain to the game and may not be of excessive length; they are
   placed with a **news-release** order (link
   [Writing Orders]({{< relref "writing-orders.md" >}}), page level). State who may
   insert messages and receive the news: home-planet
   [rulers]({{< relref "control-of-planets.md" >}}); owners of
   [colonies]({{< relref "colonies-and-ships.md#comparison" >}}) on the trade
   station's planet; and ships visiting the home planet or trade-station planet.
   State that visiting ships may use the news service **only while visiting**.
4. `## Diplomatic Messages` (anchor `#diplomatic-messages`): a diplomatic message
   is sent with a nation's turn and may be as long as desired. It may be addressed
   to a nation's name or nation ID, a ship ID, or a colony ID, and need not be
   signed (link
   [colonies and ships]({{< relref "colonies-and-ships.md#comparison" >}}) for the
   ship/colony endpoints). State the **contact rule**: a message can be sent only
   if the sender has a ship or colony at the same planet where the recipient has a
   ship or colony. Once contact is established, the nations may continue to
   exchange messages even when no longer in contact. Fold the manual's flavor
   reason (exchanged ruler-family members) into a factual `{{< callout type="info" >}}`
   note or a single clause — do not present it as a mechanic to "use".
   Cross-reference that requesting
   [colonizing permission]({{< relref "control-of-planets.md#controlled-planets" >}})
   is done by diplomatic message.
5. `## Enforcement of Treaties and Agreements` (anchor
   `#enforcement-of-treaties-and-agreements`): all agreements reached through
   diplomacy must be enforced by the nations themselves; the engine does not
   enforce treaties or agreements. Keep it to the rule — no strategy advice.

**Acceptance criteria:**

- `content/reference/communication.md` exists with valid front matter
  (`weight: 150`).
- All three sections present with the anchors `#news-service`,
  `#diplomatic-messages`, `#enforcement-of-treaties-and-agreements`.
- News-service contents (departures/arrivals, warfare, trade report, inserted
  messages) and the eligibility list (home-planet rulers; colony owners on the
  station's planet; visiting ships, only while visiting) are stated faithfully and
  link out (not restate) for trade stations/markets, warfare, ship movement, and
  rulers.
- Diplomatic-message addressing (nation name/ID, ship ID, colony ID; unsigned
  allowed) and the contact rule (and its persistence once established) are stated
  correctly; the colonizing-permission cross-reference is present.
- Enforcement section states that agreements are nation-enforced, not
  engine-enforced.
- Reference tone throughout (states rules; no step-by-step "you should"); no
  `{% … %}` Markdoc shortcodes; "nation" per the mapping; no "Empyrean Challenge";
  no leftover `{{< callout type="warning" >}}` TODO (every target exists).

---

## Task 2 — Wire the page into the site and apply weight

**Status:** DONE

**Scope:** make the page reachable and link the Working-Index lines, the pending
Control-of-Planets TODO, and the glossary now that the page exists. No new body
content.

**Steps:**

1. **Working Index** in `content/_index.md`: replace the bare-text lines with
   `relref` links —
   - `14 - COMMUNICATION` → `communication.md` (page top);
   - `14.1 - News Service` → `communication.md#news-service`;
   - `14.2 - Diplomatic Messages` → `communication.md#diplomatic-messages`;
   - `14.3 - Enforcement of Treaties and Agreements` →
     `communication.md#enforcement-of-treaties-and-agreements`.
2. **`control-of-planets.md` pending TODO**: that page carries a
   `{{< callout type="warning" >}}` TODO (currently around lines 40–43) that says
   to link the Communication reference page (Diplomatic Messages) once it exists.
   **Replace that callout** with a real
   `[diplomatic message]({{< relref "communication.md#diplomatic-messages" >}})`
   link in the surrounding prose, and **remove** the callout. Preserve the rest of
   the section's wording.
3. **Glossary** (`glossary.md`): add alphabetical entries that don't already exist
   — keep the existing glossary style (bold term, em-dash, "See [Page]" link):
   - **Diplomatic message** (`D` section) → `communication.md#diplomatic-messages`.
   - **News release** (`N` section) — the order that inserts a message into a news
     service → `communication.md#news-service` (and/or `writing-orders.md`, page
     level).
   - **News service** (`N` section) → `communication.md#news-service`.
   - **Treaty** (`T` section) — an agreement between nations, enforced by the
     nations and not by the engine → `communication.md#enforcement-of-treaties-and-agreements`.
   Do not duplicate the existing **Market** or **Trade station** entries; if
   helpful, the **Market** entry may gain a clause noting it carries a news
   service (link `communication.md#news-service`), preserving its existing
   wording.
4. **Reciprocal links** (optional, only if genuinely helpful): `trade.md`
   (markets / trade stations) may link `communication.md#news-service` for "carries
   a news service". Preserve the host page's wording; just add the `relref`. Do not
   otherwise edit the DONE pages.

**Acceptance criteria:**

- `content/_index.md` no longer has bare `COMMUNICATION` / `News Service` /
  `Diplomatic Messages` / `Enforcement of Treaties and Agreements` text for items
  14–14.3; all resolve via `relref`.
- `control-of-planets.md` links the new page for diplomatic messages and no longer
  carries the Communication TODO callout.
- Glossary has the new **Diplomatic message**, **News release**, **News service**,
  and **Treaty** entries, each linking correctly and staying alphabetical.
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
3. Confirm sidebar order: `communication` (150) sits after `control-of-planets`
   (140) and before `victory-conditions` (160).
4. Confirm every `relref` in the new page targets an existing file and that each
   anchor (`#home-planet-markets`, `#trade-stations`, `#ship-movement`,
   `#comparison`, `#controlled-planets`) resolves, and that the Working-Index
   anchors (`#news-service`, `#diplomatic-messages`,
   `#enforcement-of-treaties-and-agreements`) match the headings the page actually
   emits.
5. Confirm **no** TODO callout remains on `communication.md`, and that the
   Communication TODO callout was removed from `control-of-planets.md` and replaced
   with a working link.
6. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed),
   no engine code added, no duplication of rules owned by `trade.md`, `combat.md`,
   `exploration.md`, `colonies-and-ships.md`, or `control-of-planets.md`.

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- Sidebar shows `communication` after `control-of-planets` and before
  `victory-conditions`.
- The page reads as authoritative reference and defers (via links) to the pages in
  the overlap map for shared rules; no TODO callouts remain on it, and the
  Control-of-Planets pending link is now resolved.

---

## Out of scope

- The Trade, Control of Planets, Combat, and Exploration reference pages
  themselves — their own plans/conversions. (All are already DONE and are linked
  here with real `relref`s, not TODOs.)
- Re-documenting trade stations / home-planet markets (owned by `trade.md`),
  colonies/ships (owned by `colonies-and-ships.md`), warfare (owned by
  `combat.md`), ship movement (owned by `exploration.md`), or who a ruler is
  (owned by `control-of-planets.md`) — link to them.
- Writing the news-release / diplomatic-message order detail (owned by the future
  `writing-orders.md` build) — link at page level only.
- A broad "player → nation" rewrite of other DONE pages; only the glossary entries
  added/edited in task 2 are written in the "nation" voice.
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/communication.md`.
