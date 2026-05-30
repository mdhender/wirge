# ESPIONAGE-TODO — Convert "Espionage" to a reference page

Plan for converting `user-manual/espionage.md` (the manual's chapter 12) into a
published Diátaxis **reference** page at `content/reference/espionage.md`.

This plan is split into four small, independently reviewable tasks. Tasks 1–2
write the page content; task 3 wires it into the site; task 4 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in ESPIONAGE-TODO.md. Update the task status to
DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; intro + Spy Functions table + functions A–C | DONE |
| 2 — Functions D–F (suppression math) | DONE |
| 3 — Wire the page into the site and apply weight | DONE |
| 4 — Build, verify, and consistency pass | DONE |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`.

---

## Goal

Produce one authoritative reference page describing espionage: what a spy unit
is, the six functions a spy unit can perform, the rules governing where and how
long a spy operates, and the suppression (assassination) math. The page must
match the house style of the existing reference pages and must **not** duplicate
rules that already live elsewhere (rebellion mechanics, the `SPY` cadre
allocation) — it links to them instead.

## Source material

`user-manual/espionage.md` is the source. Read it in full first. It contains: a
one-paragraph definition of a spy unit, the **Spy Functions** table (`CODE` /
`ACTION`, six rows A–F), the "must be at that ship/colony" and persistence rules,
a sub-section describing each of the six functions, the suppression/assassination
math, and two `{% footnote %}` footnotes. Do **not** edit the source —
`user-manual/` is sacred (see `CLAUDE.md`); resolve any unclear rule in our docs,
never by changing the manual.

No `notes/` file covers espionage; there is no supplementary prep to mine for
this conversion.

The source's authoritative data points to carry over faithfully:

1. **Spy unit composition** — one soldier unit (`SLD`) + one professional unit
   (`PRO`); this is the `SPY` cadre already defined in `population.md`.
2. **One function per unit per turn** (footnote 1).
3. **The six functions** (A–F) and each function's effect (table + sub-sections).
4. **Locality rule** — a spy must be at the ship/colony to function there.
5. **Persistence rule** — a spy keeps performing its ordered function until
   re-ordered.
6. **Suppression / assassination math** — attackers destroy foreign spies equal
   to 3× the attackers' number; attackers lose 1/6 of the defenders' number; the
   worked example (21 attack 12 → 2 attackers and 7 foreign spies lost); these
   quantities vary by up to ±50% for chance (footnote 2).
7. **Rounding** — espionage results round all fractions **down** (e.g. the 1/6
   loss in the suppression math). This is a project rule, not stated in the
   source; it applies to every function's numeric result.

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| What a rebel is; how rebels accumulate; rebellion outcome | `rebellion.md` (`#rebels`, `#when-rebellion-occurs`) |
| Functions A/B/E described from the rebellion side | `rebellion.md#learning-rebel-counts` |
| `SPY` cadre = 1 `PRO` + 1 `SLD`; cadre pay/death | `population.md#population-cadres` |
| `SLD` / `PRO` population classes | `population.md#population-classes`; `units.md#population-units` |
| Spies operate on ships/colonies (S/C entities) | `colonies-and-ships.md`; `units.md#entities` |
| Spy orders (how to order a function) | `writing-orders.md` (stub — page-level link) |

`rebellion.md#learning-rebel-counts` already paraphrases functions A (Rebel
quantity and type), B (Convert rebels), and E (Incite rebellion) from the
rebellion side. This espionage page is the canonical home for the **full**
function catalog, so it states each function's effect; keep the descriptions to
the function's effect and link `rebellion.md` for what a rebel is and what
rebellion does. Add a reciprocal link from `rebellion.md#learning-rebel-counts`
back to the espionage page (task 3).

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"/"ruler").
Map the manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| Spy unit | spy unit (the `SPY` cadre) |
| Soldier unit | `SLD` |
| Professional unit | `PRO` |
| "ruler" / "player" | **nation** |
| Function (A–F) | spy function; keep the letter code in `backticks` (`A`–`F`) |
| Foreign spy | foreign spy (a spy belonging to another nation) |
| Ship/colony | ship or colony (S/C entity) |

The six functions and their codes (render the table faithfully):

| Code | Action |
| ---- | ------ |
| `A` | Rebel Quantity and Type |
| `B` | Convert Rebels |
| `C` | Uncover Foreign Spy |
| `D` | Suppress Foreign Spy |
| `E` | Incite Rebellion |
| `F` | Obtain Secrets |

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Espionage`.
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Rebellion]({{< relref "rebellion.md#learning-rebel-counts" >}})`.
- **Footnotes:** the source uses Markdoc `{% footnotes %}` / `{% footnote %}` /
  `{% fnref %}` shortcodes, which do **not** render in Hugo/Hextra. Fold both
  footnotes into prose, a table cell, or a `{{< callout type="info" >}}` block:
  - Footnote 1 ("only one function per unit per turn; for ordering see Writing
    Orders") → fold into the intro prose; the "see Writing Orders" pointer
    becomes a `relref` to `writing-orders.md` (page level).
  - Footnote 2 ("these quantities will vary by up to ±50% for the element of
    chance") → fold into the Suppress Foreign Spy section, as prose or an info
    callout adjacent to the math.
  No Markdoc shortcodes may survive in the output.
- **Codes** in backticks (`SPY`, `SLD`, `PRO`, `A`–`F`).
- **Render the Spy Functions table faithfully** (`Code` / `Action`, six rows).
- **No rule duplication:** state the spy-function catalog authoritatively here;
  link `rebellion.md` for rebel/rebellion mechanics and `population.md` for the
  `SPY` cadre. Do not re-explain what a rebel is or when a colony revolts.
- **Callouts:** `{{< callout type="info" >}}` for clarifications,
  `{{< callout type="warning" >}}` for `TODO`s about unconverted material.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Page weight and ordering (resolved)

Weights equal the section's **1-indexed position in `user-manual/toc.json`** × 10.
That position counts `Forward` as 1, so it runs **one ahead** of the published
Working-Index number in `content/_index.md` (which starts at `1 - INTRODUCTION`,
`Forward` being unpublished). Espionage is Working-Index **12** but **toc item
13**, so its weight is **130**. This matches the Working-Index step the existing
reference pages already follow (Combat `120`, Espionage `130`, Control of Planets
would be `140`).

No collision and no re-weighting of other pages is required: `130` is free.
`espionage` (130) sorts immediately after `combat` (120) and before any future
`control-of-planets` (140).

## Link targets — existing vs. pending

All link targets this page needs **already exist**; no new stub pages are
required.

- **Existing, link at the right anchor:** `rebellion.md`
  (`#learning-rebel-counts`, `#rebels`, `#when-rebellion-occurs`),
  `population.md` (`#population-cadres`, `#population-classes`),
  `units.md` (`#population-units`, `#entities`), `colonies-and-ships.md`,
  `glossary.md`.
- **Existing stub, link at page level only:** `writing-orders.md` (Spy Orders is
  the manual's 17.2.11; the stub has no per-order anchors yet — link the page,
  not an anchor).
- **Combat (Working-Index 11) is already converted** — `combat.md` (weight 120)
  exists with full anchors. The earlier assumption that Combat was unconverted is
  stale; if a combat link is ever wanted it can be a normal `relref`. Espionage
  has no strong overlap with combat, so likely **no** combat link is needed.
- **Pending / not yet converted:** Control of Planets (section 13) and
  Communication (section 14) have **no** pages. Espionage does not require a link
  to either; if one ever seems warranted, leave a
  `{{< callout type="warning" >}}` TODO rather than inventing a link.

## Anchors this page must expose

The Working-Index sub-items 12.1–12.6 will link to per-function anchors. Use
these heading slugs so the wiring in task 3 resolves:

| Working Index item | Anchor |
| ------------------ | ------ |
| 12 — Espionage (page top) | `espionage.md` |
| (Spy Functions table) | `#spy-functions` |
| 12.1 — Rebel Quantity and Type | `#rebel-quantity-and-type` |
| 12.2 — Convert Rebels | `#convert-rebels` |
| 12.3 — Uncover Foreign Spy | `#uncover-foreign-spy` |
| 12.4 — Suppress Foreign Spy | `#suppress-foreign-spy` |
| 12.5 — Incite Rebellion | `#incite-rebellion` |
| 12.6 — Obtain Secrets | `#obtain-secrets` |

---

## Task 1 — Create the page; intro + Spy Functions table + functions A–C

**Status:** DONE

**Scope:** create `content/reference/espionage.md` with front matter, the intro
paragraph, the `## Spy functions` table, the locality/persistence rules, and the
first three function sections (A Rebel Quantity and Type, B Convert Rebels,
C Uncover Foreign Spy).

**Steps:**

1. Front matter: `title: Espionage`, `weight: 130`.
2. Intro (reference tone): a spy unit is the `SPY` cadre — one soldier unit
   (`SLD`) plus one professional unit (`PRO`); link
   `population.md#population-cadres`. State that a spy unit performs **one**
   function per turn (folding footnote 1), that to act on a ship or colony the
   spy must be **at** that ship or colony, and that a spy continues its ordered
   function until re-ordered. Point ordering to
   [Writing Orders]({{< relref "writing-orders.md" >}}) (page level — fold the
   "see Writing Orders" pointer from footnote 1). State once, here, that
   espionage results round all fractions **down** (this is the page-wide rule;
   the suppression math in task 2 is the most visible case).
3. `## Spy functions`: render the six-row `Code` / `Action` table faithfully
   (codes `A`–`F` in backticks). A short lead-in sentence may introduce it; do
   not add instruction or commentary.
4. Function sections (use `##` headings so the per-function anchors resolve):
   - `## Rebel quantity and type` (`A`): reports, to the spy's own nation, the
     number of rebels on its ships and colonies and their population type; one
     spy unit is required per ship/colony. Link `rebellion.md#rebels` for what a
     rebel is and `rebellion.md#learning-rebel-counts` for the rebellion-side
     view; do not restate rebel mechanics.
   - `## Convert rebels` (`B`): converts the nation's own rebels to loyal
     population; each spy unit converts one unit of rebels. Link
     `rebellion.md#rebels`.
   - `## Uncover foreign spy` (`C`): discovers foreign spy operations on the
     nation's ships and colonies; reports the number of foreign spies and the
     name of the ship or colony they originated from. One spy unit is required
     per ship/colony.

**Acceptance criteria:**

- `content/reference/espionage.md` exists with valid front matter
  (`weight: 130`).
- Intro defines the spy unit via the `SPY` cadre (linked), states the
  one-function-per-turn, locality, persistence, and round-fractions-down rules,
  and links `writing-orders.md` at page level.
- The Spy Functions table is faithful (six rows, codes in backticks).
- Sections A–C present with correct anchors; rebel mechanics are linked, not
  restated.
- No `{% … %}` Markdoc shortcodes; "nation" per the mapping; no "Empyrean
  Challenge".

---

## Task 2 — Functions D–F (suppression math)

**Status:** DONE

**Scope:** add the remaining three function sections.

**Steps:**

1. `## Suppress foreign spy` (`D`): suppresses foreign spy operations by
   assassination. State the math exactly as the source gives it:
   - attacking spies destroy foreign spies equal to **3× the attackers' number**;
   - the attackers lose **1/6 of the defenders' number**;
   - worked example: 21 spies attacking 12 foreign spies lose 2 attacking spies
     and destroy 7 foreign spies (illustration, kept austere).

   Fold **footnote 2** in: these quantities vary by up to **±50%** for the
   element of chance — place it as prose or a `{{< callout type="info" >}}`
   adjacent to the math. Present the rule and the worked example **as the source
   gives them**; do **not** try to reconcile the apparent gap between "3× the
   attackers' number" and the example's outcome — the ±50% variance note is the
   source's own explanation and is sufficient for a reference description.
   Reiterate (or rely on the intro's statement of) the round-fractions-**down**
   rule here, since the 1/6 loss is where it bites; the example's 1/6 of 12 = 2
   is already a whole number, but state the rule so partial results are
   unambiguous.
2. `## Incite rebellion` (`E`): incites rebellion in a **foreign** colony; each
   spy unit converts one loyal population unit into a rebel unit (per turn). Link
   `rebellion.md#when-rebellion-occurs` for what rebellion does; do not restate
   it.
3. `## Obtain secrets` (`F`): obtains all or part of another nation's ship or
   colony report; one line of the report per turn per spy unit.

This chapter defines exactly six spy functions (`A`–`F`); do **not** add a
seventh. The sample turn report in `user-manual/appendices.md` shows an
espionage "Type G" column, but that is from a **later version of the rules** and
is out of scope here — ignore it. Do not write a "Differences from the rule book"
note for it.

**Acceptance criteria:**

- Sections D–F present with correct anchors.
- The suppression math (3× attackers destroyed; 1/6 of defenders lost; the 21-vs-12
  example) and the ±50% variance note are stated faithfully; no attempt to
  reconcile the example with the formula.
- The round-fractions-down rule is present (in the intro and/or beside the
  suppression math).
- Exactly six functions (`A`–`F`) are documented; no seventh type and no
  appendix-derived "Type G" note.
- Reference tone throughout (states rules; no step-by-step "you should"); no
  Markdoc shortcodes; no "Empyrean Challenge".

---

## Task 3 — Wire the page into the site and apply weight

**Status:** DONE

**Scope:** make the page reachable and link the Working-Index lines that now have
a real target. No new body content.

**Steps:**

1. **Working Index** in `content/_index.md`: replace the bare-text lines with
   `relref` links —
   - `12 - ESPIONAGE` → `espionage.md` (page top);
   - `12.1 - Rebel Quantity and Type` → `espionage.md#rebel-quantity-and-type`;
   - `12.2 - Convert Rebels` → `espionage.md#convert-rebels`;
   - `12.3 - Uncover Foreign Spy` → `espionage.md#uncover-foreign-spy`;
   - `12.4 - Suppress Foreign Spy` → `espionage.md#suppress-foreign-spy`;
   - `12.5 - Incite Rebellion` → `espionage.md#incite-rebellion`;
   - `12.6 - Obtain Secrets` → `espionage.md#obtain-secrets`.
2. **Glossary** (`glossary.md`): update / add entries:
   - Update the existing **Spy** (`SPY`) entry to link
     `espionage.md` for the function catalog (it currently links nothing for
     espionage).
   - Add a **Spy unit** entry (or fold into **Spy**) pointing at `espionage.md`.
   - Add an entry for the spy-function catalog (e.g. **Spy functions**) linking
     `espionage.md#spy-functions`; optionally add the function names that readers
     might look up (Incite rebellion, Obtain secrets, Uncover foreign spy,
     Suppress foreign spy) as `See` cross-references to the relevant anchors.
     Keep entries alphabetical and consistent with the existing glossary style.
3. **Reciprocal links** where genuinely helpful: add a `relref` from
   `rebellion.md#learning-rebel-counts` back to `espionage.md` for the full spy
   function catalog. Preserve the host page's existing wording; just add the link.

**Acceptance criteria:**

- `content/_index.md` no longer has bare `ESPIONAGE` / `Rebel Quantity and Type`
  / … text for items 12–12.6; all resolve via `relref`.
- Glossary `Spy` entry links the espionage page; new spy-unit / spy-function
  entries (if added) link correctly and stay alphabetical.
- The reciprocal link from `rebellion.md` resolves and preserves wording.

---

## Task 4 — Build, verify, and consistency pass

**Status:** DONE

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build with **no** `relref` "not found"
   errors and no duplicate-weight warnings.
2. Grep the changed pages for leftover Markdoc shortcodes (`{%`), broken/relative
   Markdown links, and the string "Empyrean Challenge".
3. Confirm sidebar order: `espionage` (130) sits after `combat` (120).
4. Confirm every `relref` in the new page targets an existing file and that each
   anchor (`#population-cadres`, `#population-classes`, `#population-units`,
   `#rebels`, `#learning-rebel-counts`, `#when-rebellion-occurs`, …) resolves,
   and that the Working-Index
   anchors (`#rebel-quantity-and-type`, `#convert-rebels`, `#uncover-foreign-spy`,
   `#suppress-foreign-spy`, `#incite-rebellion`, `#obtain-secrets`,
   `#spy-functions`) match the headings the page actually emits.
5. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed),
   no engine code added, no duplication of rules owned by `rebellion.md` or
   `population.md`.

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- Sidebar shows `espionage` after `combat`.
- The page reads as authoritative reference and defers (via links) to the pages
  in the overlap map for shared rules.

---

## Out of scope

- Converting Control of Planets (section 13) or Communication (section 14) — no
  pages exist yet; do not invent links to them.
- Re-documenting rebellion mechanics (owned by `rebellion.md`) or the `SPY` cadre
  allocation (owned by `population.md`) — link to them.
- Writing the Spy Orders detail (owned by the future `writing-orders.md` build) —
  link at page level only.
- The appendix's espionage "Type G" — it belongs to a later version of the rules;
  ignore it. Document only the six functions (`A`–`F`) this chapter defines.
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/espionage.md` or `user-manual/appendices.md`.
