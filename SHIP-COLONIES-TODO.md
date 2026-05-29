# SHIP-COLONIES-TODO — Convert "Colonies and Ships" to a reference page

Plan for converting `user-manual/colonies-and-ships.md` (the manual's chapter 5)
into a published Diátaxis **reference** page at
`content/reference/colonies-and-ships.md`.

This plan is split into five small, independently reviewable tasks. Task 1 stubs
the unconverted pages this conversion links to; tasks 2–3 write the page content;
task 4 wires it into the site; task 5 builds and verifies. Read the shared
context below before starting any task — it applies to all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session prompt:
"Implement the next task in SHIP-COLONIES-TODO.md. Update the task status to DONE
when complete."

| Task | Status |
| ---- | ------ |
| 1 — Stub the linked-but-unconverted reference pages | DONE |
| 2 — Create the page and convert the comparison chart | TODO |
| 3 — Write the "Establishment" section | TODO |
| 4 — Wire the page into the site and apply weights | TODO |
| 5 — Build, verify, and consistency pass | TODO |

Keep this table in sync with the per-task **Status** lines below.

---

## Goal

Produce one authoritative reference page describing the four entity types (open,
enclosed, and orbiting colonies, and ships) and how a player **establishes** one
with a set up order. The page must match the house style of the existing
reference pages and must not duplicate rules that already live elsewhere — it
links to them instead.

## Source material

`user-manual/colonies-and-ships.md` is short (one comparison chart, an
"Establishment" prose section, and two footnotes). Read it in full first. Do
**not** edit the source — `user-manual/` is sacred (see `CLAUDE.md`); fix
unclear rules in our docs, not the manual.

The source carries two pieces of genuinely **new** authoritative data not yet in
the converted docs:

1. **Structural units needed per unit of mass**, by entity type: open colony 1,
   enclosed colony 5, orbiting colony 10, ship 10.
2. **Where each entity may be located** (surface / asteroid / orbit) and the
   per-planet limit (one of each colony type, any number of ships).

Everything else in the source overlaps with pages already written, so it should
be cross-linked, not restated. Overlap map:

| Source statement | Already covered in |
| ---------------- | ------------------ |
| Life-support required by enclosed/orbiting colonies and ships | `ship-systems.md#life-support`, `units.md` Entities table |
| Entity definitions (open/enclosed/orbiting colony, ship) | `glossary.md`, `units.md#entities` |
| One open + one enclosed + one orbiting colony + any ships per planet | `planets.md` (line ~36) |
| Structural units as the frame for ships/colonies | `ship-systems.md#structural-units` |
| "Construction units" that build the entity and then return | `glossary.md` Construction worker (`CNW`); `units.md` |

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "empire"/"player's
holdings"). Map the manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| Open Colonies | Open-air colony (`COPN`) |
| Enclosed Colonies | Enclosed colony (`CENC`) |
| Orbiting Colonies | Orbiting colony (`CORB`) |
| Ships | Ship (`SHIP`) |
| Life support unit | Life support (`LSP`) |
| Structural units | Structural units (`STU`) |
| Construction units | Construction workers (`CNW`) — the cadre of 1 `PRO` + 1 `USK` |
| Farm units / food | `FARM` units / `FOOD` |
| Population unit | Population unit (`POP` / a population class) |
| "per player per planet" | per **nation** per planet |

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only (see existing pages). Title:
  `Colonies and Ships`.
- **Cross-links:** use Hugo `relref` shortcodes, e.g.
  `[Life support]({{< relref "ship-systems.md#life-support" >}})`.
- **Footnotes:** the source uses Markdoc `{% footnote %}` / `{% fnref %}`
  shortcodes. These do **not** render in Hugo/Hextra. Fold each footnote into the
  prose or into a `{{< callout type="info" >}}` block, as the other pages do.
  No Markdoc shortcodes may survive in the output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications,
  `{{< callout type="warning" >}}` for `TODO`s about unconverted material (match
  the pattern in `units.md` and `ship-systems.md`).
- **Codes** are written in backticks (`COPN`, `STU`, `CNW`, …).
- **No duplication:** state the two new data points authoritatively here; link
  out for everything in the overlap map rather than restating it.
- **IP/naming:** never brand anything "Empyrean Challenge" in our text; use
  "Epimethean Challenge" / "nation"; attribute as "Michael D Henderson" only
  where attribution appears (not needed in body text).

## Page weight and ordering (resolved)

Weights follow the canonical section order. The published order is given by the
**Working Index in `content/_index.md`**, and existing page weights equal the
section's position in `user-manual/toc.json` × 10 (e.g. Game Set Up 40, Basic
Units 50, Rebellion 110, Victory Conditions 160).

