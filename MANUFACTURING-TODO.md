# MANUFACTURING-TODO — Convert "Manufacturing" to a reference page

Plan for converting `user-manual/manufacturing.md` (the manual's chapter 6) into
a published Diátaxis **reference** page at
`content/reference/manufacturing.md`.

This plan is split into five small, independently reviewable tasks. Tasks 1–3
write the page content; task 4 wires it into the site; task 5 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in MANUFACTURING-TODO.md. Update the task status
to DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; Factory Groups + Labor | DONE |
| 2 — Build costs + factory-units-required | DONE |
| 3 — Retooling, Assembling, Dis-assembling | DONE |
| 4 — Wire the page into the site and apply weight | DONE |
| 5 — Build, verify, and consistency pass | DONE |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`.

---

## Goal

Produce one authoritative reference page describing colony manufacturing: factory
groups, the labor they consume, the materials each unit costs, how many factory
units a build needs, and the retool / assemble / dis-assemble operations. The
page must match the house style of the existing reference pages and must **not**
duplicate rules that already live elsewhere — it links to them instead.

## Source material

`user-manual/manufacturing.md` is the source (Factory Groups, Labor + labor
chart, Shortages, "Cost" Chart, No. of Factory Units Required, Retooling,
Assembling, Dis-assembling, and four footnotes). Read it in full first. Do
**not** edit the source — `user-manual/` is sacred (see `CLAUDE.md`); fix unclear
rules in our docs, not the manual.

`notes/manufacturing.md` is **supplementary working prep** (not published). It
restates the manual and adds engine-internal pipeline detail (q1/q2/q3 WIP
columns, volume units, Cargo, fractional remainders). **Keep that engine-internal
pipeline narrative OUT of the reference page** — the conceptual cycle already
lives in the `production-cycle.md` explanation and the timing/WIP tables in
`shortages.md`. The reference page states the manual's rules and links to those
two pages for the mechanism.

The source carries several genuinely **new** authoritative data points not yet in
the converted docs:

1. **Factory Group Labor Chart** — `PRO` and `USK` units required per factory
   unit, by group size (larger groups are more efficient).
2. **Build cost chart** — metallic (`METS`) and non-metallic (`NMTS`) units
   required per output unit, by unit type.
3. **Factory throughput** — each factory unit converts `20 × TL` mass units of
   natural resources per year, which sets how many factory units a build needs.
4. **Assembly rule** — one construction worker (`CNW`) per 500 mass units of an
   operational unit; the list of "operational" units; assembly also adds `FACT`
   to factory groups and `MINE` to mine groups.
5. **Dis-assembly rule** — reverses assembly with a 10% loss (except `SPY` and
   `CNW`); same construction-worker count as assembly.

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| Shortages (manual 6.3) — how scarce inputs are resolved | `shortages.md` (reference) |
| WIP, 4-turn year, delivery schedule, shortage timing | `explanation/production-cycle.md`; `shortages.md#work-in-process-and-timing` |
| Factory units (`FACT`); `METS` / `NMTS` as factory inputs | `units.md` production chart; `mining.md` |
| `PRO` / `USK` population classes; `AUT` replacing `USK` | `population.md#population-classes`; `ship-systems.md#automation` |
| Construction worker (`CNW`) cadre = 1 `PRO` + 1 `USK` | `population.md#population-cadres`; `glossary.md` |
| Build change / assembly / dis-assembly / set up orders | `writing-orders.md` (stub — already exists) |
| Units in storage; "operational" vs stored | `mass.md#storage`; `units.md` |
| `STU-1` / `STU-2` (regular vs light structural) | `ship-systems.md#structural-units`; `colonies-and-ships.md` |

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Map the
manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| Factory unit (FU) | factory unit (`FACT`) |
| Factory group | factory group |
| Professional units | `PRO` |
| Unskilled units | `USK` |
| Automation units | `AUT` |
| Construction units | construction workers (`CNW`) |
| Metallic units | metallic resources (`METS`) |
| Non-metallic units | non-metallic resources (`NMTS`) |
| Build change order | build change order (link `writing-orders.md`) |
| Light Structural | `STU-2`; "Structural" | `STU-1` |
| "player" | **nation** |

Map every unit name in the cost chart to its engine code: Assault Weapon `ASW`,
Assault Craft `ASC`, Anti-missile `ANM`, Automation `AUT`, Consumer Good `CNGD`,
Energy Shield `ESH`, Energy Weapon `EWP`, Factory `FACT`, Farm `FARM`, Hyper
Engine `HDRV`, Life Support `LSP`, Light Structural `STU-2`, Military Robot
`MRBT`, Military Supplies `MTSP`, Mine `MINE`, Missile `MSS`, Missile Launcher
`MSL`, Sensor `SEN`, Space Drive `SDRV`, Structural `STU-1`, Transport `TPT`.

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Manufacturing`.
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Shortages]({{< relref "shortages.md" >}})`.
- **Footnotes:** the source uses Markdoc `{% footnote %}` / `{% fnref %}`
  shortcodes, which do **not** render in Hugo/Hextra. Fold each footnote into the
  prose, a table cell, or a `{{< callout type="info" >}}` block. No Markdoc
  shortcodes may survive in the output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications,
  `{{< callout type="warning" >}}` for `TODO`s about unconverted material.
- **Codes** in backticks (`FACT`, `METS`, `CNW`, …).
- **No duplication:** state the new data points authoritatively here; link out
  for everything in the overlap map. In particular, do **not** re-explain the
  shortage/WIP mechanics — link `shortages.md` and `production-cycle.md`.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Page weight and ordering (resolved)

Weights equal the section's position in `user-manual/toc.json` × 10. Manufacturing
is **item 7** in the toc (Forward 1, Introduction 2, History 3, Game Set Up 4,
Basic Units 5, Colonies and Ships 6, **Manufacturing 7**), so its weight is
**70**.

No collision and no re-weighting of other pages is required: 70 is free between
`colonies-and-ships.md` (60) and `shortages.md` (75). `shortages.md` is the
manual's 6.3 sub-section and correctly sorts just after Manufacturing.

## Link targets — all already exist

Unlike the Colonies and Ships conversion, this one needs **no new stub pages**.
`writing-orders.md` (build change / assembly / dis-assembly / set up orders),
`shortages.md`, `production-cycle.md`, `units.md`, `population.md`,
`ship-systems.md`, `mining.md`, `farming.md`, and `glossary.md` all already
exist. Link at the appropriate anchor; link `writing-orders.md` at **page level**
(its order-type anchors don't exist yet). A `technological-advancement.md` stub
(weight 80) is **out of scope** — TL is already explained in `units.md` and this
conversion does not need a tech-advancement page.

---

## Task 1 — Create the page; Factory Groups + Labor

**Status:** DONE

**Scope:** create `content/reference/manufacturing.md` with front matter, a short
intro, a `## Factory groups` section, and a `## Labor` section with the labor
chart.

**Steps:**

1. Front matter: `title: Manufacturing`, `weight: 70`.
2. Intro (1–2 sentences, reference tone): manufacturing is how colonies build
   units; only colonies have factory groups (ships never do). Link `FACT` /
   factory units to `units.md` production chart.
3. `## Factory groups`: a factory group is formed by an assembly order
   (link `writing-orders.md`) and manufactures every unit **except** natural
   resources (`METS`, `NMTS`, `FUEL`, `GOLD`), `FOOD`, and population.
   Manufacturing any unit takes one year (four turns); link the timing/WIP detail
   to [The Production Cycle]({{< relref "../explanation/production-cycle.md" >}})
   and `shortages.md#work-in-process-and-timing` rather than restating it. State
   that a group may mix factory units of different TLs (from `notes/`), kept to a
   factual sentence.
4. `## Labor`: factory groups consume `PRO` and `USK` per factory unit, scaling
   with group size (larger = more efficient). Convert the **Factory Group Labor
   Chart** to a Hugo table:

   | Factory units in group | `PRO` per `FACT` | `USK` per `FACT` |
   | ---------------------- | ---------------- | ---------------- |
   | 1–4 | 6 | 18 |
   | 5–49 | 5 | 15 |
   | 50–499 | 4 | 12 |
   | 500–4,999 | 3 | 9 |
   | 5,000–49,999 | 2 | 6 |
   | 50,000+ | 1 | 3 |

   Fold **footnote 1** ("`USK` may be replaced by automation units") into a note
   below the table, linking `ship-systems.md#automation`. Fold **footnote 2**
   ("FU = factory unit") by simply using `FACT` / "factory unit" in the header.

**Acceptance criteria:**

- `content/reference/manufacturing.md` exists with valid front matter
  (`weight: 70`).
- Factory-group definition is present and links the timing/shortage mechanics out
  (no WIP/pipeline narrative restated here).
- The labor chart is correct and uses codes; the `USK`→`AUT` substitution note is
  present and links automation.
- No `{% … %}` Markdoc shortcodes; "nation" per the mapping.

---

## Task 2 — Build costs + factory-units-required

**Status:** DONE

**Scope:** add the materials cost chart and the factory-throughput rule.

**Steps:**

1. `## Build costs`: convert the manual's "Cost" Chart to a Hugo table of
   metallic (`METS`) and non-metallic (`NMTS`) units required per output unit,
   one row per unit type, using engine codes (see the code mapping above).
   Preserve the formulas exactly (`1 × TL`, `8 + TL`, `0.2`, `999 + TL`, etc.).
   Fold **footnote 3** ("TL shown is that of the basic unit") into a short note.
   Fold **footnote 4** (light structural built only by orbiting colonies; an
   orbiting colony will not build regular structural units) into a note on the
   `STU-2` row, linking `ship-systems.md#structural-units`.
2. `## Factory units required`: each factory unit converts `20 × TL` mass units
   of natural resources per year, so units that cost more than that need more
   than one factory unit per unit built. Include the manual's worked example
   (a `TL-2` `HDRV` costs 90 resource units → 5 `TL-2` `FACT` build one) as an
   illustrative example, kept austere (illustration, not instruction).

**Acceptance criteria:**

- The cost chart lists all unit types with correct `METS`/`NMTS` formulas, using
  engine codes.
- The `20 × TL` throughput rule and the factory-units-required relationship are
  stated, with the worked example.
- Footnotes 3 and 4 are folded in; the `STU-1`/`STU-2` manufacture restriction is
  captured and linked.

---

## Task 3 — Retooling, Assembling, Dis-assembling

**Status:** DONE

**Scope:** add the three order-driven operations.

**Steps:**

1. `## Retooling`: a build change order (link `writing-orders.md`) makes a factory
   group switch the unit it produces. Retooling takes one turn or more; any
   work in process must finish first, and the turn report says when the group is
   ready for the new order.
2. `## Assembling`: assembly orders (link `writing-orders.md`) form `CNW` and
   `SPY` cadres and make **operational** units functional after storage. List the
   operational units (map to codes: `SDRV`, `SEN`, `AUT`, `LSP`, `EWP`, `ESH`,
   `MINE`, `FACT`, `FARM`, `HDRV`, `STU-1`, `STU-2`, `MSL`). State the rule: one
   construction worker (`CNW`) per 500 mass units of an operational unit (link
   `population.md#population-cadres` for the cadre, `mass.md` for mass). Note
   assembly also adds `FACT` to factory groups and `MINE` to mine groups.
3. `## Dis-assembling`: dis-assembly orders reverse assembly, with a 10% loss of
   the units dis-assembled (except `SPY` and `CNW`); the construction-worker
   count is the same as for assembly.

**Acceptance criteria:**

- All three sections present; order types link `writing-orders.md`.
- Operational-unit list uses codes; the 1-`CNW`-per-500-mass rule and the 10%
  dis-assembly loss are stated correctly.
- Reference tone throughout (states rules; no step-by-step "you should").

---

## Task 4 — Wire the page into the site and apply weight

**Status:** DONE

**Scope:** make the page reachable and link the Working Index lines that now have
a real target. No new body content.

**Steps:**

1. **Working Index** in `content/_index.md`: replace the bare-text lines
   `6 - MANUFACTURING`, `6.1 - Factory Groups`, `6.2 - Labor`,
   `6.4 - "Cost" Chart`, `6.5 - No. of Factory Units Required`, `6.6 - Retooling`,
   `6.7 - Assembling`, `6.8 - Dis-assembling` with `relref` links into the new
   page (page top for 6; section anchors for the rest:
   `#factory-groups`, `#labor`, `#build-costs`, `#factory-units-required`,
   `#retooling`, `#assembling`, `#dis-assembling`). Leave `6.3 - Shortages`
   pointing at `shortages.md` (already linked).
2. **Glossary** (`glossary.md`): add alphabetical entries that don't already
   exist — `Factory group`, `Build change order`, `Operational unit`,
   `Dis-assembly` — each linking to the right `manufacturing.md` anchor. The
   `Assembly` entry already exists; update it to also link
   `manufacturing.md#assembling` if helpful. Do not duplicate `Construction
   worker` (already present).
3. **Reciprocal links** where genuinely helpful: `shortages.md` and/or
   `production-cycle.md` may link back to `manufacturing.md` for factory-group
   context; the `units.md` production chart may link to `manufacturing.md` for
   build costs and labor. Keep existing wording; just add the `relref`.

**Acceptance criteria:**

- `content/_index.md` no longer has bare `MANUFACTURING` / `Factory Groups` /
  `Labor` / `"Cost" Chart` / `No. of Factory Units Required` / `Retooling` /
  `Assembling` / `Dis-assembling` text; all resolve via `relref`.
- Glossary has the new entries, each linking correctly.
- Any reciprocal links added resolve and preserve the host page's wording.

---

## Task 5 — Build, verify, and consistency pass

**Status:** DONE

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build with **no** `relref` "not found"
   errors and no duplicate-weight warnings.
2. Grep the changed pages for leftover Markdoc shortcodes (`{%`), broken/relative
   Markdown links, and the string "Empyrean Challenge".
3. Confirm sidebar order: `manufacturing` (70) sits after `colonies-and-ships`
   (60) and before `shortages` (75).
4. Confirm every `relref` in the new page targets an existing file and that each
   anchor (`#automation`, `#structural-units`, `#population-cadres`,
   `#work-in-process-and-timing`, `#storage`, …) resolves.
5. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed),
   no engine code added, no duplication of rules owned by other pages (especially
   the shortage/WIP mechanics).

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- The page reads as authoritative reference and defers (via links) to the pages
  in the overlap map for shared rules.

---

## Out of scope

- Re-converting Shortages (owned by `shortages.md`) or the production cycle
  (owned by `production-cycle.md`) — link to them.
- Importing the engine-internal pipeline narrative from `notes/manufacturing.md`
  (q1/q2/q3 WIP columns, volume units, Cargo, fractional remainders).
- A `technological-advancement.md` stub (this conversion does not need it).
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/manufacturing.md`.
