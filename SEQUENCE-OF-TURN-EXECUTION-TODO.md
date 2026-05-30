# SEQUENCE-OF-TURN-EXECUTION-TODO — Convert "Sequence of Turn Execution" to a reference page

Plan for converting `user-manual/sequence-of-turn-execution.md` (the manual's
chapter 16 in canonical order) into a published Diátaxis **reference** page at
`content/reference/sequence-of-turn-execution.md`.

This plan is split into four small, independently reviewable tasks. Tasks 1–2
write the page content (the 21-stage ordered list); task 3 wires it into the
site; task 4 builds and verifies. Read the shared context below before starting
any task — it applies to all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in SEQUENCE-OF-TURN-EXECUTION-TODO.md. Update the
task status to DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; intro + stages 1–11 | DONE |
| 2 — Stages 12–21 | DONE |
| 3 — Wire the page into the site and apply weight | DONE |
| 4 — Build, verify, and consistency pass | DONE |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`. This page is a
near-perfect example of the reference mode: an ordered list that mirrors the
structure of the machinery (the turn runner), with the "why" links pointed
outward at the explanation pages.

---

## Goal

Produce one authoritative reference page giving the **exact ordered list of the
21 stages** in which a turn resolves. The page is the canonical statement of turn
ordering that the rest of the docs rely on (e.g. that production is calculated
*before* combat, and combat resolves *before* set up). Each stage gets a single
neutral sentence and a cross-link to the page that owns its mechanics. The page
must **not** retell the four-turn production cadence — that belongs to
`explanation/production-cycle.md`, which it links once up front.

## Source material

`user-manual/sequence-of-turn-execution.md` is the source. It is short: a
one-line preamble ("Each turn is processed in stages, as shown below.") followed
by a numbered list of 21 stages. Read it in full first. Do **not** edit the
source — `user-manual/` is sacred (see `CLAUDE.md`); fix unclear rules in our
docs, not the manual.

The 21 stages, **in the exact order the source gives** (preserve this order — it
is the entire point of the page; downstream pages depend on it):

1. Mining and farming production is calculated.
2. Manufacturing production is calculated.
3. Combat takes place.
4. Set up orders are processed.
5. Dis-assembly orders are processed.
6. Build change orders are entered.
7. Mining change orders are entered.
8. Transfers are processed.
9. Assembly orders are processed.
10. All market and trade station activity takes place.
11. Surveys are carried out.
12. Probe and sensor reports are compiled.
13. Espionage activity takes place.
14. Ship movement occurs.
15. Draft orders are processed.
16. Pay and ration orders are entered.
17. Rebellion occurs.
18. Rebel increases take place.
19. Naming and control orders are processed.
20. Population increases are calculated.
21. News service reports are compiled.

**Preserve the source's verbs.** The manual deliberately distinguishes stages
that are *processed* / *take place* / *calculated* (acted on this turn) from
stages that are *entered* (orders recorded so they take effect, e.g. build
change 6, mining change 7, pay and ration 16). Carry that distinction into the
page's wording; do not flatten every stage to "processed."

Check `notes/` for any supplementary prep: `notes/orders.md`,
`notes/turn-report-cheat-sheet.md`, and `notes/quick-command-index.md` may name
the engine's order codes and report sections. As with the manufacturing
conversion, keep engine-internal pipeline detail **out** of the reference page —
state the manual's ordering and link the mechanics pages.

## Overlap map (link, do not restate)

The sequence is the ordered list of stages **within** a turn; the production
cycle is the rhythm **across** turns. They are complementary, not duplicative.

| Source statement | Already covered in (link, don't restate) |
| ---------------- | ---------------------------------------- |
| Why most output is annual / WIP / 4-turn year | `explanation/production-cycle.md` (the cadence — primary overlap) |
| Mining + farming production (stage 1) | `mining.md`, `farming.md` |
| Manufacturing production; build change / dis-assembly / assembly (stages 2, 5, 6, 9) | `manufacturing.md` (`#retooling`, `#dis-assembling`, `#assembling`) |
| Combat (stage 3) | `combat.md` |
| Set up / transfers / assembly (stages 4, 8, 9) | `colonies-and-ships.md` (`#establishment`); order forms → `writing-orders.md` (stub) |
| Market and trade station activity (stage 10) | `trade.md` (`#trade-stations`) |
| Surveys / probe + sensor reports / ship movement (stages 11, 12, 14) | `exploration.md` (`#surveys`, `#probes`, `#ship-movement`) |
| Espionage (stage 13) | `espionage.md` |
| Pay and ration (stage 16) | `food.md#rations` |
| Rebellion + rebel increases (stages 17, 18) | `rebellion.md` (`#when-rebellion-occurs`, `#rebel-increase`, `#turn-sequence`) |
| Naming and control (stage 19) | `control-of-planets.md#taking-control`; naming forms → `writing-orders.md` (stub) |
| Population increases; draft (stages 20, 15) | `population.md` (`#population-changes`); draft order → `writing-orders.md` (stub) |
| News service reports (stage 21) | `communication.md#news-service` |