The Working Index lists **Colonies and Ships as section 5** — a top-level
section that sits **after Basic Units and before Manufacturing**. Its canonical
weight is therefore **60** (`toc.json` position 6 × 10).

That collides with two existing pages that have drifted onto section-level
slots even though the Working Index lists them as **Basic Units sub-pages**:

- `mining.md` — Working Index `4.4.3 - Mines` — currently `weight: 60`.
- `food.md` — Working Index `4.5.2 - Consumer Goods and Food` — currently
  `weight: 65`.

Both belong under Basic Units (50-series), before Colonies and Ships. **Resolution
(applied in Task 4):**

| Page | Current weight | New weight |
| ---- | -------------- | ---------- |
| `colonies-and-ships.md` (new) | — | **60** |
| `mining.md` | 60 | **58** |
| `food.md` | 65 | **59** |

This puts both sub-pages back under Basic Units and ahead of Colonies and Ships,
with no collisions. Out of scope: the pre-existing `population.md`/`farming.md`
tie at 55 and finer intra-Basic-Units ordering — leave them unless they block
the build.

## Unconverted link targets — stub them

This conversion needs to link to material from chapters that are not converted
yet. Rather than writing plain-prose dangling references, **stub those reference
pages** in Task 1 (front matter with a TOC-derived weight + a `TODO` callout
body), then link to them normally. Targets:

| Concept needed | Stub page | Title | Weight (toc.json × 10) | Used by |
| -------------- | --------- | ----- | ---------------------- | ------- |
| Set up / transfer / assembly orders | `content/reference/writing-orders.md` | Writing Orders | 180 (Writing Orders = item 18) | Establishment section (Task 3) |
| Mass counted for STU; storage at ½ mass | `content/reference/mass.md` | Mass | 190 (Appendices = item 19) | Footnote 2 (Task 2) |

Notes:
- For stubs, link at **page level** (`{{< relref "writing-orders.md" >}}`),
  not to anchors that don't exist yet.
- `mass.md` filename/scope is the executor's call; the recommendation is a single
  page titled "Mass" that will hold Appendix A.6 (Mass) and A.7 (Storage), with a
  `## Storage` section. (`glossary.md` already at 185 will then sort just before
  `mass.md` at 190 — acceptable; do not re-weight the glossary here.)
- A `manufacturing.md` stub (weight 70) is **not required** for this task and is
  out of scope; this conversion does not link to it.

---

## Task 1 — Stub the linked-but-unconverted reference pages

**Status:** DONE

**Scope:** create minimal stub pages so the links added in Tasks 2–3 resolve and
the site builds clean. No real content from the manual yet.

**Steps:**

1. Create `content/reference/writing-orders.md` with front matter
   `title: Writing Orders`, `weight: 180`, and a body consisting of a
   `{{< callout type="warning" >}}` **TODO** noting the page is a stub for the
   manual's Writing Orders chapter (set up, transfer, assembly, and the other
   order types) and is not yet written.
