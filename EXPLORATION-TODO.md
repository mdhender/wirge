# EXPLORATION-TODO — Convert "Exploration" to a reference page

Plan for converting `user-manual/exploration.md` (the manual's Exploration
chapter) into a published Diátaxis **reference** page at
`content/reference/exploration.md`.

This plan is split into four small, independently reviewable tasks. Tasks 1–2
write the page content; task 3 wires it into the site (and reconciles an existing
duplication); task 4 builds and verifies. Read the shared context below before
starting any task — it applies to all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in EXPLORATION-TODO.md. Update the task status to
DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; Ship movement | TODO |
| 2 — Probes + Surveys | TODO |
| 3 — Wire the page into the site; reconcile the probe/survey duplication | TODO |
| 4 — Build, verify, and consistency pass | TODO |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`.

---

## Goal

Produce one authoritative reference page describing exploration: the rules for
ship movement (interplanetary, interstellar, and intra-binary jumps), and the
contents of a probe report and a survey report. The page must match the house
style of the existing reference pages and must **not** duplicate rules that
already live elsewhere — it links to them instead. In particular, Exploration
owns the **movement rules** and the **probe/survey report contents**; it does
**not** restate drive or sensor unit mechanics (those belong to
`ship-systems.md`).

## Source material

`user-manual/exploration.md` is the source (Ship Movement → Interplanetary
Movement, Interstellar Movement; Probes; Surveys). Read it in full first. Do
**not** edit the source — `user-manual/` is sacred (see `CLAUDE.md`); fix unclear
rules in our docs, not the manual.

The source is short. Its authoritative data points to convert:

1. **Interplanetary movement** — a jump within a system is always treated as
   **0.1 light years**; a ship may jump from one orbit to another within the
   system.
2. **Interstellar movement** — a jump may start from **any orbit** and **ends
   automatically in the eleventh orbit** of the target system; interstellar
   distances come from the **Star List**.
3. **Intra-binary movement** — moving between the two systems of a binary is
   *written* as an interstellar jump but is **treated as 0.2 light years**, and
   the ship **may move orbit-to-orbit** (need not arrive in the 11th orbit).
4. **Probe** — executed by sensors on a ship or colony; reports, for **any planet
   in the same system**: orbiting ships (count, mass, ID numbers); orbiting
   colonies (count, mass, ID numbers); surface colonies (count, mass, ID
   numbers); natural-resource deposits (type and **approximate** quantity of
   each); and the planet's **habitability number**.
5. **Survey** — any ship or colony may survey the **planet it is at**; reports the
   number of deposits, **where they are located**, their type, and the **exact**
   number of resource units in each. A survey **requires one transport (`TPT`)
   and one professional unit (`PRO`)** and **completes in one turn**.

The source's two `[Hyper-Engines](/docs/user-manual/basic-units#hyper-engines)`
links are bare `/docs/user-manual/...` links into the sacred manual; convert both
to a `relref` to our [Hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}})
section (see Conventions). The source contains **no Markdoc `{% %}` shortcodes**.

