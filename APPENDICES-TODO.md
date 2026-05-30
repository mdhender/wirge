# APPENDICES-TODO — Convert the manual's "Appendices" to their real homes

Plan for converting `user-manual/appendices.md` (the manual's Appendices) into
published material. Unlike the chapter conversions, the appendices are mostly
lookup tables and one-line definitions, and **most of Appendix A is already
decomposed** into existing reference pages. The central job here is a per-item
**disposition** — already-homed / needs-a-home / host-here — and only then a
decision about whether a standalone `content/reference/appendices.md` page is
warranted at all.

**Headline decision (resolved below): do _not_ create a standalone
`appendices.md` page.** Every appendix item already lives on a topic page or is
homed onto one (`mass.md`, `units.md`, `exploration.md`, the glossary) or into a
how-to guide. Scattering each item to the page whose machinery it describes is
the Diátaxis-correct outcome ("respect the structure of the machinery" —
`references/reference.rst`); a grab-bag appendix page would mix unrelated topics.

This plan is split into small, independently reviewable tasks. Tasks 1–6 home the
content; task 7 wires the Working Index and cross-links; task 8 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in APPENDICES-TODO.md. Update the task status to
DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Mass + Storage → write the `mass.md` body (A.6, A.7) | TODO |
| 2 — Quantities represented → add a section to `units.md` (B.1) | TODO |
| 3 — Approximation → add to `exploration.md` (A.1) | TODO |
| 4 — Definition-only items → glossary (A.2 Fractions, A.5 Hyper Space; verify A.3/A.4) | TODO |
| 5 — Sample Orders File → `how-to/writing-orders.md` (C.1) | TODO |
| 6 — Sample Turn Report → new `how-to/read-a-turn-report.md` (C.2) | TODO |
| 7 — Wire the Working Index (Appendix A/B/C) + cross-links | TODO |
| 8 — Build, verify, and consistency pass | TODO |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing. Reference
pages must **describe and only describe** (austere, factual, no instruction or
"why"), per `references/reference.rst`. The two sample documents (Appendix C) are
**illustrative, not austere reference** — they go in `how-to/`, not on a reference
page (justified per item below).

---

## Goal

Find the correct home for every appendix entry and wire the Working Index lines
(Appendix A/B/C) to those homes. Add authoritative reference data that is not yet
captured (the mass-unit definition, the storage definition, the items-per-unit
quantities, and the log-base-10 approximation table). Convert the two sample
documents into annotated how-to material. **Re-host nothing that an existing page
already owns** — cross-link instead.

## Source material

`user-manual/appendices.md` is the source. Read it in full first. It has four
manual-numbered appendices:

- **Appendix I — definitions:** Approximation, Fractions, Groups, Habitability
  Number, Hyper Space, Mass, Storage.
- **Appendix II — Quantities Represented by Units:** an "items per unit" table.
- **Appendix III — Examples:** farm group, factory group, and a missile/shortage
  timeline (informal, engine-internal WIP narrative).
- **Appendix IV — Sample Documents:** a sample Orders File and a sample Turn
  Report.

Do **not** edit the source — `user-manual/` is sacred (see `CLAUDE.md`); resolve
any unclear or contradictory wording in our docs, never in the manual.

**The published Working Index already re-letters and prunes these:**

| Working Index | Manual source | Items |
| ------------- | ------------- | ----- |
| Appendix A | Appendix I | A.1 Approximation … A.7 Storage |
| Appendix B | Appendix II | B.1 Quantities Represented by Units |
| Appendix C: Sample Documents | Appendix IV | C.1 Orders File, C.2 Turn Report |
| _(omitted)_ | **Appendix III (Examples)** | — not in the Working Index — |

So the manual's **Appendix III has no Working Index line and gets none** — its
worked examples are already covered by the converted topic pages (see the
disposition table). Do not reintroduce it.

Working notes (not published, supplementary only): `notes/unit-codes.md`,
`notes/quick-glossary.md`, `notes/orders.md`,
`notes/manufacturing-process-with-shortages.md`. Use for cross-checking codes and
order grammar; keep engine-internal pipeline detail out of published pages (same
rule as `MANUFACTURING-TODO.md`).

---

## Per-item disposition (the central deliverable)

Verify each disposition against the source and the named page before acting.

| Appendix item | Source | Disposition | Home / link target | Action |
| ------------- | ------ | ----------- | ------------------ | ------ |
| **A.1 Approximation** | I | **host-here** (table is unhosted reference data) | `exploration.md` (new `### Approximation` under Probes → `#approximation`); glossary `Approximation` already exists | Task 3 |
| **A.2 Fractions** | I | **host-here** (one-line convention; no topic-page owner) | `glossary.md` (new term **Fraction / rounding**) | Task 4 |
| **A.3 Groups** | I | **already-homed** | `glossary.md` (**Group**) + `manufacturing.md#factory-groups` + `mining.md` | cross-link only |
| **A.4 Habitability Number** | I | **already-homed** | `habitability.md`; glossary **Habitability number** | cross-link only |
| **A.5 Hyper Space** | I | **already-homed** | `glossary.md` (**Hyper-space**) | cross-link only |
| **A.6 Mass** | I | **host-here** (`mass.md` is a stub) | `mass.md` body | Task 1 |
| **A.7 Storage** | I | **host-here** (`mass.md#storage` is a stub) | `mass.md#storage` body; glossary new **Storage** | Task 1 (+ glossary in Task 4) |
| **B.1 Quantities Represented by Units** | II | **host-here** (orphaned reference data) | `units.md` (new `### Quantities represented` → `#quantities-represented`) | Task 2 |
| **Appendix III — Examples** | III | **drop / already covered** (not in Working Index) | `manufacturing.md`, `farming.md`, `shortages.md` (equivalent worked examples already present) | none (document the omission) |
| **C.1 Orders File** | IV | **host-here** (illustrative → how-to) | `how-to/writing-orders.md` (resolves its existing Appendix-C TODO) | Task 5 |
| **C.2 Turn Report** | IV | **host-here** (illustrative → how-to) | new `how-to/read-a-turn-report.md` | Task 6 |

**Why no standalone `appendices.md`:** after the table above, zero items are
left without a home. A.6/A.7 already point into `mass.md` from the Working Index —
the established precedent is decomposition, not an appendix bucket. A reference
page must mirror the machinery it describes; "Approximation" belongs with the
reporting chapter, "Quantities" with the unit catalog, definitions with the
glossary. Keeping them together would violate `references/reference.rst`
("respect the structure of the machinery").

**Why Appendix III is dropped, not re-hosted:** the farm-group and factory-group
examples and the missile/shortage timeline duplicate material now in
`manufacturing.md#factory-units-required`, `farming.md`, and the worked WIP tables
in `shortages.md#work-in-process-and-timing` — and they read as informal
explanation full of engine-internal WIP narrative (the same q1/q2/q3 detail
`MANUFACTURING-TODO.md` deliberately excluded). The Working Index already omits
them. Per the skill, reference must not host worked "explanation"; the converted
pages already carry cleaner illustrations. No relocation is needed; if Task 8
finds a genuinely unique fact in Appendix III not covered elsewhere, fold that one
fact into the owning page rather than reviving the example.

**Why the sample documents are how-to, not reference:** an annotated sample is
application-oriented and action-led — a nation consults it while interpreting an
actual report or drafting an actual order file. That is how-to ("if you want X, do
Y"), not austere reference (`references/reference.rst`: reference "should not
attempt to show how to perform tasks … link to how-to guides"). They must stay
**annotation around a sample**, linking the reference pages that own each rule —
never restating the rules.

---

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| Habitability number, surface limits (HN × 100,000 / × 10,000,000) | `habitability.md` |
| Groups (factories all build one unit; mines all work one deposit) | `manufacturing.md#factory-groups`; `mining.md`; glossary **Group** |
| Hyper space | glossary **Hyper-space**; `ship-systems.md#hyperdrives` |
| Build / "cost" chart, 20 × TL throughput, factory-units-required | `manufacturing.md#build-costs`, `#factory-units-required` |
| Shortage timing, WIP, delivery slip (Appendix III missile example) | `shortages.md#work-in-process-and-timing`; `explanation/production-cycle.md` |
| Farm group output, quarter delivery (Appendix III farm example) | `farming.md`; `shortages.md` |
| Assembly / dis-assembly / operational units / storage | `manufacturing.md#assembling`, `#dis-assembling`; glossary **Operational unit**, **Storage** |
| Order formats exercised by the sample Orders File | `reference/writing-orders.md` (per-order anchors); `how-to/writing-orders.md` |
| Report sections (mining, manufacturing, census, survey, espionage, combat, trade) | `mining.md`, `manufacturing.md`, `population.md`, `exploration.md#surveys`, `espionage.md`, `combat.md`, `trade.md` |

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). The sample
documents use old rule-book codes and spelled-out names; translate every one (see
`units.md` "Differences from the rule book"):

| Source term / report token | Use in our pages |
| -------------------------- | ---------------- |
| "player", "Player #" | **nation** |
| Anti-missile | `ANM` |
| Assault Craft | `ASC` |
| Assault Weapons | `ASW` |
| Automation | `AUT` |
| Consumer Goods | `CNGD` |
| Energy Shield | `ESH` |
| Energy Weapon / "energy weapons-4" | `EWP` / `EWP-4` |
| Factory / `FCT-1` | `FACT` / `FACT-1` |
| Farm / `FRM-1` / `FAM-1` (source typo) | `FARM` / `FARM-1` |
| Hyper Engines / "hyper engines-1" | `HDRV` / `HDRV-1` |
| Life Support / "Life Supports-1" | `LSP` / `LSP-1` |
| **Light Structural** | `STU-2` (do **not** print "Light structural") |
| Military Robots | `MRBT` |
| Military Supplies / `MTSP` | `MTSP` |
| Mine / `MIN-1` | `MINE` / `MINE-1` |
| Missile | `MSS` |
| Missile Launcher / "missile launchers-1" | `MSL` / `MSL-1` |
| Research / `RSCH` | `RSCH` |
| Sensor / `SEN-1` | `SEN` / `SEN-1` |
| Space Drive / "space drive-3" | `SDRV` / `SDRV-3` |
| Structural / `STUN` | `STU-1` |
| Transport / `TPT-1` | `TPT` |
| "soldier" (draft) | `SLD` |
| "trainee units" (draft) | `TRN` |
| census `UEM/USK/PRO/SLD/CNW` | same codes |

The structural rows of Appendix II are governed by the recorded
structural-units/TL decision: the manual's "Light Structural" is `STU-2` and
"Structural" is `STU-1`; **do not reintroduce "Light structural"** (see
`units.md` "Differences from the rule book" and the structural TODO in
`manufacturing.md`). Under the current model both `STU-1` and `STU-2` "house 1
mass unit"; coordinate with the planned STU-2 change noted in `manufacturing.md`
(do not pre-apply it).

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only.
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Storage]({{< relref "mass.md#storage" >}})`; from `how-to/` use
  `../reference/...` (see `how-to/writing-orders.md` for the pattern).
- **Markdoc shortcodes:** the source uses none (plain tables and fenced
  `text` blocks), but the rule still holds — no `{% … %}` Markdoc may survive in
  any converted output; fold any stray footnote-style aside into prose or a
  `{{< callout >}}`.
- **Callouts:** `{{< callout type="info" >}}` for clarifications;
  `{{< callout type="warning" >}}` for `TODO`s about material whose owning
  reference page does not yet exist.
- **Codes** in backticks (`MU`, `STU-1`, `FACT`, …).
- **No duplication:** state genuinely new data points authoritatively at their
  home; link out for everything in the overlap map. Sample documents annotate and
  link — they never restate a rule.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation". (The string does not appear in the source appendices, but
  it does appear in `user-manual/toc.json` — never copy it into authored content.)

## Page weight and ordering (resolved)

**No new standalone reference page, so no new reference weight is introduced.**
Homed material keeps its host page's existing weight: `units.md` 50,
`exploration.md` (its existing weight), `glossary.md` 185, `mass.md` 190. For
reference, the published weights run `writing-orders.md` **180**, `glossary.md`
**185**, `mass.md` **190**; *were* a standalone appendices page kept (it is not),
it would slot at **182**, between Writing Orders and the glossary. State this
explicitly in review so the "after Writing Orders" expectation is satisfied
without a grab-bag page.

The one **new** page is the how-to `read-a-turn-report.md`. The how-to section
currently holds `writing-orders.md` at weight **10**; assign the new guide
**weight 20** (it reads as the companion that follows writing orders). This is a
judgment call — reorder if the section gains a natural "read your report first"
framing.

## Link targets — existing vs. pending

**Existing (link directly):** `mass.md` (`#storage`), `units.md`,
`exploration.md` (`#probes`), `habitability.md`, `glossary.md`,
`manufacturing.md` (`#factory-groups`, `#assembling`, `#dis-assembling`),
`mining.md`, `ship-systems.md` (`#structural-units`, `#sensors`, `#hyperdrives`),
`shortages.md`, `farming.md`, `espionage.md`, `combat.md`, `trade.md`,
`population.md`, `reference/writing-orders.md`, `how-to/writing-orders.md`.