Note `rebellion.md#turn-sequence` already states the *local* ordering (rebellion
before rebel increase, pay/ration just before). This page is the *global*
canonical ordering; link `#turn-sequence` rather than re-deriving it.

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). The source
text here is mostly order/stage names rather than unit codes, but where a stage
names a unit, use its code:

| Source term | Use in our page |
| ----------- | --------------- |
| Mining / farming / manufacturing production | mines (`MINE`), farms (`FARM`), factories (`FACT`) — link `mining.md` / `farming.md` / `manufacturing.md` |
| Set up order | set up order (link `colonies-and-ships.md#establishment`, `writing-orders.md`) |
| Build change order | build change order (link `manufacturing.md#retooling`) |
| Assembly / dis-assembly order | assembly / dis-assembly order (link `manufacturing.md#assembling` / `#dis-assembling`) |
| Transfer | transfer (link `colonies-and-ships.md`, `writing-orders.md`) |
| Draft order | draft order (link `population.md#population-changes`, `writing-orders.md`) |
| Pay / ration order | pay / ration order (link `food.md#rations`) |
| Naming / control order | naming / control order (link `control-of-planets.md#taking-control`) |
| News service | news service (link `communication.md#news-service`) |
| "player" | **nation** |

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Sequence of Turn
  Execution`. Weight: `170` (see "Page weight and ordering" below).
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Combat]({{< relref "combat.md" >}})`,
  `[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}})`.
- **No Markdoc shortcodes:** the source has none, but if any `{% … %}` survives
  from prep, fold it into prose, a table cell, or a `{{< callout >}}`. No Markdoc
  may appear in the output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications,
  `{{< callout type="warning" >}}` only if some named mechanic genuinely lacks a
  page (see "Link targets" — none should, except order *forms*, for which
  `writing-orders.md` is an existing stub linked at page level).
- **Codes** in backticks (`MINE`, `FARM`, `FACT`, `SPY`, …).
- **No duplication:** state the ordering authoritatively here; link out for every
  mechanic. In particular do **not** restate the four-turn cadence, WIP, or the
  per-unit failure modes — link `production-cycle.md`.
- **Reference tone:** describe only. No "you should," no strategy, no rationale
  beyond a neutral clause. An ordered list of stages with one factual sentence
  each is the whole page.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation."

## Page weight and ordering (resolved)

Weights equal the section's **1-indexed position in `user-manual/toc.json`** × 10
(this is the rule the shipped pages follow, and it runs one ahead of the
published Working-Index number because the unpublished `Forward` is toc item 1).
Sequence of Turn Execution is **toc item 17**, so its weight is **170**. (Its
Working-Index number is 16; do not multiply that — Working-Index 16 × 10 = 160
would collide with Victory Conditions.)

Confirmed against shipped weights: `communication` 150, `victory-conditions` 160,
**`sequence-of-turn-execution` 170**, `writing-orders` 180. **170 is free** — no
collision and no re-weighting of other pages is required. The page sorts in the
sidebar after Victory Conditions and before Writing Orders, matching the manual.

## Link targets — verify each before linking

Almost every mechanic this page names now has a converted page (the recent
commits converted Combat, Espionage, Control of Planets, Communication, and
earlier Trade/Exploration). **The prompt's "pending pages" framing is stale** —
verify and link the real pages below; do **not** leave warning-callout TODOs for
them. The single exception is order *forms* (the syntax of set up / transfer /
draft / pay / ration / naming orders): `writing-orders.md` exists but is a
**stub** with no section anchors, so link it at **page level** only.

| Page | Status | Anchors this page uses |
| ---- | ------ | ---------------------- |
| `explanation/production-cycle.md` | exists | page level |
| `mining.md` | exists | page level |
| `farming.md` | exists | page level |
| `manufacturing.md` | exists | `#retooling`, `#assembling`, `#dis-assembling` |
| `combat.md` | exists | page level |
| `colonies-and-ships.md` | exists | `#establishment` |
| `trade.md` | exists | `#trade-stations` |
| `exploration.md` | exists | `#surveys`, `#probes`, `#ship-movement` |
| `espionage.md` | exists | page level |
| `food.md` | exists | `#rations` |
| `rebellion.md` | exists | `#when-rebellion-occurs`, `#rebel-increase`, `#turn-sequence` |
| `control-of-planets.md` | exists | `#taking-control` |
| `population.md` | exists | `#population-changes` |
| `communication.md` | exists | `#news-service` |
| `writing-orders.md` | **stub** | page level only (no anchors) |
| `glossary.md` | exists | for the wiring task |