2. Create `content/reference/mass.md` with front matter `title: Mass`,
   `weight: 190`, a one-line intro, a `## Storage` heading (so footnote 2 has a
   stable anchor target), and a `{{< callout type="warning" >}}` **TODO** noting
   it is a stub for Appendix A.6 (Mass) and A.7 (Storage).

**Acceptance criteria:**

- Both stub files exist with valid front matter and the weights above.
- Each body is a short stub with a `TODO` warning callout; no invented rules.
- `mass.md` contains a `## Storage` heading.
- `hugo` still builds (stubs alone introduce no broken links).

---

## Task 2 — Create the page and convert the comparison chart

**Status:** TODO

**Scope:** create `content/reference/colonies-and-ships.md` with front matter, a
short intro, and the comparison chart converted to a Hugo table using engine
codes. Fold both footnotes in.

**Steps:**

1. Add front matter: `title: Colonies and Ships`, `weight: 60`.
2. Write a 1–2 sentence intro defining colonies and ships as the four **entity**
   types, linking to `units.md#entities` and the glossary entry for
   ship/colony. Keep it information-oriented (reference mode), no tutorial tone.
3. Convert the chart. Recommended shape: one row per attribute, one column per
   entity type, with the column headers using both the name and code
   (e.g. `Open-air (COPN)`). Include these rows from the source:
   - Allowed per nation per planet (1 / 1 / 1 / any number)
   - Located on planet surface (habitable terrestrial / uninhabitable
     terrestrial / — / —)
   - Located on asteroid (— / yes / — / —)
   - Located in orbit (— / — / any planet / any planet)
   - Life support required (no / yes / yes / yes)
   - Structural units per unit of mass (1 / 5 / 10 / 10)
   - Size limitation (none for all)
