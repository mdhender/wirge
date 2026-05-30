# WRITING-ORDERS-TODO — Convert "Writing Orders" into a reference page **and** a companion how-to

Plan for converting `user-manual/writing-orders.md` (the manual's section 17) into
**two** published Diátaxis deliverables:

1. a **reference** page — the order catalog — at `content/reference/writing-orders.md`
   (this file already exists as a stub; the work **replaces it in place**), and
2. a companion **how-to** guide — the larger worked examples — at
   `content/how-to/writing-orders.md` (a **new** file).

Writing Orders is a long, list-structured section (General Rules plus ~22 order
categories), so this plan breaks the work into many small numbered tasks —
roughly one per order category — instead of one monolithic task. Read the shared
context below before starting any task; it applies to all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in WRITING-ORDERS-TODO.md. Update the task
status to DONE when complete."

The tasks fall into three groups: **reference tasks** (Tasks 1–14) build the
austere catalog page; **how-to tasks** (Tasks 15–18) build the worked-example
guide; the **wiring and verify tasks** (Tasks 19–20) connect both pages to the
site and confirm a clean build.

| Task | Status |
| ---- | ------ |
| 1 — Replace the stub; front matter, intro, General Rules | DONE |
| 2 — Combat orders | DONE |
| 3 — Set up orders | DONE |
| 4 — Assembly & Dis-assembly orders | DONE |
| 5 — Build change, Transfer, Mining change orders | DONE |
| 6 — Market orders (buy/sell units & TL) | DONE |
| 7 — Survey & Probe orders | DONE |
| 8 — Spy orders | DONE |
| 9 — News release orders | DONE |
| 10 — Jump orders | DONE |
| 11 — Draft, Disband, Pay, Ration orders | DONE |
| 12 — Control & Un-control orders | DONE |
| 13 — Naming orders | DONE |
| 14 — Trade station & Colonization orders | DONE |
| 15 — Create the how-to; front matter, intro, scaffolding | DONE |
| 16 — How-to: the full `set up … end` walkthrough | DONE |
| 17 — How-to: a complete sample order file | TODO |
| 18 — How-to: multi-order sequences in Sequence-of-Play order | TODO |
| 19 — Wire both pages into the site; index, reciprocal links, glossary | TODO |
| 20 — Build, verify, and consistency pass | TODO |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing both
pages. This conversion produces TWO modes, so read **both**
`references/reference.rst` AND `references/how-to-guides.rst`:

- The **reference** page must **describe and only describe** — austere, factual,
  no instruction ("first do X, then Y"), no strategy. Each order shows its
  **format** plus **one** short, minimal example (two at most where genuinely
  distinct variants exist, e.g. buy-units vs buy-TL) with minimal explanation —
  just enough to read the format.
- The **how-to** page is task-oriented: it guides a competent reader through
  assembling a turn's orders, using conditional imperatives and a logical
  sequence. It carries the **larger** examples — the full multi-line
  `set up … end` block in context, a realistic complete order file, and
  multi-order sequences in Sequence-of-Play order. It does **not** teach strategy
  and does **not** restate the per-order format (it links to the reference for
  that).

Rule of thumb for the split: if an example is longer than a couple of lines, or
shows several orders working together, or needs prose to explain **why**, it
belongs in the how-to and the reference links to it.

---

## Goal

Produce two pages that together convert the manual's Writing Orders section:

1. **`content/reference/writing-orders.md`** (`weight: 180`, replacing the
   existing stub) — the authoritative **order catalog**: the General Rules, then
   the per-order **format / grammar, fields, and constraints**, each with one
   minimal example. Austere reference mode throughout.
2. **`content/how-to/writing-orders.md`** (NEW, `weight: 10`) — the companion
   **"How to write a turn's orders"** guide: the full `set up … end` walkthrough,
   a complete sample order file, and multi-order sequences arranged in
   Sequence-of-Play order.

Both pages must match the house style of the existing reference pages, must
**not** duplicate rules that live elsewhere (they link out), and must be wired
reciprocally: the reference links to the how-to for the big examples; the how-to
links back to the reference for the per-order format.

## Source material

`user-manual/writing-orders.md` is the source (General Rules, then a List of
Orders covering ~22 categories). **Read it in full first.** Do **not** edit the
source — `user-manual/` is sacred (see `CLAUDE.md`); resolve unclear or
contradictory rules in our docs, never by changing the manual.

`notes/orders.md` is **supplementary working prep** (not published). It restates
the order set using a **different grammar** from the manual (space-delimited,
verb-first) — see the grammar decision below. Do **not** import that engine
grammar into either published page; both pages use the manual's grammar
(Divergence 1). (`notes/quick-command-index.md` was empty and has been removed.)

The source's order categories, in source order, each becoming a catalog entry:

- **General Rules** — page formatting; the header line (player name, player ID
  No., game No., game-turn No., signature); the slashed-zero convention; no comma
  needed between a quantity and its unit; orders must be written in
  Sequence-of-Play order or they may not execute; orders are addressed to a
  ship/colony ID No. as the first field; orders execute only if the unit has the
  needed items (partial fulfillment); `//` line comments.
- **Combat orders** — bombard, invade, raid (with `material raided`),
  support-attacker, support-defender; the integer percent committed and the
  required `%` sign.
- **Set up orders** — the multi-line `set up … end` block (terminated by `end`).
- **Assembly orders** — factory / mine / other variants.
- **Dis-assembly orders** — same as assembly with `disassemble` replacing
  `assemble`.
- **Build change orders** — start a new product or `retool`.
- **Transfer orders** — one unit type per order (multi-item transfer is a future
  feature).
- **Mining change orders** — reassign a mining group to a new deposit.
- **Market orders** — buy units / buy TL / sell units / sell TL (quantity omitted
  for TL).
- **Survey orders.**
- **Probe orders** — one or more orbits, comma-separated.
- **Spy orders** — check rebels, convert rebels, incite rebels, check for spies,
  attack spies, gather information.
- **News release** — market-planet form and trade-station form; quoted message
  text; optional quoted signature.
- **Jump orders** — in-system move (incl. the 11th-orbit `star-letter-dash`
  form), and system jump.
- **Draft orders.**
- **Disband orders** — present in the source; **missing from the index** (see the
  flag below).
- **Pay orders.**
- **Ration orders** — integer percent with required `%`.
- **Control orders.**
- **Un-control orders** — same as control with `un-control` replacing `control`.
- **Naming orders** — planets, and ships/colonies; 24-character limit; quoted
  names.
- **Trade station orders** — permission granted/denied; the receiving entity is a
  proxy.
- **Colonization orders** — permission to colonize; proxy note; permission cannot
  be revoked.

Verify each against the source — don't trust this summary.

## Overlap map (link, do not restate)

The reference page gives the **order format only**; the mechanic each order drives
already lives on another page. Link at the appropriate anchor; do **not** restate
the rule. Verify each anchor exists in the target file before linking — if an
anchor can't be confirmed, link at page level and/or leave a
`{{< callout type="warning" >}}` TODO rather than inventing a `#`-anchor.

| Order(s) | Mechanic lives in |
| -------- | ----------------- |
| Sequence-of-Play ordering rule (primary overlap) | [Sequence of Turn Execution]({{< relref "sequence-of-turn-execution.md" >}}) — link, do **not** restate the 21-stage list |
| Combat: bombard / invade / raid / support; percent committed | `combat.md` (`#bombardment`, `#attack-orders`, `#percentage-of-commitment`, `#defense-support`) |
| Spy: check/convert/incite/check-for/attack/information | `espionage.md` (`#spy-functions`, `#convert-rebels`, `#incite-rebellion`, …) |
| Control / un-control / colonization permission | `control-of-planets.md` (`#taking-control`, `#relinquishing-planets`) |
| Market buy/sell; trade-station permission | `trade.md` (`#home-planet-markets`, `#trade-stations`) |
| News release / news service | `communication.md` (`#news-service`) |
| Survey / probe / jump (movement) | `exploration.md` (`#surveys`, `#probes`, `#ship-movement`, `#interplanetary-movement`, `#interstellar-movement`) |
| Assemble / disassemble / build change (retool) | `manufacturing.md` (`#assembling`, `#dis-assembling`, `#retooling`) |
| Set up / transfer; ship & colony IDs as the order target | `colonies-and-ships.md` (`#establishment`) |
| Mining change / deposit assignment | `mining.md` (`#yield`) |
| Draft / disband; pay; ration | `population.md` (`#orders`, `#population-changes`); `food.md` (`#rations`, `#starvation`) |
| Unit **codes** used in every example | `units.md` (authoritative code table); `weapons.md`; `ship-systems.md` — link for code definitions; do **not** restate unit stats |

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Two mapping
rules apply to this section in particular.

**1. "player" → "nation," with a boundary.** The manual's General Rules speak of
"the player" — the human who fills out and submits the turn sheet. Map the
**in-game actor** to **nation** (e.g. "a nation's orders"), but keep wording sane
where the rule is genuinely about the **person or the turn-sheet submission**
(signature, player name, player ID No., numbering pages). Flag this boundary in
the General Rules section (see Task 1); do not force "nation" onto a rule that is
really about the physical turn sheet.

**2. Unit names → engine codes in `CODE-TL` form.** The manual spells unit names
out (`space drives-1`, `hyper engines-1`); **our examples use the published
codes** from the authoritative table in
[`content/reference/units.md`](content/reference/units.md) — **not**
`notes/unit-codes.md`, which diverges (it lists `SPD`/`HEN`; `units.md`
deliberately uses `SDRV`/`HDRV` to avoid confusion with `SEN`). This is an
intentional, allowed departure from the manual's wording — the examples are
**ours**; only the `user-manual/` source text is sacred. **Keep the order
keywords and structure faithful; only swap the unit naming.** Codes in backticks.

| Source wording | Use in our examples |
| -------------- | ------------------- |
| `space drives-1` | `SDRV-1` |
| `hyper engines-1` | `HDRV-1` |
| `life supports-1` | `LSP-1` |
| `sensor-1` | `SEN-1` |
| `factories-6` | `FACT-6` |
| `mine-2` | `MINE-2` |
| `missile launchers-1` | `MSL-1` |
| `energy weapons-4` | `EWP-4` |
| `spy units` | `SPY` |
| `structural units` | `STU` (use `STU-1`/`STU-2` only where a TL is given) |
| `professionals` | `PRO` |
| `soldier` (draft/pay type) | `SLD` |
| `trainee` (draft type) | `TRN` |
| `CNW` (already a code) | `CNW` |
| `unskilled` / `professional` (pay type) | `USK` / `PRO` |
| `food`, `fuel`, `gold` | `FOOD`, `FUEL`, `GOLD` |
| `consumer goods` | `CNGD` |

Mirror the manual's TL presence: where the source gives a TL, write `CODE-TL`
(`SDRV-1`); where it omits one (e.g. bare `STU` in a market example), write the
bare code. The draft/pay **type words** ("soldier," "unskilled," "professional")
are a softer boundary like rule 1 above — render them as codes (`SLD`, `USK`,
`PRO`) for house-style consistency, and note this once.

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only.
  - Reference: `title: Writing Orders`, `weight: 180` (keep the existing stub's
    front matter; replace only the body).
  - How-to: `title: Write a turn's orders` (a how-to title says what it shows —
    per `how-to-guides.rst`, prefer an action title over a noun), `weight: 10`.
- **Cross-links:** Hugo `relref` shortcodes. Same-directory links use the bare
  filename (`[Combat]({{< relref "combat.md" >}})` on the reference page);
  cross-directory links from the how-to into reference use the relative path
  (`[Writing Orders]({{< relref "../reference/writing-orders.md" >}})`), and the
  reference into how-to uses `[…]({{< relref "../how-to/writing-orders.md" >}})`.
  Verify the exact relative form against an existing cross-directory link (e.g.
  the `../explanation/production-cycle.md` links already in the reference pages).
- **Callouts:** the source uses Markdoc `{% callout %}` / `{% callout
  type="warning" %}` blocks (Ration, Control, Naming, Trade Station,
  Colonization). These do **not** render in Hugo/Hextra. Fold each into a
  Hugo/Hextra `{{< callout type="info" >}}` / `{{< callout type="warning" >}}`
  shortcode or into prose. **No `{%` may survive in either output file.**
- **Format/example blocks:** render every order's **format** and **example** as a
  fenced ` ```text ` code block (the source already does this; keep it).
- **Codes** in backticks (`SDRV`, `AUT-1`, `FACT-6`, …); no rule duplication.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation."

## Page weight and ordering (resolved)

- **Reference:** `weight: 180`, **replacing the existing stub in place** — do not
  create a new file or change the weight. The reference weights step by ten in
  Working-Index order: Sequence of Turn Execution is 170, so Writing Orders is
  180 (free, no collision, no re-weighting of other pages).
- **How-to:** new file `content/how-to/writing-orders.md` at **`weight: 10`**.
  `content/how-to/` currently holds only `_index.md`, so this is the first how-to
  page and 10 is free. Hugo/Hextra auto-generates the section card for it from its
  front matter — do **not** hand-author a how-to index entry or card list (see
  `[[hextra-auto-cards-no-manual-index]]`).

## Link targets — existing vs. pending

All overlap-map target pages already exist in `content/reference/`
(`sequence-of-turn-execution.md`, `combat.md`, `espionage.md`,
`control-of-planets.md`, `trade.md`, `communication.md`, `exploration.md`,
`manufacturing.md`, `colonies-and-ships.md`, `mining.md`, `population.md`,
`food.md`, `units.md`, `weapons.md`, `ship-systems.md`, `glossary.md`). **No new
stub pages are required.** Confirm each anchor exists before linking; if a
specific anchor can't be confirmed, link at page level and/or leave a
`{{< callout type="warning" >}}` TODO rather than inventing it.

## Divergences / decisions to FLAG explicitly (surface, do not silently resolve)

1. **Grammar — DECIDED: publish the manual's grammar.** The manual's order grammar
   is **comma-delimited and target-first** (`16, build change, 8, EWP-4.`).
   `notes/orders.md` uses a **space-delimited, verb-first** grammar
   (`build change <id> <group> <target>`). **Decision (from the user): both pages
   publish the manual's comma-delimited, target-first grammar.** A *later,
   separate* conversion task may migrate the docs to the engine grammar from
   `notes/orders.md`, but that grammar is **not confirmed complete**, so it is out
   of scope here — do **not** adopt it, mix it in, or reconcile the two now. No
   reader-facing "undecided" warning callout is needed (the grammar is settled for
   this conversion); just use the manual's grammar consistently in every format
   line and example.
2. **Disband missing from the index.** The source has a **Disband orders**
   section, but the `content/_index.md` 17.x sub-tree omits it (it jumps Draft →
   Pay). Cover Disband in the catalog (Task 11) **and** have the wiring task
   (Task 19) **add** the missing entry to the Working Index in source order
   (Disband after Draft), renumbering the following 17.2.x labels to suit.
3. **"player" vs "nation" boundary — DECIDED.** Map the **in-game actor** to
   **nation** (e.g. "a nation's orders"). **But preserve the turn-sheet / print-out
   wording as-is** — the header line names (signature, player name, player ID No.,
   game No., game-turn No., "the number of the last print-out received") describe
   the **generated turn-sheet/report (output)**, not player input, so leave that
   wording intact rather than forcing "nation" onto it. Handle this in Task 1;
   don't blanket-rewrite every "player."

## Reference-page anchor scheme (so the index relrefs resolve)

Use these H2 headings on the reference page (their auto-generated anchors are what
Task 19 links from the Working Index):

`#general-rules`, `#combat-orders`, `#set-up-orders`, `#assembly-orders`,
`#dis-assembly-orders`, `#build-change-orders`, `#transfer-orders`,
`#mining-change-orders`, `#market-orders`, `#survey-orders`, `#probe-orders`,
`#spy-orders`, `#news-release-orders`, `#jump-orders`, `#draft-orders`,
`#disband-orders`, `#pay-orders`, `#ration-orders`, `#control-orders`,
`#un-control-orders`, `#naming-orders`, `#trade-station-orders`,
`#colonization-orders`. Under Naming, two H3s: `#naming-planets`,
`#naming-ships-and-colonies`. Keep heading text and casing stable across tasks so
later wiring matches; if you rename a heading, update Task 19's anchor list.

---

# Reference tasks (Tasks 1–14)

## Task 1 — Replace the stub; front matter, intro, General Rules

**Status:** DONE

**Scope:** replace the stub body of `content/reference/writing-orders.md` (keep
its `title: Writing Orders` / `weight: 180` front matter) with a short intro and a
`## General rules` section. Examples use the **manual's comma-delimited,
target-first grammar** throughout (Divergence 1).

**Steps:**

1. Keep the front matter. Remove the stub TODO callout.
2. Intro (1–2 sentences, reference tone): this page is the catalog of orders a
   nation submits with its turn — each order's format, fields, and constraints,
   with one minimal example apiece. Point to the companion how-to
   ([Write a turn's orders]({{< relref "../how-to/writing-orders.md" >}})) for the
   larger worked examples (the full set-up block, a complete order file, and
   multi-order sequences). The how-to page already exists as a TODO-callout stub
   (created alongside Task 1) so this `relref` resolves; Tasks 15–18 fill it in.
3. `## General rules` — describe, in austere reference tone:
   - the header line each page carries (signature, player name, player ID No.,
     game No., game-turn No.), and that the game-turn No. is the number of the
     last print-out received — **preserve this turn-sheet wording as-is** (it
     names generated turn-sheet/report output, not player input, per Divergence
     3); do not force "nation" onto it;
   - the slashed-zero convention (write zeros slashed to distinguish from `O`);
   - no comma is needed between a quantity and its unit;
   - **orders must be written in Sequence-of-Play order or they may not execute** —
     link [Sequence of Turn Execution]({{< relref "sequence-of-turn-execution.md" >}})
     for the canonical stage order; do **not** restate the 21-stage list. (Keep
     the manual's assemble-before-disassemble illustration to one short line, or
     defer the worked illustration to the how-to.)
   - orders are addressed to a ship or colony; the **ship/colony ID No. is the
     first field** of most orders (link `colonies-and-ships.md` for entity IDs);
   - orders are carried out only if the entity has the needed units (partial
     fulfillment) — one short sentence, no worked example;
   - `//` line comments: `//` and the rest of the line are ignored. Show the
     minimal comment example as a fenced `text` block.

**Acceptance criteria:**

- The stub TODO callout is gone; front matter unchanged (`weight: 180`).
- Intro links the how-to. Examples use the manual's comma-delimited grammar; no
  "undecided-grammar" warning callout is added (the grammar is settled).
- `## General rules` covers the header line, slashed zero, quantity/unit spacing,
  Sequence-of-Play ordering (linked, not restated), ID-first addressing, partial
  fulfillment, and `//` comments. Turn-sheet/print-out wording preserved as-is;
  "nation" used for the in-game actor.
- No `{%` shortcodes; no "Empyrean Challenge".

---

## Task 2 — Combat orders

**Status:** DONE

**Scope:** add `## Combat orders` with the five combat order forms.

**Steps:**

1. One sentence: percent committed is an integer and the `%` sign is required
   (10% barely committed, 100% totally committed). Link
   [Percentage of commitment]({{< relref "combat.md#percentage-of-commitment" >}}).
2. For each of **bombard, invade, raid, support (attacker), support (defender)**:
   a fenced `text` **format** line and **one** minimal `text` example, codes
   swapped where any unit names appear (raid's `material raided` example uses
   `GOLD`). Keep the source's brief NOTEs (raid requires the material; support
   shows the supported entity's ID) as one-line prose, not instruction.
3. Link the combat mechanics out:
   [bombardment]({{< relref "combat.md#bombardment" >}}),
   [attack orders]({{< relref "combat.md#attack-orders" >}}),
   [defense support]({{< relref "combat.md#defense-support" >}}). Do **not**
   restate combat resolution.

**Acceptance criteria:**

- All five combat forms present, each with format + one minimal example.
- The integer-percent / required-`%` rule stated once and linked to combat.
- Mechanics linked, not restated; reference tone (no "to attack, first …").

---

## Task 3 — Set up orders

**Status:** DONE

**Scope:** add `## Set up orders` with the format and **one minimal** example;
the full multi-line walkthrough goes to the how-to (Task 16).

**Steps:**

1. State the format: `set up , type (ship or colony) , establishing ship/colony
   No. , transfer , quantity and item , … , end .` — note `end` terminates the
   block and that the order may span several lines.
2. Show **one short** minimal example (two or three transfer lines, not the full
   manual block), codes swapped (`SDRV-1`, `LSP-1`, `SEN-1`, `STU`, `FOOD`,
   `PRO`, `FUEL`, `HDRV-1`). Keep the `-1` = TL-1 note to one line.
3. Link [Establishment]({{< relref "colonies-and-ships.md#establishment" >}}) for
   what set up does. Add: *"For the full set-up block in context, see
   [Write a turn's orders]({{< relref "../how-to/writing-orders.md" >}})."*

**Acceptance criteria:**

- Format present; example is minimal (a few transfer lines), not the full manual
  block; codes swapped; `end` terminator noted.
- Links to Establishment and forward to the how-to for the full block.

---

## Task 4 — Assembly & Dis-assembly orders

**Status:** DONE

**Scope:** add `## Assembly orders` and `## Dis-assembly orders`.

**Steps:**

1. `## Assembly orders`: the three variants — **factory** (`assemble , qty FACT ,
   product`), **mine** (`assemble , qty MINE , deposit No.`), **other**
   (`assemble , qty units`) — each with format + one minimal example, codes
   swapped (`FACT-6` making `CNGD`; `MINE-2` on a deposit; `MSL-1`). Keep the
   source's NOTE that factories and mines assemble into groups automatically to
   one line. Link [Assembling]({{< relref "manufacturing.md#assembling" >}}).
2. `## Dis-assembly orders`: state that the format and examples match assembly
   with `disassemble` replacing `assemble`; show one minimal example. Link
   [Dis-assembling]({{< relref "manufacturing.md#dis-assembling" >}}) for the 10%
   loss rule — do **not** restate it.

**Acceptance criteria:**

- Three assembly variants present, each format + one minimal example, codes
  swapped; the auto-group NOTE kept to one line.
- Dis-assembly stated as the assemble variant with `disassemble`; mechanic linked,
  not restated.

---

## Task 5 — Build change, Transfer, Mining change orders

**Status:** DONE

**Scope:** add `## Build change orders`, `## Transfer orders`, and
`## Mining change orders`.

**Steps:**

1. `## Build change orders`: format (`No. , build change , factory group No. ,
   item to start building (or retool)`). Show the source's examples folded to one
   or two minimal lines (`16, build change, 8, EWP-4.` and a `retool` line),
   codes swapped. Link [Retooling]({{< relref "manufacturing.md#retooling" >}}).
2. `## Transfer orders`: format (`No. , transfer , quantity and unit , receiving
   ship/colony No.`). One minimal example (`SPY`). Keep the source NOTE that one
   order moves one unit type (multi-item transfer is a future feature) to one
   line. Link [Colonies and Ships]({{< relref "colonies-and-ships.md" >}}).
3. `## Mining change orders`: format (`No. , mining , mining group No. , new
   deposit No.`). One minimal example. Link [Mining]({{< relref "mining.md" >}}).

**Acceptance criteria:**

- Three sections present, each format + one minimal example, codes swapped.
- The single-unit-per-transfer NOTE kept brief; mechanics linked, not restated.

---

## Task 6 — Market orders (buy/sell units & TL)

**Status:** DONE

**Scope:** add `## Market orders` with the four forms; this is the one order with
two genuinely distinct variants on each side (units vs TL), so two examples per
side are allowed.

**Steps:**

1. **Buy units** (`No. , buy , quantity , unit type , price in GOLD each`) and
   **buy TL** (`No. , buy , technology level , price in GOLD each`) — note
   **quantity is omitted for TL**. Examples folded to the minimal distinct set
   (e.g. one `buy , 25,600 , STU , 0.01`, one `buy , TL-6 , 1,000,000`), codes
   swapped (`STU`, `AUT-1`, `SDRV-3`, `TL-6`).
2. **Sell units** and **sell TL**, same shape with `sell`; note quantity omitted
   for TL here too. One minimal example each (`sell , STU , 0.5`; `sell , TL-4 ,
   800,000`).
3. Link [Home planet markets]({{< relref "trade.md#home-planet-markets" >}}). Do
   **not** restate market mechanics or pricing rules.

**Acceptance criteria:**

- Four market forms present; the quantity-omitted-for-TL rule stated for both buy
  and sell; codes swapped; at most two examples per side.
- Market mechanics linked, not restated.

---

## Task 7 — Survey & Probe orders

**Status:** DONE

**Scope:** add `## Survey orders` and `## Probe orders`.

**Steps:**

1. `## Survey orders`: format (`No. , survey`) + one example. Link
   [Surveys]({{< relref "exploration.md#surveys" >}}).
2. `## Probe orders`: format (`No. , probe , orbit No. , …`); note multiple
   comma-separated orbits are allowed in one order. One or two minimal examples
   (single orbit; multiple orbits). Link
   [Probes]({{< relref "exploration.md#probes" >}}).

**Acceptance criteria:**

- Both sections present with format + minimal example(s); the multi-orbit note
  kept brief; mechanics linked, not restated.

---

## Task 8 — Spy orders

**Status:** DONE

**Scope:** add `## Spy orders` with the six spy-function forms.

**Steps:**

1. State the common shape: `No. , quantity of spies , <function> [, defender
   No.]`. Give the six forms — **check rebels**, **convert rebels**, **incite
   rebels** (+ defender), **check for spies**, **attack spies** (+ defender),
   **information** (+ defender) — as format lines, then a compact block of the
   source's minimal examples (codes: `SPY` quantities are integers). Note which
   forms take a defender ID.
2. Link [Espionage]({{< relref "espionage.md#spy-functions" >}}) (and the specific
   function anchors — `#convert-rebels`, `#incite-rebellion`, etc. — only where
   confirmed) for what each function does. Do **not** restate spy mechanics.

**Acceptance criteria:**

- All six spy forms present with formats and a compact example set; defender-ID
  forms noted; mechanics linked, not restated.

---

## Task 9 — News release orders

**Status:** DONE

**Scope:** add `## News release orders` with the market-planet and trade-station
forms.

**Steps:**

1. **Market-planet** form (`news , market planet location , message text [,
   signature]`) and **trade-station** form (`news , trade station colony No. ,
   message text [, signature]`). Note the message text must be in double quotes;
   the signature is optional and, if present, also quoted; odd characters may get
   the order rejected. One minimal example per form.
2. Link [News service]({{< relref "communication.md#news-service" >}}). Do **not**
   restate the news service.

**Acceptance criteria:**

- Both news forms present with format + one minimal example; the quoted-text /
  optional-quoted-signature rule stated; mechanic linked, not restated.

---

## Task 10 — Jump orders

**Status:** DONE

**Scope:** add `## Jump orders` with in-system and system forms.

**Steps:**

1. **In-system** (`No. , move , orbit No.`): note that from the 11th orbit you
   prefix the destination orbit with the target star's sequence letter and a dash
   (`C-4`). Examples `77, move, 6.` and `88, move, C-4.`. Link
   [Interplanetary movement]({{< relref "exploration.md#interplanetary-movement" >}}).
2. **System jump** (`No. , move , destination location`): one example
   (`79, move, 4-6-19.`). Link
   [Interstellar movement]({{< relref "exploration.md#interstellar-movement" >}}).
3. Cross-reference the [eleventh orbit]({{< relref "glossary.md" >}}) glossary
   term only if helpful; do not restate the 11th-orbit rule.

**Acceptance criteria:**

- Both jump forms present with format + example; the 11th-orbit star-letter form
  shown; movement mechanics linked, not restated.

---

## Task 11 — Draft, Disband, Pay, Ration orders

**Status:** DONE

**Scope:** add `## Draft orders`, `## Disband orders`, `## Pay orders`, and
`## Ration orders`.

**Steps:**

1. `## Draft orders`: format (`No. , draft , quantity and type of unit`); examples
   with type words as codes (`SLD`, `TRN`, `CNW`). Link
   [Population orders]({{< relref "population.md#orders" >}}).
2. `## Disband orders`: format (`No. , disband , quantity and type of unit`); one
   minimal example. Link [Population]({{< relref "population.md#population-changes" >}}).
   *(This is the order the index omits — Task 19 adds it to the Working Index.)*
3. `## Pay orders`: format (`No. , pay , wages , type`); examples with type words
   as codes (`USK`, `PRO`, `SLD`). Link [Population]({{< relref "population.md" >}}).
4. `## Ration orders`: format (`No. , ration , ration percentage %`). Fold the
   source's `{% callout %}` into a `{{< callout type="info" >}}`: ration is an
   integer with a required `%`; 50% is half a full ration, 100% a full ration;
   starvation sets in at 25%. Note all population on the entity gets the same
   ration. Link [Rations]({{< relref "food.md#rations" >}}) and
   [Starvation]({{< relref "food.md#starvation" >}}).

**Acceptance criteria:**

- All four sections present with format + minimal example; draft/pay type words
  rendered as codes with a one-line note on that choice.
- The Ration `{% callout %}` is folded into a Hugo callout (no `{%` survives);
  mechanics linked, not restated.

---

## Task 12 — Control & Un-control orders

**Status:** DONE

**Scope:** add `## Control orders` and `## Un-control orders`.

**Steps:**

1. `## Control orders`: format (the source writes `Empire No. , control ,
   location` — map the actor to **nation**; flag if the `Empire No.` wording is
   genuinely a distinct field rather than the acting nation's ID, per
   `[[victory-conditions-empire-race-nation]]`). Fold the source's warning
   `{% callout %}` ("the location must include the orbit number") into a
   `{{< callout type="warning" >}}` or prose. One example
   (`28, control, 2-4-6/9.`). Link
   [Taking control]({{< relref "control-of-planets.md#taking-control" >}}).
2. `## Un-control orders`: state it is the control order with `un-control`
   replacing `control`; one example. Link
   [Relinquishing planets]({{< relref "control-of-planets.md#relinquishing-planets" >}}).

**Acceptance criteria:**

- Both sections present; the orbit-number requirement folded into a Hugo callout
  or prose (no `{%`); the `Empire No.`→nation mapping handled and the boundary
  flagged if non-trivial; mechanics linked, not restated.

---

## Task 13 — Naming orders

**Status:** DONE

**Scope:** add `## Naming orders` with two H3 subsections.

**Steps:**

1. One line: names may be at most 24 characters including blanks; names are
   enclosed in double quotes; odd characters may get the order rejected (fold the
   source's two warning `{% callout %}` blocks into prose or one Hugo callout).
2. `### Naming planets` (`location , name , "name"`) — example
   (`5-12-38/2, name, "Goldball Prime".`).
3. `### Naming ships and colonies` (`No. , name , "name"`) — example
   (`39, name, "Dragonfire".`).

**Acceptance criteria:**

- Both H3s present with format + one example; the 24-char / quoted-name rule
  stated once; no `{%` survives.

---

## Task 14 — Trade station & Colonization orders

**Status:** DONE

**Scope:** add `## Trade station orders` and `## Colonization orders`.

**Steps:**

1. `## Trade station orders`: format (`trade station No. , permission , receiving
   No. , granted | denied`). Fold the source's proxy `{% callout %}` into prose or
   a `{{< callout type="info" >}}`: the receiving entity is a proxy — granting or
   denying permission acts on the **nation** that controls it. Examples
   (`138, permission, 200, granted.` / `162, permission, 100, denied.`). Link
   [Trade stations]({{< relref "trade.md#trade-stations" >}}).
2. `## Colonization orders`: format (`receiving No. , permission to colonize ,
   location`). Fold the two source `{% callout %}` blocks: the location must
   include the orbit number; the receiving entity is a proxy (permission acts on
   the controlling nation); **permission to colonize cannot be revoked once
   granted**. One example. Link
   [Control of planets]({{< relref "control-of-planets.md" >}}) and/or
   `trade.md` as appropriate (verify the right mechanic page).

**Acceptance criteria:**

- Both sections present with format + example; the proxy and
  cannot-revoke / orbit-number rules folded into Hugo callouts or prose (no `{%`);
  "Empire"→"nation" in the proxy wording; mechanics linked, not restated.

---

# How-to tasks (Tasks 15–18)

These build `content/how-to/writing-orders.md`. Read `how-to-guides.rst` first:
action-oriented, conditional imperatives, logical sequence, no teaching/strategy,
no restating the per-order format (link the reference for that).

## Task 15 — Create the how-to; front matter, intro, scaffolding

**Status:** DONE

**Scope:** create `content/how-to/writing-orders.md` with front matter, a goal
statement, and the framing that ties it to the reference and to Sequence of Turn
Execution.

**Steps:**

1. Front matter: `title: Write a turn's orders`, `weight: 10`.
2. Goal sentence ("This guide shows you how to assemble the orders for one turn
   …"). State the assumed competence (the reader knows what they want their
   nation to do this turn).
3. Link the reference for per-order format
   ([Writing Orders]({{< relref "../reference/writing-orders.md" >}})) and
   [Sequence of Turn Execution]({{< relref "../reference/sequence-of-turn-execution.md" >}})
   for the order in which orders must appear. State the one load-bearing rule the
   guide is built around: **write orders in Sequence-of-Play order or they may not
   execute** — but link, don't restate the 21 stages.
4. Leave clearly-marked placeholders (HTML comments or short stub headings) for
   the three worked sections that Tasks 16–18 fill: the set-up walkthrough, the
   complete order file, and the Sequence-of-Play sequences. Do **not** hand-author
   any how-to index/card entry (Hextra auto-generates it — `[[hextra-auto-cards-no-manual-index]]`).

**Acceptance criteria:**

- File exists with `title: Write a turn's orders`, `weight: 10`.
- Goal + assumed-competence framing present; reference and sequence-of-turn-execution
  linked; the Sequence-of-Play rule stated and linked (not restated).
- No `{%`; no "Empyrean Challenge"; how-to mode (no per-order format duplicated).

---

## Task 16 — How-to: the full `set up … end` walkthrough

**Status:** DONE

**Scope:** fill the set-up section with the **full** multi-line `set up … end`
block shown in context, with the prose the reference deliberately omits.

**Steps:**

1. Reproduce the manual's full set-up block (all transfer lines) as one fenced
   `text` block, codes swapped (`STU`, `SDRV-1`, `LSP-1`, `FOOD`, `PRO`, `SEN-1`,
   `FUEL`, `HDRV-1`). This is the example too long for the reference.
2. Walk through it with conditional imperatives ("list each item to transfer on
   its own line; close the block with `end`"). Explain **why** the order may span
   several lines and why `end` is required — the kind of "why" that is banned from
   the reference and belongs here.
3. Link back to [Set up orders]({{< relref "../reference/writing-orders.md#set-up-orders" >}})
   for the bare format and to
   [Establishment]({{< relref "../reference/colonies-and-ships.md#establishment" >}})
   for what set up does. Do not teach which units to put in a ship (that's
   strategy — out of scope).

**Acceptance criteria:**

- The full multi-line set-up block is present with codes swapped; prose explains
  the block/`end` mechanics (the "why" the reference omits).
- Links back to the reference format and to Establishment; no strategy advice.

---

## Task 17 — How-to: a complete sample order file

**Status:** TODO

**Scope:** fill the order-file section with one realistic, complete order file.

**Steps:**

1. Show a single fenced `text` block containing: the page header line (player
   name, player ID No., game No., game-turn No., signature placeholders — keep the
   turn-sheet wording per Divergence 3), slashed-zero usage, a `//` comment or
   two, and a handful of real orders for one or more ships/colonies, codes
   swapped. Keep it plausible but compact.
2. Annotate the file with conditional imperatives in prose ("put the header at the
   top of each page"; "use `//` to leave notes the parser ignores"). Link back to
   [General rules]({{< relref "../reference/writing-orders.md#general-rules" >}}).
3. If the manual's Appendix C ("Orders File") sample is relevant, note it as the
   model but do not duplicate Appendix C verbatim if it is not yet converted —
   leave a `{{< callout type="warning" >}}` TODO if it should later link there.

**Acceptance criteria:**

- One complete, compact sample order file present with header line, slashed zero,
  `//` comments, and several orders, codes swapped.
- Annotated with conditional imperatives; links back to the reference General
  rules; no per-order format restated.

---

## Task 18 — How-to: multi-order sequences in Sequence-of-Play order

**Status:** TODO

**Scope:** fill the sequencing section with multi-order examples arranged in
Sequence-of-Play order, showing several orders working together.

**Steps:**

1. Show one or two short sequences (e.g. dis-assembly before assembly; a transfer
   feeding a later order) ordered to match
   [Sequence of Turn Execution]({{< relref "../reference/sequence-of-turn-execution.md" >}}).
   Use the manual's own assemble/dis-assembly illustration as the anchor case.
2. Explain **why** the ordering matters (the parser may drop an out-of-order
   order) — the "why" banned from the reference. Use conditional imperatives
   ("write your dis-assembly orders before your assembly orders").
3. Link the canonical stage order rather than restating the 21 stages; link back
   to the relevant reference order sections for each order's format.

**Acceptance criteria:**

- At least one multi-order sequence in Sequence-of-Play order, with prose
  explaining why order matters; links to Sequence of Turn Execution and back to
  the reference; no restating of the 21-stage list; no strategy advice.

---

# Wiring and verify (Tasks 19–20)

## Task 19 — Wire both pages into the site; index, reciprocal links, glossary

**Status:** TODO

**Scope:** make both pages reachable and link the Working Index 17.x sub-tree. No
new body content beyond links.

**Steps:**

1. **Working Index** in `content/_index.md`: turn the `17 - WRITING ORDERS` line
   and its full **17.x sub-tree** into `relref` links/anchors into the reference
   page using the anchor scheme above (`#general-rules`, `#combat-orders`,
   `#set-up-orders`, … `#colonization-orders`, plus `#naming-planets` /
   `#naming-ships-and-colonies`). Map each 17.2.x label to its matching anchor;
   point `17.2 - List of Orders` at the page top or the first order anchor.
2. **Add the missing Disband entry** (Divergence 2): insert a Disband orders line
   in source order (after Draft) with a `#disband-orders` relref, and renumber the
   following 17.2.x labels accordingly.
3. **Reciprocal page links:** confirm the reference intro links the how-to (Task
   1) and the how-to links the reference (Task 15); add any per-section back-links
   the worked examples need (set-up, general rules, order formats). Verify both
   directions resolve.
4. **Glossary** (`glossary.md`): add/relink the order-form terms that don't
   already have entries — e.g. **Order** (general), **Percent committed**
   (cross-link to the existing *Commitment* entry if duplication is a risk),
   **Set-up block**, **Build change order** (already exists — confirm it points
   right), **Proxy** (trade-station/colonization), **Slashed zero**. Keep entries
   alphabetical; link each to the right `writing-orders.md` anchor or to the
   mechanic page. Do not duplicate existing entries (Set up order, Control order,
   Disband, Disassembly, News release, Ration, Draft, Pay all already exist —
   relink to the new anchors where helpful rather than re-adding).

**Acceptance criteria:**

- The `content/_index.md` 17.x sub-tree resolves via `relref` to real anchors on
  the reference page; the Disband entry is added and following labels renumbered.
- Reference ↔ how-to reciprocal links resolve in both directions.
- Glossary has the new order-form terms (no duplicates), each linking correctly.
- No hand-authored how-to index/card entry (Hextra auto-generates it).

---

## Task 20 — Build, verify, and consistency pass

**Status:** TODO

**Scope:** confirm both pages build, all links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build — **no** `relref` "not found" errors
   and no duplicate-weight warnings.
2. Grep both new/changed pages for leftover Markdoc shortcodes (`{%`), broken or
   relative Markdown links, and the string "Empyrean Challenge".
3. Confirm sidebar order: reference `writing-orders` (180) sits after
   `sequence-of-turn-execution` (170) and before `glossary` (185); the how-to
   `writing-orders` (10) appears as the first card under How-to guides.
4. Confirm every `relref` on **both** pages targets an existing file and that each
   overlap-map anchor resolves (`#establishment`, `#assembling`,
   `#dis-assembling`, `#retooling`, `#percentage-of-commitment`, `#spy-functions`,
   `#taking-control`, `#trade-stations`, `#news-service`, `#surveys`, `#probes`,
   `#interplanetary-movement`, `#interstellar-movement`, `#rations`,
   `#starvation`, `#orders`, `#population-changes`, …). Where an anchor could not
   be confirmed, verify a page-level link and/or a `{{< callout type="warning" >}}`
   TODO is in place instead of an invented anchor.
5. Confirm the Working-Index 17.x anchors resolve to the reference page's actual
   headings.
6. Re-read both pages against `CLAUDE.md` and the Diátaxis skill: the reference is
   describe-only (no instruction/strategy); the how-to is action-oriented (no
   per-order format duplicated, no strategy); no engine code added; no rule
   duplicated that an overlap-map page owns.
7. Confirm both pages use the manual's comma-delimited, target-first grammar
   consistently and that no engine-grammar (`notes/orders.md`) syntax leaked in.

**Acceptance criteria:**

- `hugo --gc` builds with no errors or broken-`relref` warnings.
- No `{%` shortcodes, no "Empyrean Challenge", no broken links on either page.
- Reference reads as austere catalog; how-to reads as a task guide; both wired
  reciprocally; index 17.x resolves; sidebar order correct.

---

## Out of scope

- **Strategy / optimization advice** — which orders to pick and why; neither page
  teaches tactics. (The how-to shows **how** to write a turn's orders, not how to
  win.)
- **Unit stats and code definitions** — owned by `units.md` / `weapons.md` /
  `ship-systems.md`; link, do not restate.
- **Adopting or reconciling the engine order grammar** in `notes/orders.md` —
  both pages publish the manual's grammar (Divergence 1). Migrating to the engine
  grammar is a separate future task and that grammar is not confirmed complete; do
  not adopt or mix it here.
- **Any engine code**, including the order parser — lives in the separate `pyre`
  repo.
- **Editing `user-manual/writing-orders.md`** — sacred; typo fixes only.
- **Converting Appendix C** (sample Orders File / Turn Report) — out of scope for
  this conversion; the how-to may note it as a future link target via a
  `{{< callout type="warning" >}}` TODO, but does not convert it.

> Note: worked order-file walkthroughs are **not** out of scope — they are the
> explicit purpose of the companion how-to deliverable (Tasks 16–18).