**New anchors this plan creates:** `units.md#quantities-represented` (Task 2),
`exploration.md#approximation` (Task 3), `how-to/read-a-turn-report.md` (Task 6),
new glossary terms **Fraction / rounding** and **Storage** (Task 4).

**Pending / uncertain (flag, do not invent):** some sample-turn-report sections
have no dedicated reference owner yet (the exact **census grid**, the **internal
espionage report** layout, the **survey report** grid). Where an owning page or
anchor does not exist, annotate with a `{{< callout type="warning" >}}` TODO
rather than linking a guessed anchor. Note for the record (out of scope) that the
Working Index line **3.6 Initial Turn Sheet** points at
`game-setup.md#initial-turn-report`, an anchor that does not currently exist —
leave it for a separate fix.

---

## Task 1 — Mass + Storage → write the `mass.md` body (A.6, A.7)

**Status:** TODO

**Scope:** replace the stub body of `content/reference/mass.md` with the Mass-unit
definition and the Storage section. Keep `weight: 190`.

**Steps:**

1. Keep/adjust the existing intro sentence (mass measures how much a unit or
   resource counts against structural and carrying capacity). Add the **mass-unit
   definition** from A.6: one **mass unit** (`MU`) is set at 17,000 pounds —
   roughly the weight of 100 people. Link `MU` is the standard measure of mass and
   of resource quantity (mirror the glossary **Mass unit** entry; do not duplicate
   formulas owned by `ship-systems.md` / `colonies-and-ships.md`).