4. **Footnote 1** ("one open, one enclosed, one orbiting, and any number of
   ships at one planet"): fold into the "Allowed per nation per planet" row as a
   short clarifying sentence below the table or an `info` callout. This page is
   now the authoritative home for that limit (Task 4 points `planets.md` here).
5. **Footnote 2** (units in storage count as ½ their mass; the mass of the
   structural units housing the entity is not counted): render as prose and link
   the mass concept to the `mass.md` stub, e.g.
   `[mass]({{< relref "mass.md" >}})` and storage to
   `[storage]({{< relref "mass.md#storage" >}})`. Keep it accurate to the source;
   the detail lives on the (stubbed) Mass page.

**Acceptance criteria:**

- `content/reference/colonies-and-ships.md` exists with valid front matter
  (`weight: 60`).
- The chart's seven attributes are all present and correct, using engine codes.
- The two new data points (STU-per-mass ratios; location/limit rules) appear
  exactly as in the source.
- Both footnotes are represented; footnote 2 links to `mass.md`; **no** `{% … %}`
  Markdoc shortcodes remain.
- No text brands the game "Empyrean Challenge"; "nation" used per the mapping.

---

## Task 3 — Write the "Establishment" section

**Status:** TODO

**Scope:** convert the source's "Establishment" prose into a `## Establishment`
section describing the set up order and the materials it must carry.

**Steps:**

1. Describe the **set up order**, linking the term to the `writing-orders.md`
   stub (`{{< relref "writing-orders.md" >}}`): it transfers materials (any type
   and amount, including population) from an existing ship/colony **at the same
   location** to the new site. It is used only for establishment and **precludes
   transfer and assembly orders** on that entity. Link "transfer order" and
   "assembly order" to the same stub (page level).
2. List the **required materials**, mapped to codes:
   - Structural units (`STU`) — link `ship-systems.md#structural-units`.
   - Either farm units (`FARM`) **or** enough `FOOD` to feed the population for
     at least one turn — link `farming.md` / `food.md`.
   - At least one population unit. Add the source's caveat: an **unpopulated**
     entity can be taken over by any other nation that installs a population
     unit there. (Connects to control/rebellion; keep it a plain note.)
   - Enough **construction workers** (`CNW`) to assemble the entity — link the
     glossary `CNW` entry and/or `units.md`.
3. State the **partial-assembly rule**: if there are not enough construction
   workers, only the proportional portion of the assembly is done.
4. State the **return rule**: once construction workers finish, they
   automatically return to the ship/colony they came from, unless the set up
   order says otherwise.

**Acceptance criteria:**

- A `## Establishment` section covers: what a set up order is, that it precludes
  transfer/assembly orders, the four required-material categories, the
  partial-assembly rule, and the construction-worker return rule.
- "Construction units" is correctly rendered as construction workers (`CNW`).
- Order-type terms link to `writing-orders.md`; material terms link to their
  existing pages; all links resolve.
- Reference tone throughout (states rules; no step-by-step "you should").

---

## Task 4 — Wire the page into the site and apply weights

**Status:** TODO

**Scope:** make the new page reachable, apply the weight resolution, and link the
Working Index lines that now have real targets. No new body content.

**Steps:**

1. **Apply weights:** set `mining.md` `weight: 58` and `food.md` `weight: 59`
   (see "Page weight and ordering").
2. **Working Index** in `content/_index.md`: replace the three plain-text lines
   `- 5 - COLONIES AND SHIPS`, `- 5.1 - Chart`, `- 5.2 - Establishment` with
   `relref` links into the new page (page top for 5 and 5.1; `#establishment`
   for 5.2).
3. **Working Index — stubbed targets:** now that the stubs exist, link the
   matching lines: `17 - WRITING ORDERS` (and `17.2.2 - Set Up Orders`,
   `17.2.3 - Assembly orders`, `17.2.6 - Transfer Orders` if present) →
   `writing-orders.md`; `A.6 - MASS` and `A.7 - STORAGE` → `mass.md`
   (`#storage` for A.7).
4. **Reciprocal link from `planets.md`:** the one-colony-of-each-type-per-planet
   sentence (~line 36) should link to this page as the authoritative source for
   the per-planet limit. Keep `planets.md`'s wording; just add the `relref`.
5. **Glossary:** add a `Set up order` entry (alphabetical) defining it and
   linking to `colonies-and-ships.md#establishment`. Add an `Establishment`
   entry only if it does not merely duplicate. Add back-links from existing
   entries (Colony, Ship, Entity, …) only where genuinely helpful.

**Acceptance criteria:**

- `mining.md` is `weight: 58`, `food.md` is `weight: 59`.
- `content/_index.md` no longer has bare `COLONIES AND SHIPS` / `Chart` /
  `Establishment` text; all three resolve via `relref`, as do the Writing Orders
  and Mass/Storage lines now backed by stubs.
- `planets.md` links its per-planet-limit sentence to the new page.
- Glossary has a `Set up order` entry that links correctly.

---

## Task 5 — Build, verify, and consistency pass

**Status:** TODO

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo` (or `hugo server`) and confirm a clean build with **no** `relref`
   "not found" errors.
2. Grep the changed pages for leftover Markdoc shortcodes (`{% `), broken/relative
   Markdown links, and the string "Empyrean Challenge".
3. Confirm sidebar order: `mining`(58) and `food`(59) now sit under Basic Units,
   `colonies-and-ships`(60) follows them, and the Writing Orders(180)/Mass(190)
   stubs appear in tail order.
4. Confirm every `relref` in the new page targets an existing file (including the
   `writing-orders.md` and `mass.md` stubs) and that `mass.md#storage` resolves.
5. Re-read against `CLAUDE.md`: Diátaxis reference mode (not mixed), no engine
   code added, no duplication of rules owned by other pages.

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- The page reads as authoritative reference and defers (via links) to the pages
  in the overlap map for shared rules.

---

## Out of scope

- Fully converting Writing Orders or the Mass/Storage appendix — Task 1 only
  **stubs** them.
- A `manufacturing.md` stub (this conversion does not link to it).
- The pre-existing `population.md`/`farming.md` weight tie at 55.
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/colonies-and-ships.md`.