Before linking any anchor, confirm it resolves (grep the target file's headings).
The anchors above were checked while writing this plan, but re-verify at
implementation time in case headings shifted.

> **Correction to carry forward:** the prompt referred to
> `content/how-to/writing-orders.md`. The actual file is
> `content/reference/writing-orders.md` (a reference-mode stub; `content/how-to/`
> holds only `_index.md`). Writing Orders is **dual-natured**: the *reference*
> page owns each order's fit and format (syntax), and *worked examples* of
> writing orders may later live in a how-to page. The Sequence page needs only
> the order forms, so link the **reference** path at page level. A future how-to
> for order-writing examples is **not** a link target for this page (out of
> scope).

---

## Task 1 — Create the page; intro + stages 1–11

**Status:** DONE

**Scope:** create `content/reference/sequence-of-turn-execution.md` with front
matter, a short intro, and an ordered list covering **stages 1–11** (mining/
farming production through surveys).

**Steps:**

1. Front matter: `title: Sequence of Turn Execution`, `weight: 170`.
2. Intro (1–2 sentences, reference tone): a turn resolves in a fixed sequence of
   stages, listed below in the order they execute; the same order repeats every
   turn. Link the across-turn rhythm out once:
   "Each stage's output follows the four-turn cadence described in
   [The Production Cycle]({{< relref "../explanation/production-cycle.md" >}})."
   Do **not** restate that cadence.
3. Begin a single ordered list (`1.`…) — Markdown's ordered list, one item per
   stage, numbered to match the source exactly. Each item: the stage name as a
   short neutral clause (preserving the source's verb — *processed* / *entered* /
   *take place* / *calculated*), then a `relref` link to the owning page.
   Stages 1–11:

   1. Mining and farming production is calculated. → `mining.md`, `farming.md`
   2. Manufacturing production is calculated. → `manufacturing.md`
   3. Combat takes place. → `combat.md`
   4. Set up orders are processed. → `colonies-and-ships.md#establishment`
      (and `writing-orders.md`, page level)
   5. Dis-assembly orders are processed. → `manufacturing.md#dis-assembling`
   6. Build change orders are entered. → `manufacturing.md#retooling`
   7. Mining change orders are entered. → `mining.md`
   8. Transfers are processed. → `colonies-and-ships.md` (and
      `writing-orders.md`, page level)
   9. Assembly orders are processed. → `manufacturing.md#assembling`
   10. All market and trade station activity takes place. →
       `trade.md#trade-stations`
   11. Surveys are carried out. → `exploration.md#surveys`

4. Optionally add one `{{< callout type="info" >}}` noting that production
   (stages 1–2) is calculated **before** combat (stage 3) and before any order
   processing, so newly-formed groups produce nothing on the turn they are
   created — but link `production-cycle.md` for the explanation rather than
   spelling out the WIP timing. Keep it to a factual clause; omit if it drifts
   toward instruction.

**Acceptance criteria:**

- `content/reference/sequence-of-turn-execution.md` exists with valid front
  matter (`weight: 170`).
- Stages 1–11 are present as a single ordered list, in exact source order, each
  with the source's verb preserved and a resolving `relref`.
- No four-turn-cadence narrative is restated; `production-cycle.md` is linked.
- No `{% … %}` Markdoc; "nation" not "player"; codes in backticks.

---

## Task 2 — Stages 12–21

**Status:** DONE

**Scope:** continue the same ordered list with **stages 12–21** (probe/sensor
reports through news service reports). No new sections — this is the tail of the
one list started in task 1.

**Steps:**

1. Continue the ordered list (items `12.`…`21.`), same one-sentence-plus-`relref`
   form, source verbs preserved:

   12. Probe and sensor reports are compiled. → `exploration.md#probes`
   13. Espionage activity takes place. → `espionage.md`
   14. Ship movement occurs. → `exploration.md#ship-movement`
   15. Draft orders are processed. → `population.md#population-changes`
       (and `writing-orders.md`, page level)
   16. Pay and ration orders are entered. → `food.md#rations`
   17. Rebellion occurs. → `rebellion.md#when-rebellion-occurs`
   18. Rebel increases take place. → `rebellion.md#rebel-increase`
   19. Naming and control orders are processed. →
       `control-of-planets.md#taking-control` (naming forms →
       `writing-orders.md`, page level)
   20. Population increases are calculated. → `population.md#population-changes`
   21. News service reports are compiled. → `communication.md#news-service`

2. Where two adjacent stages share an owning page (17 + 18 → `rebellion.md`;
   11 + 12 + 14 → `exploration.md`), still give each stage its own list item and
   its own link/anchor; do not merge stages. The list must have exactly 21 items.

**Acceptance criteria:**

- Stages 12–21 complete the ordered list; the page now lists all 21 stages in
  exact source order with no merges, omissions, or reorderings.
- Every `relref` resolves to an existing file/anchor (rebellion, exploration,
  population, food, control-of-planets, espionage, communication).
- Reference tone throughout; no strategy, no cadence restatement.

---

## Task 3 — Wire the page into the site and apply weight

**Status:** DONE

**Scope:** make the page reachable and link the Working-Index line and glossary.
No new body content.

**Steps:**

1. **Working Index** in `content/_index.md`: replace the bare-text line
   `- 16 - SEQUENCE OF TURN EXECUTION` (currently unlinked) with a `relref` link
   into the new page:
   `- 16 - [SEQUENCE OF TURN EXECUTION]({{< relref "reference/sequence-of-turn-execution.md" >}})`.
   The manual's sub-stages are not separately headed on the page (it's one
   ordered list), so a single page-level link is correct — do not invent
   per-stage anchors in the index.