2. Replace the **`## Storage`** stub (remove its TODO callout) with the A.7
   definition: certain units must be **assembled** to be operational and
   **dis-assembled** to be transferred; while not operational they are said to be
   **in storage**. Cross-link
   [Assembling]({{< relref "manufacturing.md#assembling" >}}),
   [Dis-assembling]({{< relref "manufacturing.md#dis-assembling" >}}), and the
   glossary **Operational unit**. Do **not** restate the operational-unit list or
   the 1-`CNW`-per-500-`MU` rule (owned by `manufacturing.md#assembling`).

**Acceptance criteria:**

- `mass.md` has no TODO callout; the 17,000-pound mass-unit figure is stated.
- `## Storage` defines assembled/operational vs. in-storage and links out for the
  assembly mechanics (no duplication).
- Reference tone (describe only); `weight: 190` unchanged.

---

## Task 2 — Quantities represented → add a section to `units.md` (B.1)

**Status:** TODO

**Scope:** add a `## Quantities represented` section (anchor
`#quantities-represented`) to `content/reference/units.md` carrying Appendix II's
"items per unit" table, translated to engine codes.

**Steps:**

1. Convert the Appendix II table to a Hugo table keyed by engine code. Preserve
   each "number of items per unit" value, mapping names to codes:
   `ANM` 1, `ASC` 1, `ASW` enough to arm 1 `SLD` unit, `AUT` enough to replace 1
   `USK` unit × its TL, `CNGD` indeterminate, `ESH` 1, `EWP` 1, `FACT` 1, `FARM`
   1, `HDRV` 1, `LSP` 1, `STU-2` houses 1 `MU`, `MRBT` 100 robots, `MTSP` enough
   for 1 `SLD` unit per combat round, `MINE` 1, `MSS` 1, `MSL` 1, `SEN` 1, `SDRV`
   1, `STU-1` houses 1 `MU`, `TPT` 1. Add the source's closing fact: each natural
   resource unit is 1 `MU` of that resource.
