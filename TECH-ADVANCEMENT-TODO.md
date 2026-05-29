# TECH-ADVANCEMENT-TODO — Convert "Technological Advancement" to a reference page

Plan for converting `user-manual/technological-advancement.md` (the manual's
chapter 7) into a published Diátaxis **reference** page at
`content/reference/technological-advancement.md`.

This plan is split into five small, independently reviewable tasks. Tasks 1–3
write the page content; task 4 wires it into the site; task 5 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in TECH-ADVANCEMENT-TODO.md. Update the task
status to DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; TL basics + overview of the three methods | DONE |
| 2 — Research + Research Point Requirements table | DONE |
| 3 — Technology transfer + Buying technology | DONE |
| 4 — Wire the page into the site and apply weight | DONE |
| 5 — Build, verify, and consistency pass | DONE |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`.

---

## Goal

Produce one authoritative reference page describing how a ship or colony raises
its technological level (`TL`): what `TL` caps a colony can manufacture, that a
manufactured unit's `TL` is fixed, and the three methods of advancement —
research (with the Research Point Requirements table), technology transfer, and
buying technology. The page must match the house style of the existing reference
pages and must **not** duplicate rules that already live elsewhere — it links to
them instead.

## Source material

`user-manual/technological-advancement.md` is the source. Read it in full first.
It carries (verify against the source — do not trust this summary):

1. Home colonies (nations) start at `TL 1` and advance through the levels in
   **consecutive** order.
2. A colony's `TL` determines the **highest-TL unit its factories can
   manufacture** (a level-5 colony manufactures `TL 1`–`TL 5` units). A factory's
   **own** `TL` concerns only the **output rate** of units, not the `TL` of what
   it builds.
3. Once a unit is manufactured, its `TL` cannot be changed.
4. Three ways to improve a ship/colony's `TL`:
   - **Research** — a build change order switches a factory group from
     manufacturing to research; it completes its work in process first, then
     produces **1 research point (`RSCH`) per factory unit × that unit's `TL`,
     per year**. The **Research Point Requirements** table gives the points per
     level (`TL 2` = 100,000, doubling each level up to `TL 10` = 25,600,000).
   - **Technology transfer** — an established ship/colony has the same `TL` as
     the ship/colony that established it; **more than one level can transfer at
     once** (a `TL 2` colony could receive levels 3–6 and rise to `TL 6`); a ship
     can transfer only levels **up to its own `TL`** (to transfer level 6, the
     ship must be `TL 6`).
   - **Buying technology** at a market or trade station.

Do **not** edit the source — `user-manual/` is sacred (see `CLAUDE.md`); fix
unclear rules in our docs, not the manual. (No `notes/` file is dedicated to
technological advancement; `notes/unit-codes.md` and `notes/colony-template.md`
mention `RSCH` only in passing and add nothing authoritative for this page.)

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| `TL` sets a unit's mass, cost, effectiveness | `units.md` (production chart; "Differences from the rule book"); `glossary.md` "Technological level" |
| Build change order; "complete work in process first" before switching | `manufacturing.md#retooling` |
| Factory throughput as `× TL` per year (research's `1 × TL` parallels the factory's `20 × TL` MU/year) | `manufacturing.md#factory-units-required` |
| The four-turn year / when annual output lands | `explanation/production-cycle.md` |
| Set up order; an established entity inherits its establisher (mechanism of transfer) | `colonies-and-ships.md#establishment`; `writing-orders.md` |
| Build change / set up / transfer / market order types | `writing-orders.md` (stub — page-level link only; order-type anchors don't exist yet) |
| `RSCH` as factory output used to pay for advancement | `units.md` Prototypes row; `glossary.md` "Research point" |

Note: `colonies-and-ships.md#establishment` documents the set up order but does
**not** currently state that the new entity inherits the establisher's `TL`. That
`TL`-inheritance fact is **owned by this page** (the Technology transfer section);
link `#establishment` for the order mechanism, state the inheritance here.

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Map the
manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| "the players' home colonies (nations)" | home colonies / nations |
| Technological level / "TL" | technological level (`TL`) |
| Research point | `RSCH` |
| Factory unit | factory unit (`FACT`) |
| Factory group | factory group |
| Build change order | build change order (link `manufacturing.md#retooling` / `writing-orders.md`) |
| "transferring the technology" / established ship/colony | set up order; established entity (link `colonies-and-ships.md#establishment`) |
| Market / trade station | market / trade station |
| "player" | **nation** |

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Technological
  Advancement`. Weight: `80` (see "Page weight and ordering").
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Retooling]({{< relref "manufacturing.md#retooling" >}})`. Same-directory
  pages take a bare filename; the production cycle is in `../explanation/`.
- **Markdoc shortcodes:** if any `{% … %}` Markdoc footnote/shortcode appears in
  the source, fold it into prose, a table cell, or a
  `{{< callout type="info" >}}` block. No Markdoc shortcodes may survive in the
  output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications;
  `{{< callout type="warning" >}}` for `TODO`s about unconverted material (the
  Trade page).
- **Codes** in backticks (`TL`, `RSCH`, `FACT`, …); large numbers with thousands
  separators, matching the source table (`100,000` … `25,600,000`).
- **No duplication:** state the advancement rules authoritatively here; link out
  for everything in the overlap map. In particular, do **not** re-explain
  retooling/"finish WIP first" (owned by `manufacturing.md#retooling`), the
  set up order (owned by `colonies-and-ships.md` / `writing-orders.md`), or what
  `TL` does to a unit's stats (owned by `units.md`).
- **Reference tone:** describe and only describe — no "you should", no rationale.
  The worked transfer example (`TL 2` → levels 3–6 → `TL 6`) is an *illustration*,
  kept austere.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Page weight and ordering (resolved)

Weights equal the section's position in `user-manual/toc.json` × 10. In
`toc.json` the order is Forward 1, Introduction 2, History 3, Game Set Up 4,
Basic Units 5, Colonies and Ships 6, Manufacturing 7, **Technological Advancement
8**, Trade 9 — so this page's weight is **80**.

(The Working Index in `content/_index.md` labels it "chapter 7" using the
manual's own chapter numbering, which is offset from the `toc.json` position; the
weight follows the `toc.json` position, `80`, consistent with `manufacturing.md`
at `70`.)

No collision and no re-weighting of other pages is required: 80 is free between
`manufacturing`/`shortages` (70/75) and the future Trade page (90).

## Link targets — existing vs. pending

**Already exist** (link at the right anchor): `units.md`, `manufacturing.md`
(`#retooling`, `#factory-units-required`), `colonies-and-ships.md`
(`#establishment`), `writing-orders.md` (page-level only — its order-type anchors
don't exist yet), `explanation/production-cycle.md`, `glossary.md`.

**Pending — do not invent a link:** there is **no Trade reference page** yet
(Trade is `toc.json` item 9, weight 90, not converted). The source's third
method, "buy technology at a market or trade station," therefore has no trade
page to point at. Handle it (see Task 3) by linking the **market order** at
`writing-orders.md` (page level) **and** marking the missing Trade page with a
`{{< callout type="warning" >}}` `TODO`. Do **not** create a `trade.md` stub here
— the Trade conversion owns that.

---

## Task 1 — Create the page; TL basics + overview of the three methods

**Status:** DONE

**Scope:** create `content/reference/technological-advancement.md` with front
matter, a short intro stating the `TL` basics, and a one-line framing of the
three advancement methods (each method gets its own section in Tasks 2–3).

**Steps:**

1. Front matter: `title: Technological Advancement`, `weight: 80`.
2. Intro (reference tone, a few sentences):
   - Home colonies (nations) start at `TL 1` and advance through the levels
     consecutively.
   - A colony's `TL` caps the highest-`TL` unit its
     [factories]({{< relref "manufacturing.md" >}}) can build (a level-5 colony
     builds `TL 1`–`TL 5` units); a factory's **own** `TL` governs only its
     [output rate]({{< relref "manufacturing.md#factory-units-required" >}}), not
     the `TL` of what it builds.
   - A manufactured unit's `TL` is fixed and cannot change afterward.
   - For what `TL` does to a unit's mass, cost, and effectiveness, link
     [Units]({{< relref "units.md" >}}) rather than restating it.
3. State that a ship or colony's `TL` can be raised in three ways — research,
   technology transfer, and buying technology — each described below. Keep this
   to one framing sentence; the detail lives in the sections.

**Acceptance criteria:**

- `content/reference/technological-advancement.md` exists with valid front matter
  (`weight: 80`).
- The `TL 1` start + consecutive advancement, the colony-`TL` build cap, the
  factory-`TL`-is-output-rate-only distinction, and the "fixed once built" rule
  are all stated, with `TL`-stat detail linked out to `units.md`.
- No `{% … %}` Markdoc shortcodes; "nation" per the mapping; no "Empyrean
  Challenge".

---

## Task 2 — Research + Research Point Requirements table

**Status:** DONE

**Scope:** add the `## Research` section, including the throughput rule and the
Research Point Requirements table.

**Steps:**

1. `## Research`: a [build change order]({{< relref "manufacturing.md#retooling" >}})
   switches a factory group from manufacturing to research. The group completes
   its [work in process]({{< relref "manufacturing.md#retooling" >}}) before
   beginning research — link `manufacturing.md#retooling`, do **not** restate the
   "finish WIP first" behavior.
2. State the throughput rule: a researching group produces **1 research point
   (`RSCH`) per factory unit (`FACT`) × that factory unit's `TL`, per year**. Note
   (briefly, austere) this parallels manufacturing's `20 × TL` mass-units/year
   throughput; link [Factory units required]({{< relref "manufacturing.md#factory-units-required" >}}).
   For when an annual figure lands, link
   [The Production Cycle]({{< relref "../explanation/production-cycle.md" >}})
   rather than explaining the four-turn year.
3. Convert the **Research Point Requirements** table to a Hugo table — `RSCH`
   required to reach each level, preserving the source values exactly:

   | Level | `RSCH` required |
   | ----- | --------------- |
   | 2     | 100,000         |
   | 3     | 200,000         |
   | 4     | 400,000         |
   | 5     | 800,000         |
   | 6     | 1,600,000       |
   | 7     | 3,200,000       |
   | 8     | 6,400,000       |
   | 9     | 12,800,000      |
   | 10    | 25,600,000      |

   (Verify against the source; the cost doubles each level. `TL 1` has no row —
   nations begin there.)

**Acceptance criteria:**

- `## Research` present; the build change order and "finish WIP first" link
  `manufacturing.md#retooling` (not restated).
- The `1 × TL` `RSCH`-per-factory-unit-per-year rule is stated with codes; the
  Research Point Requirements table is correct (`TL 2` = 100,000 … `TL 10` =
  25,600,000) and uses thousands separators.
- Reference tone; no "Empyrean Challenge"; no Markdoc shortcodes.

---

## Task 3 — Technology transfer + Buying technology

**Status:** DONE

**Scope:** add the `## Technology transfer` and `## Buying technology` sections.

**Steps:**

1. `## Technology transfer`:
   - An established ship or colony has the **same `TL`** as the ship/colony that
     established it. Link the order/mechanism to
     [Establishment]({{< relref "colonies-and-ships.md#establishment" >}}) (the
     set up order); state the `TL`-inheritance fact here (it is not on that
     page).
   - **More than one level can transfer at once**: a `TL 2` colony can receive
     levels 3–6 and rise to `TL 6` (worked example, kept as an austere
     illustration).
   - A ship transfers only levels **up to its own `TL`**: to transfer level 6,
     the ship must itself be `TL 6`.
2. `## Buying technology`:
   - `TL` can be bought at a **market or trade station** (via the market order;
     link `writing-orders.md` at page level — its market-order anchor doesn't
     exist yet).
   - Because the Trade reference page is not yet converted, add:

     ```
     {{< callout type="warning" >}}
     **TODO:** The Trade reference page (markets and trade stations) is not yet
     converted. Link the market/trade-station detail here once it exists.
     {{< /callout >}}
     ```

     Adjust the wording to house style, but do **not** invent a `trade.md`
     `relref` — that link is pending the Trade conversion.

**Acceptance criteria:**

- Both sections present. Transfer states `TL` inheritance, multi-level transfer
  (with the `TL 2` → 3–6 → `TL 6` example), and the ship-`TL`-caps-transfer rule;
  it links `colonies-and-ships.md#establishment` for the set up order.
- Buying technology names the market/trade station, links `writing-orders.md` at
  page level, and carries the warning `TODO` for the missing Trade page (no
  fabricated `trade.md` link).
- Reference tone; codes in backticks; no "Empyrean Challenge".

---

## Task 4 — Wire the page into the site and apply weight

**Status:** DONE

**Scope:** make the page reachable and relink the lines/cells that now have a
real target. No new body content.

**Steps:**

1. **Working Index** in `content/_index.md`: replace the bare-text line
   `- 7 - TECHNOLOGICAL ADVANCEMENT` with a `relref` link to the new page top:
   `- 7 - [TECHNOLOGICAL ADVANCEMENT]({{< relref "reference/technological-advancement.md" >}})`.
   (The manual gives this chapter no numbered sub-items in the Working Index, so
   only the one line changes. Leave `8 - TRADE` and below as bare text — Trade is
   not yet converted.)
2. **`units.md`** — relink the `RSCH` Prototypes row Detail cell, which currently
   reads "Technological advancement page not yet converted", to the new page
   (mirroring how the `FACT` row was relinked during the Manufacturing
   conversion):
   `[Technological Advancement]({{< relref "technological-advancement.md" >}})`.
   Also review the **"Differences from the rule book"** note about `RSCH-1`
   ("prohibits research to improve it") — link the phrase to the new page (e.g.
   `technological-advancement.md#research`) if it reads naturally; otherwise leave
   the wording intact.
3. **Glossary** (`glossary.md`): the `Technological level` and `Research point`
   entries already exist — relink them to the appropriate
   `technological-advancement.md` anchor where it adds value (keep their existing
   `units.md` reference). Decide whether to **add** a `Technology transfer` entry
   (linking `technological-advancement.md#technology-transfer`) and/or a
   `Research` entry; add only if it earns its place alphabetically and does not
   duplicate `Set up order` (already present) or `Research point`.
4. **Reciprocal links** where genuinely helpful: `manufacturing.md#retooling` may
   note that a build change order can also switch a factory group to research
   (link back to `technological-advancement.md#research`);
   `colonies-and-ships.md#establishment` may note that the new entity inherits the
   establisher's `TL` (link `technological-advancement.md#technology-transfer`).
   Keep existing wording; just add the `relref`.

**Acceptance criteria:**

- `content/_index.md` line 7 resolves via `relref`; Trade and below remain bare.
- The `units.md` `RSCH` Detail cell links the new page (no "not yet converted"
  text left); any `RSCH-1` relink resolves.
- Glossary relinks/additions resolve and don't duplicate existing entries.
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
3. Confirm sidebar order: `technological-advancement` (80) sits after
   `manufacturing` (70) / `shortages` (75) and before any future Trade page (90).
4. Confirm every `relref` in the new page targets an existing file and that each
   anchor (`#retooling`, `#factory-units-required`, `#establishment`,
   `#production` / `units.md`, …) resolves. Confirm the only deliberately
   *unlinked* target is the pending Trade page, which is covered by the warning
   `TODO` callout (no `trade.md` `relref`).
5. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed),
   no engine code added, no duplication of rules owned by other pages (retooling,
   the set up order, `TL`-stat effects).

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- The page reads as authoritative reference and defers (via links) to the pages
  in the overlap map for shared rules; the Trade dependency is flagged, not
  faked.

---

## Out of scope

- Re-converting Manufacturing or retooling (owned by `manufacturing.md`) — link
  `#retooling` and `#factory-units-required`.
- The **Trade** reference page itself (`toc.json` item 9, weight 90) — not
  created here; the market/trade-station link is left as a flagged `TODO`.
- Re-explaining the four-turn year (owned by `explanation/production-cycle.md`) or
  what `TL` does to unit stats (owned by `units.md`).
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/technological-advancement.md`.