2. **Glossary** (`glossary.md`): the `Turn` entry already exists (one game cycle =
   one quarter year); add entries that don't yet exist, in alphabetical order:
   - `Sequence of turn execution` — the fixed order of the 21 stages in which a
     turn resolves; link `sequence-of-turn-execution.md`.
   - `Stage` (or `Stage (turn)`) — one step of the turn sequence; link
     `sequence-of-turn-execution.md`.
   Relink the existing `Turn` entry to also reference the sequence page if it
   reads naturally; otherwise leave it.
3. **Reciprocal link (consider):** in
   `explanation/production-cycle.md`, where it describes production being
   calculated early in the turn (the "the group is only *formed*" / "production
   is calculated earlier in the turn" passage near `## Factories`), add a
   `relref` to `sequence-of-turn-execution.md` for the full within-turn ordering.
   Keep the existing wording; just add the link. Also consider a back-link from
   `rebellion.md#turn-sequence` to the canonical sequence page. Add these only
   where they read naturally; do not force them.

**Acceptance criteria:**

- `content/_index.md` line 16 resolves via `relref` (no bare
  `SEQUENCE OF TURN EXECUTION` text remains).
- Glossary has the new `Sequence of turn execution` and `Stage` entries, each
  linking correctly and placed alphabetically; no duplicate `Turn` entry.
- Any reciprocal links added resolve and preserve the host page's wording.

---

## Task 4 — Build, verify, and consistency pass

**Status:** DONE

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build with **no** `relref` "not found"
   errors and **no** duplicate-weight warnings (170 must be unique).
2. Grep the changed pages for leftover Markdoc shortcodes (`{%`), broken/relative
   Markdown links, and the string "Empyrean Challenge".
3. Confirm sidebar order: `sequence-of-turn-execution` (170) sits after
   `victory-conditions` (160) and before `writing-orders` (180).
4. Confirm the page lists **exactly 21 stages in exact source order** with the
   source verbs preserved (cross-check against
   `user-manual/sequence-of-turn-execution.md`), and that every `relref`
   (`#retooling`, `#assembling`, `#dis-assembling`, `#establishment`,
   `#trade-stations`, `#surveys`, `#probes`, `#ship-movement`, `#rations`,
   `#when-rebellion-occurs`, `#rebel-increase`, `#taking-control`,
   `#population-changes`, `#news-service`) targets an existing file and anchor.
5. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed
   with explanation), no engine code added, no duplication of the production
   cadence (owned by `production-cycle.md`).

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- The page reads as an austere, authoritative ordered list and defers (via links)
  to the mechanics pages and to `production-cycle.md` for the "why."

---

## Out of scope

- Re-converting the production-cycle narrative — the four-turn year, WIP, and the
  per-unit failure modes are owned by `explanation/production-cycle.md`; link to
  it, never restate it.
- Writing the `writing-orders.md` order forms (still a stub) — link it at page
  level; converting it is a separate later task.
- Any engine code, including the turn runner / scheduler (lives in the separate
  `pyre` repo).
- Editing `user-manual/sequence-of-turn-execution.md` or any other manual file.