There is **no `notes/` file dedicated to exploration.** The `notes/`
planet-generator files (`planet-generator-v0/1/2.md`, `cluster-generation.md`)
cover engine-internal planet/cluster generation and add nothing authoritative for
movement or report contents; `notes/orders.md` / `notes/quick-command-index.md`
describe order syntax (engine/orders detail) and are **out of scope** here. Do not
import any of it.

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| Hyperdrive jump range/fuel; interplanetary jump = 0.1 ly; "a jump cannot end in deep space" | `ship-systems.md#hyperdrives` |
| Space drives maintain orbit / maneuver in combat; cannot make jumps | `ship-systems.md#space-drives` |
| Sensors conduct probes; probe rate = `TL` planets per turn; sensor auto-reports | `ship-systems.md#sensors` |
| A survey's one transport (`TPT`) and its transfer/capacity mechanics | `ship-systems.md#transports` |
| What a deposit is; resource types (`GOLD`/`FUEL`/`METS`/`NMTS`); approximate vs. exact quantity | `planets.md#natural-resources` |
| Planet types a probe distinguishes | `planets.md#types` |
| The habitability number a probe reports | `habitability.md`; `planets.md#habitability-number` |
| What deposits feed into | `mining.md` (page level / `#deposits`) |
| Interstellar distances (Star List); per-nation visibility of stars | `game-setup.md#star-lists`; `game-setup.md#exploration-visibility` |
| The eleventh orbit an interstellar jump arrives in | `game-setup.md#11th-orbit` |
| Jump / probe / survey **orders** (syntax) | `writing-orders.md` (stub — page-level link only; order-type anchors don't exist yet) |

**Reconcile, do not merely link — the probe/survey report contents are currently
duplicated.** `planets.md#learning-about-a-planet` already describes the probe and
survey report contents, and `ship-systems.md#sensors` ends with
"For probe contents, see [Planets]({{< relref "planets.md#learning-about-a-planet" >}})."
This conversion makes **`exploration.md` the single authoritative home** for those
report contents (the manual files them under Exploration). Task 3 trims
`planets.md#learning-about-a-planet` to a brief planet-side pointer that links
`exploration.md#probes` / `#surveys`, and relinks the `ship-systems.md#sensors`
"probe contents" reference to `exploration.md#probes`. Do **not** leave the full
report list living in two pages.

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Map the
manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| Hyper-Engines (the manual cross-reference) | hyperdrives (`HDRV`) — link `ship-systems.md#hyperdrives` |
| sensors (execute a probe) | sensors (`SEN`) — link `ship-systems.md#sensors` |
| transport (a survey requires one) | transport (`TPT`) — link `ship-systems.md#transports` |
| professional unit (a survey requires one) | `PRO` — link `units.md#population-units` |
| natural resource deposits | deposits (`GOLD` / `FUEL` / `METS` / `NMTS`) — link `planets.md#natural-resources` |
| habitability number | habitability number (HN) — link `habitability.md` |
| I.D. No.'s | ID numbers |
| light years | light years |
| eleventh orbit | the [11th orbit]({{< relref "game-setup.md#11th-orbit" >}}) |
| Star List | Star List — link `game-setup.md#star-lists` |
| "the player" / "a player" | **nation** |

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Exploration`. Weight:
  `100` (see "Page weight and ordering").
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}})`. All the targets
  above are same-directory reference pages, so each takes a **bare filename**
  (including `writing-orders.md`, which lives in `content/reference/`, **not**
  `content/how-to/` — the original brief was wrong on this).
- **Writing-orders is dual-natured (link the reference page for now).** "Writing
  orders" spans two Diátaxis modes: the **reference** page
  (`content/reference/writing-orders.md`) owns the *fit and format* of each order
  (fields, syntax, constraints), while *worked examples* of jump / probe / survey
  orders belong in a **how-to** page that does not yet exist. This Exploration
  page links the **reference** `writing-orders.md` at **page level** (its order-type
  anchors don't exist yet). When a how-to companion is created, examples may link
  there too — but do **not** create that how-to here, and do **not** link a
  `how-to/writing-orders.md` that doesn't exist.
- **Source `/docs/user-manual/...` links:** the source's two bare links to
  `basic-units#hyper-engines` must become `relref`s to
  `ship-systems.md#hyperdrives`. No bare `/docs/user-manual/...` link may survive
  in the output (those point into the unpublished manual).
- **Markdoc shortcodes:** none in this source. Confirm none are introduced; no
  `{% … %}` may appear in the output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications (e.g. the
  intra-binary special case); `{{< callout type="warning" >}}` for the `TODO`
  about the unconverted Combat chapter (see "Dependency to flag").
- **Codes** in backticks (`HDRV`, `SEN`, `TPT`, `PRO`, `GOLD`, `FUEL`, `METS`,
  `NMTS`, …).
- **No duplication:** state the movement rules and report contents authoritatively
  here; link out for everything in the overlap map. Do **not** re-explain
  hyperdrive/space-drive/sensor/transport unit mechanics, deposit/type/HN
  definitions, or the Star List itself.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Dependency to flag explicitly

**Combat-time movement is out of scope and owned by Combat (not yet converted).**
"Ship Movement During Combat" is Working-Index item **11.9**, part of the
unconverted Combat chapter. This Exploration page covers **strategic (jump)
movement** only. Combat maneuver is a space-drive function already summarized at
`ship-systems.md#space-drives`; the tactical combat-movement rules belong to the
Combat page. Add a single `{{< callout type="warning" >}}` `TODO` under
**Ship movement** noting that movement during combat is covered by the
not-yet-converted Combat reference page; **do not** fabricate a `combat.md`
`relref`. Link Combat at page level once that page exists.

## Page weight and ordering (resolved)

The reference weights step by ten in Working-Index order: Trade 90,
**Exploration 100**, Rebellion 110. Exploration is **item 9** in the Working Index
in `content/_index.md`, so its weight is **100**.

No collision and no re-weighting of other pages is required: 100 is free between
`trade.md` (90) and `rebellion.md` (110).

## Link targets — existing vs. pending

**Already exist** (link at the right anchor): `ship-systems.md`
(`#hyperdrives`, `#space-drives`, `#sensors`, `#transports`), `planets.md`
(`#natural-resources`, `#types`, `#habitability-number`,
`#learning-about-a-planet`), `habitability.md`, `mining.md` (`#deposits`),
`game-setup.md` (`#star-lists`, `#exploration-visibility`, `#11th-orbit`),
`units.md` (`#population-units`), `writing-orders.md` (page-level only — its
jump/probe/survey order anchors don't exist yet), `glossary.md`.

**Pending — do not invent a link:** there is **no Combat reference page** yet
(Working-Index item 11). The Combat dependency above is handled with a `warning`
`TODO` and prose; do **not** fabricate a `combat.md` `relref` and do **not**
create a stub (the Combat conversion owns that).

---

## Task 1 — Create the page; Ship movement

**Status:** TODO

**Scope:** create `content/reference/exploration.md` with front matter, a one-line
intro, and the full `## Ship movement` section (with the two movement
sub-sections).

**Steps:**

1. Front matter: `title: Exploration`, `weight: 100`.
2. Intro (1–2 sentences, reference tone): exploration covers how ships move
   between orbits and systems and how a nation learns a planet's contents by
   probe and survey. Keep it austere.
3. `## Ship movement` with two sub-sections (use these headings so the anchors
   resolve from the Working Index):
   - `### Interplanetary movement`: a jump within a system is always treated as
     **0.1 light years**; a ship may jump from one orbit to another within the
     system. Link [Hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}}) for
     jump range, fuel, and the rule that a jump cannot end in deep space — do not
     restate those.
   - `### Interstellar movement`: an interstellar jump may start from **any
     orbit** and **ends automatically in the 11th orbit** of the target system
     (link [game-setup.md#11th-orbit]({{< relref "game-setup.md#11th-orbit" >}}));
     interstellar distances come from the
     [Star List]({{< relref "game-setup.md#star-lists" >}}). State the
     **intra-binary** special case factually: a move between the two systems of a
     binary is written as an interstellar jump but is **treated as 0.2 light
     years**, and the ship **may move orbit-to-orbit** (it need not arrive in the
     11th orbit). Put the intra-binary special case in a
     `{{< callout type="info" >}}` if it reads more clearly set apart, or as a
     plain factual paragraph — either is acceptable; keep it austere.
4. Add the **Combat** dependency `{{< callout type="warning" >}}` `TODO` under
   `## Ship movement` (see "Dependency to flag"): movement during combat is owned
   by the not-yet-converted Combat reference page; no `combat.md` `relref`.
5. Convert both source `/docs/user-manual/basic-units#hyper-engines` links to
   `relref`s to `ship-systems.md#hyperdrives`. Use "nation" throughout; codes in
   backticks.

**Acceptance criteria:**

- `content/reference/exploration.md` exists with valid front matter
  (`weight: 100`).
- `## Ship movement` states: interplanetary = 0.1 ly orbit-to-orbit; interstellar
  starts from any orbit and ends in the 11th orbit, distances from the Star List;
  the intra-binary 0.2-ly orbit-to-orbit special case.
- Hyperdrive/Star List/11th-orbit facts are **linked**, not restated.
- The Combat-movement dependency is a `warning` callout (no fabricated `combat.md`
  link); no bare `/docs/user-manual/...` links and no `{% … %}` shortcodes
  survive; "nation" per the mapping; no "Empyrean Challenge".

---

## Task 2 — Probes + Surveys

**Status:** TODO

**Scope:** add the `## Probes` and `## Surveys` sections — the authoritative
report contents.

**Steps:**

1. `## Probes`: a probe is executed by **sensors (`SEN`)** on a ship or colony
   (link [Sensors]({{< relref "ship-systems.md#sensors" >}}) for the probe rate
   and sensor mechanics — do not restate). A probe reports on **any planet in the
   same system**. List what it reports (a list or small table), mapping terms to
   codes/links:
   - orbiting ships — count, approximate mass, ID numbers;
   - orbiting colonies — count, approximate mass, ID numbers;
   - surface colonies — count, mass, ID numbers;
   - natural-resource [deposits]({{< relref "planets.md#natural-resources" >}}) —
     type and **approximate** quantity of each;
   - the planet's [habitability number]({{< relref "habitability.md" >}}).
   Keep "approximate" explicit (it is the contrast with a survey's exact figures);
   link `glossary.md` "Approximation" only if it reads naturally.
2. `## Surveys`: any ship or colony may survey the **planet it is located at**. A
   survey reports the number of deposits, **where they are located**, their type,
   and the **exact** number of resource units in each. A survey **requires one
   transport (`TPT`)** (link [Transports]({{< relref "ship-systems.md#transports" >}}))
   **and one professional unit (`PRO`)** (link
   [population units]({{< relref "units.md#population-units" >}})), and
   **completes in one turn**.
3. State the probe-vs-survey distinction factually where natural (same-system /
   approximate vs. at-planet / exact / deposit locations) — as description, not as
   advice on which to use.

**Acceptance criteria:**

- `## Probes` lists all five report items with codes/links; "approximate" is
  explicit; sensor mechanics are linked, not restated.
- `## Surveys` states the at-planet scope, the deposit-count/location/type/exact
  contents, the one-`TPT` + one-`PRO` requirement, and the one-turn completion.
- Reference tone throughout (states facts; no "you should probe before
  surveying"); codes in backticks; no `{% … %}` shortcodes; no "Empyrean
  Challenge".

---

## Task 3 — Wire the page into the site; reconcile the probe/survey duplication

**Status:** TODO

**Scope:** make the page reachable, relink the Working-Index 9.x lines, relink the
glossary, and **reconcile the existing probe/survey duplication** so the report
contents live only in `exploration.md`. No new body content beyond the
reconciliation trims.

**Steps:**

1. **Working Index** in `content/_index.md`: turn the bare-text lines 9 and 9.x
   into `relref` links (mirroring Trade/Rebellion):
   - `9 - EXPLORATION` → `9 - [EXPLORATION]({{< relref "reference/exploration.md" >}})`
   - `9.1 - Ship Movement` → anchor `#ship-movement`
   - `9.1.1 - Interplanetary Movement` → anchor `#interplanetary-movement`
   - `9.1.2 - Interstellar Movement` → anchor `#interstellar-movement`
   - `9.2 - Probes` → anchor `#probes`
   - `9.3 - Surveys` → anchor `#surveys`
   Leave items 10+ (Rebellion onward) as they are.
2. **Reconcile `planets.md#learning-about-a-planet`:** the probe/survey report
   contents now live in `exploration.md`. Trim that section to a brief planet-side
   pointer — keep the one-line description of the two methods and **link**
   `exploration.md#probes` and `exploration.md#surveys` for the full report
   contents — and remove the duplicated detail (the per-item mass/ID/quantity
   list). Preserve the surrounding planet facts (what a deposit/type/HN is) where
   they belong.
3. **Relink `ship-systems.md#sensors`:** change the trailing "For probe contents,
   see [Planets]({{< relref "planets.md#learning-about-a-planet" >}})." to point
   at `exploration.md#probes`. Keep the sensor mechanics (probe rate, auto-report)
   in `ship-systems.md`.
4. **Glossary** (`glossary.md`) — these entries **already exist**; relink them
   (do not add duplicates):
   - **Probe** (under **P**) — currently unlinked; add
     `See [Exploration]({{< relref "exploration.md#probes" >}}).`
   - **Survey** (under **S**) — currently unlinked; add
     `See [Exploration]({{< relref "exploration.md#surveys" >}}).`
   - **Jump** (under **J**) — currently unlinked; link
     `exploration.md#ship-movement` (the strategic-movement rules), keeping its
     existing deep-space wording.
   - **Orbit** (under **O**) — optional: link `game-setup.md#stars-and-orbits` if
     it reads naturally; otherwise leave intact. Do **not** duplicate the existing
     Interplanetary/Interstellar-location or Eleventh-orbit entries.
5. **Reciprocal links** where genuinely helpful (keep host wording; just add the
   `relref`): `game-setup.md`'s Star List / 11th-orbit material may note that
   interstellar jumps use the Star List and arrive in the 11th orbit, linking
   `exploration.md#interstellar-movement`. Add only if it earns its place.

**Acceptance criteria:**

- `content/_index.md` lines 9, 9.1, 9.1.1, 9.1.2, 9.2, 9.3 resolve via `relref` to
  the correct `exploration.md` anchors.
- `planets.md#learning-about-a-planet` no longer duplicates the full probe/survey
  report list — it briefly points to `exploration.md#probes` / `#surveys`; the
  planet-side facts are preserved.
- `ship-systems.md#sensors` "probe contents" reference points at
  `exploration.md#probes`.
- Glossary **Probe**, **Survey**, and **Jump** entries are relinked to
  `exploration.md` anchors; no duplicate entries introduced.
- Any reciprocal links added resolve and preserve the host page's wording.

---

## Task 4 — Build, verify, and consistency pass

**Status:** TODO

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build with **no** `relref` "not found"
   errors and no duplicate-weight warnings.
2. Grep the changed pages for leftover Markdoc shortcodes (`{%`), bare
   `/docs/user-manual/` links, broken/relative Markdown links, and the string
   "Empyrean Challenge".
3. Confirm sidebar order: `exploration` (100) sits after `trade` (90) and before
   `rebellion` (110).
4. Confirm every `relref` in the new page targets an existing file and that each
   anchor (`#hyperdrives`, `#space-drives`, `#sensors`, `#transports`,
   `#natural-resources`, `#types`, `#11th-orbit`, `#star-lists`,
   `#population-units`, …) resolves. Confirm the only deliberately *unlinked*
   target is the pending Combat chapter, covered by the `warning` `TODO` (no
   `combat.md` `relref`).
5. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed),
   no engine code added, no duplication of rules owned by other pages (drive /
   sensor / transport mechanics; deposit/type/HN definitions; the Star List).
   Confirm the probe/survey report contents now live **only** in `exploration.md`
   (planets.md and ship-systems.md link to it).

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no bare `/docs/user-manual/` links, no "Empyrean
  Challenge", no broken links in any changed or new file.
- The page reads as authoritative reference and defers (via links) to the pages in
  the overlap map for shared rules; the Combat dependency is flagged, not faked;
  the probe/survey duplication is resolved in favor of `exploration.md`.

---

## Out of scope

- Re-explaining **hyperdrive / space-drive / sensor / transport** unit mechanics
  (owned by `ship-systems.md`) — link them.
- Re-defining **deposits, resource types, planet types, or the habitability
  number** (owned by `planets.md` / `habitability.md` / `mining.md`) — link them.
- Re-describing the **Star List** or **11th orbit** mechanics (owned by
  `game-setup.md`) — link them.
- **Combat-time ship movement** (Working-Index 11.9, owned by the unconverted
  Combat chapter) — flagged with a `warning` `TODO`, linked at page level once
  Combat exists.
- **Jump / probe / survey order syntax** (the *fit and format*, owned by the
  reference `writing-orders.md`) — link at page level; its order-type anchors
  don't exist yet. A how-to companion carrying *worked examples* of those orders
  is a separate, future page — not created or linked here.
- The **planet / cluster generator** and any engine code (lives in the separate
  `pyre` repo); the `notes/` generator and orders files.
- Editing `user-manual/exploration.md`.