2. Render the manual's "Light Structural" row as **`STU-2`** and "Structural" as
   **`STU-1`** (per the code mapping); do not print "Light structural". Both house
   1 `MU` under the current model.
3. Add a `{{< callout type="info" >}}` noting the structural quantities follow the
   current one-`MU`-per-`STU` model and will change with the planned STU-2 revision
   tracked in [Manufacturing]({{< relref "manufacturing.md#build-costs" >}}); do
   not pre-apply that change here.

**Acceptance criteria:**

- `units.md` has a `## Quantities represented` section with the full table in
  engine codes; the natural-resource "1 `MU`" line is present.
- No "Light structural" string; `STU-1`/`STU-2` rows correct and cross-linked to
  the structural TODO.
- Reference tone; no formula duplication from `manufacturing.md`/`ship-systems.md`.

---

## Task 3 — Approximation → add to `exploration.md` (A.1)

**Status:** TODO

**Scope:** host the log-base-10 approximation table on
`content/reference/exploration.md` as a subsection of Probes (anchor
`#approximation`).

**Steps:**

1. Under `## Probes`, add `### Approximation`: probe and sensor reports give
   certain values not exactly but as the **log base 10** of the actual number.
   Convert the source table to a Hugo table:

   | Actual mass / quantity | Reported approximation |
   | ---------------------- | ---------------------- |
   | 0 – 9                  | 0                      |
   | 10 – 99                | 1                      |
   | 100 – 999              | 2                      |
   | 1,000 – 9,999          | 3                      |
   | 10,000 – 99,999        | 4                      |
   | 100,000 – 999,999      | 5                      |
   | 1,000,000 – 9,999,999  | 6                      |

   State the pattern continues for larger magnitudes (each row is one more power
   of ten). Note this is the convention behind the "approximate" quantities a
   probe reports, in contrast to the exact figures a survey gives (the page
   already draws that contrast under Surveys).
2. Confirm the glossary **Approximation** entry already exists (it does) and, if
   helpful, point it at the new `exploration.md#approximation` anchor.

**Acceptance criteria:**

- `exploration.md#approximation` exists with the log-base-10 table and a
  "continues for larger magnitudes" note.
- The text ties approximation to probe/sensor reports and contrasts with survey
  exactness; reference tone, no instruction.

---

## Task 4 — Definition-only items → glossary (A.2, A.5; verify A.3, A.4)

**Status:** TODO

**Scope:** add the two glossary terms that do not yet exist and confirm the
already-homed definitions are present and adequate.

**Steps:**

1. Add **Fraction / rounding** (alphabetical, under **F**): fractions of units are
   resolved by truncation or by rounding up depending on the operation. State this
   as the engine convention; do **not** invent a single global rule — the manual
   says it depends on context, and individual pages state their own rounding.
2. Add **Storage** (under **S**): a unit not currently operational — one that must
   be assembled before it functions — is said to be in storage; link
   [Mass · Storage]({{< relref "mass.md#storage" >}}) and the **Operational unit**
   entry.
3. Verify existing entries cover the rest and adjust only if wrong: **Group**
   (A.3 — general; both factories and mines), **Habitability number** (A.4),
   **Hyper-space** (A.5), **Approximation** (A.1), **Mass unit** (A.6). These
   already exist; do not duplicate.

**Acceptance criteria:**

- Glossary has new **Fraction / rounding** and **Storage** entries, alphabetized,
  with correct links.
- No duplicate or conflicting entries; A.3/A.4/A.5/A.1/A.6 confirmed already
  present.

---

## Task 5 — Sample Orders File → `how-to/writing-orders.md` (C.1)

**Status:** TODO

**Scope:** add the Appendix C Orders File as an annotated full sample in
`content/how-to/writing-orders.md`, and remove that page's existing Appendix-C
TODO callout.

**Steps:**

1. Replace the `{{< callout type="warning" >}}` TODO (currently in the "A complete
   order file" section) with a full annotated sample order file. Translate every
   line of the source Orders File to **current engine codes and order grammar**
   (use the code mapping above and the existing examples on this page and in
   `reference/writing-orders.md` as the style: comma-delimited fields, code-TL like
   `EWP-4`, `MSL-1`, `FACT-6`, `CNGD`, period terminators, slashed zeros). Convert
   "player" framing to "nation". Keep the multi-line **set-up block** form already
   demonstrated on the page.
2. Annotate with `//` comments (the page's established convention) explaining
   representative lines; link the owning order types in
   `reference/writing-orders.md` (e.g. draft, build change, assemble, disassemble,
   transfer, support, invade, raid, bombard, survey, probe, control, market, news,
   name, pay, ration, move, set up). Do **not** restate the order formats — link
   them.
3. If any source line uses an order whose **current grammar is not yet defined**
   in `reference/writing-orders.md`, annotate it with a `{{< callout
   type="warning" >}}` TODO rather than inventing syntax.

**Acceptance criteria:**

- The page's Appendix-C TODO callout is gone; a full, annotated, engine-code order
  file is present and reads as the canonical sample.
- Every code/name translated (no `FCT`/`FRM`/`MIN`/`STUN`/spelled-out names; no
  "player"); orders link their reference anchors without restating formats.
- Any undefined order grammar is flagged with a TODO, not guessed.

---

## Task 6 — Sample Turn Report → new `how-to/read-a-turn-report.md` (C.2)

**Status:** TODO

**Scope:** create a new how-to guide that reproduces an engine-code-translated,
annotated sample turn report and explains how to read it, linking each section to
the reference page that owns its rules.

**Steps:**

1. Create `content/how-to/read-a-turn-report.md`: front matter `title: Read a turn
   report`, `weight: 20`. Short intro framing the goal (interpret the report you
   receive each turn); it does not teach strategy and does not restate rules.
2. Reproduce the source sample report in a fenced `text` block, **translated to
   engine codes** (`FACT`/`FARM`/`MINE`/`STU-*`/etc.; "nation" for "player").
   Walk it section by section — Vital/Other Statistics, Census, Storage
   (operational vs. in storage), Mines, Factory groups (orders + WIP quarters),
   Espionage, Survey — with prose that explains what each section reports and
   **links the owning reference page** for the underlying rule:
   [Population]({{< relref "../reference/population.md" >}}),
   [Mining]({{< relref "../reference/mining.md" >}}),
   [Manufacturing]({{< relref "../reference/manufacturing.md" >}}) /
   [Shortages]({{< relref "../reference/shortages.md#work-in-process-and-timing" >}}),
   [Mass · Storage]({{< relref "../reference/mass.md#storage" >}}),
   [Espionage]({{< relref "../reference/espionage.md" >}}),
   [Surveys]({{< relref "../reference/exploration.md#surveys" >}}),
   [Approximation]({{< relref "../reference/exploration.md#approximation" >}}).
3. For report sections whose field layout has **no reference owner yet** (the
   exact census grid, the internal-espionage report grid, the survey-report grid),
   describe them at a high level and add a `{{< callout type="warning" >}}` TODO
   noting the owning reference page is pending — do not invent anchors.
4. Keep it annotation-around-a-sample: explain *what a field means and where the
   rule lives*, never re-derive the rule here.

**Acceptance criteria:**

- `how-to/read-a-turn-report.md` exists (`weight: 20`), reproduces the translated
  sample, and annotates each section with a link to its owning reference page.
- No old codes, no "player"; no rule restated (links only).
- Undocumented report sections carry TODO callouts rather than guessed links.

---

## Task 7 — Wire the Working Index (Appendix A/B/C) + cross-links

**Status:** TODO

**Scope:** point every Appendix A/B/C line in `content/_index.md` at its real home;
confirm Appendix III stays omitted; add reciprocal links. No new body content.

**Steps:**

1. **Working Index** in `content/_index.md` — replace the bare-text appendix lines
   with `relref` links:
   - `A.1 - APPROXIMATION` → `exploration.md#approximation`
   - `A.2 - FRACTIONS` → `glossary.md` (definition-only; page-level, since glossary
     terms have no per-term anchor)
   - `A.3 - GROUPS` → `glossary.md` (term **Group**; page-level)
   - `A.4 - HABITABILITY NUMBER` → `habitability.md`
   - `A.5 - HYPER SPACE` → `glossary.md` (term **Hyper-space**; page-level)
   - `A.6 - MASS` → `mass.md` (already linked — leave)
   - `A.7 - STORAGE` → `mass.md#storage` (already linked — leave)
   - `B.1 - QUANTITIES REPRESENTED BY UNITS` → `units.md#quantities-represented`
   - `C.1 - Orders File` → `how-to/writing-orders.md` (the annotated sample
     section)
   - `C.2 - Turn Report` → `how-to/read-a-turn-report.md`

   Keep the `Appendix A` / `Appendix B` / `Appendix C: Sample Documents` header
   lines as plain text. **Do not add an Appendix III / Examples line** — the index
   deliberately omits it.
2. **Reciprocal links** where genuinely helpful (preserve existing wording, just
   add `relref`): `mass.md` may link `manufacturing.md#assembling`;
   `units.md#quantities-represented` may link `manufacturing.md#build-costs` and
   `ship-systems.md#structural-units`; the new turn-report guide and the order-file
   guide may link each other; `how-to/writing-orders.md` should now link the
   reference order pages it annotates.
3. Confirm the glossary changes from Task 4 are in place and that
   `glossary.md` cross-links resolve.

**Acceptance criteria:**

- No bare-text appendix lines remain in `content/_index.md`; A.1–C.2 all resolve
  via `relref` (A.6/A.7 unchanged).
- No Appendix III line is introduced.
- Reciprocal links resolve and preserve host wording.

---

## Task 8 — Build, verify, and consistency pass

**Status:** TODO

**Scope:** confirm everything builds, links resolve, modes are correct, and
nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build — no `relref` "not found" errors, no
   duplicate-weight warnings.
2. Grep changed/new files for: leftover `{%` Markdoc shortcodes; old rule-book
   codes that should have been translated (`FCT`, `FRM`, `FAM`, `MIN`, `STUN`,
   "Light structural", "hyper engine", spelled-out unit names in samples); the
   literal "player" where "nation" is meant; and the string "Empyrean Challenge".
3. Confirm every new anchor resolves: `units.md#quantities-represented`,
   `exploration.md#approximation`, the new glossary terms, and the
   `mass.md#storage` body.
4. Confirm Diátaxis modes: `mass.md`, `units.md`, `exploration.md` additions are
   austere **reference** (describe only); the two sample documents are **how-to**
   (annotation around a sample, linking reference for rules — not restating them).
5. Confirm Appendix III was **not** reintroduced anywhere, and that no standalone
   `content/reference/appendices.md` was created. Confirm sidebar order is sane
   (no new reference weight introduced; `read-a-turn-report.md` sits at how-to
   weight 20 after `writing-orders.md` at 10).
6. Re-read against `CLAUDE.md` and the skill: no engine code added, no rule
   duplicated from a page in the overlap map, manual untouched.

**Acceptance criteria:**

- `hugo --gc` builds with no errors or broken-`relref` warnings.
- No `{%`, no untranslated codes, no "player"/"Empyrean Challenge" in any
  changed/new file.
- Reference additions read as reference; sample documents read as how-to; Appendix
  III absent; no standalone appendices page.

---

## Out of scope

- A standalone `content/reference/appendices.md` page (decided against; every item
  is decomposed to its machinery's home).
- Re-converting tables already owned by existing pages — `habitability.md`
  (HN/limits), `manufacturing.md` (cost chart, throughput), `shortages.md` (WIP
  timelines), `farming.md` (output) — link only.
- The manual's **Appendix III (Examples)** — already covered by the topic pages
  and omitted from the Working Index; not re-hosted (no engine-internal WIP
  narrative imported, per `MANUFACTURING-TODO.md`).
- Fixing the pre-existing Working Index anchor `game-setup.md#initial-turn-report`
  (3.6) — noted, but a separate change.
- Building out full reference pages for report sections that lack one (census grid,
  internal-espionage grid, survey grid) — flagged with TODO callouts, deferred.
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/appendices.md` (sacred).
