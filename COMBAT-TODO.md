# COMBAT-TODO — Convert "Combat" to a reference page

Plan for converting `user-manual/combat.md` (the manual's chapter 11) into a
published Diátaxis **reference** page at `content/reference/combat.md`.

Combat is by far the longest section in the manual (its 11.x sub-tree runs to
11.13 in the Working Index of `content/_index.md`). This plan is therefore split
into many small, independently reviewable tasks — roughly one per sub-mechanic —
so no single session has to convert the whole chapter. Tasks 1–11 write the page
content section by section; task 12 wires it into the site; task 13 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in COMBAT-TODO.md. Update the task status to
DONE when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; Description, Military supplies, Percentage of commitment | TODO |
| 2 — Attack orders (four order types) | TODO |
| 3 — Raids and invasions (assault craft, assault weapons, transports, military robots) | TODO |
| 4 — Bombardment (by colonies; by ships) | TODO |
| 5 — Defense (soldiers, bombardment, while invading, raids, support) | TODO |
| 6 — Combat factor (table + worked example) | TODO |
| 7 — Casualties (invasion, troop transport, bombardment, raiding) | TODO |
| 8 — Damage: energy weapons (+ energy shields) | TODO |
| 9 — Damage: missiles and anti-missiles | TODO |
| 10 — Ship movement during combat; End of round | TODO |
| 11 — Surrender; Captured colonies; Combat and ship/colony TL | TODO |
| 12 — Wire the page into the site and apply weight | TODO |
| 13 — Build, verify, and consistency pass | TODO |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`. Combat is
procedure-heavy, so the strongest temptation here is to slide into "first the
computer does X, then you should…" Keep it to neutral statements of what the
machinery does. Illustrative worked examples (the manual supplies several) are
permitted as *illustration*, not instruction.

---

## Goal

Produce one authoritative reference page describing the combat machinery: how
attacks are ordered and committed, how raids, invasions, and bombardment are
resolved, how each side defends, how combat factors and casualties are computed,
how energy weapons, missiles, and anti-missiles do damage, how ships move during
combat, and how combat ends — including surrender, capture, and the technological
consequences of capture and population loss. The page must match the house style
of the existing reference pages and must **not** duplicate the weapon/drive unit
stats that already live in `weapons.md` and `ship-systems.md` — it links to them
instead, and owns only the combat **procedure** (which those pages explicitly
defer to "the combat reference material when that section is converted").

## Source material

`user-manual/combat.md` is the source. **Read it in full first.** Do **not** edit
the source — `user-manual/` is sacred (see `CLAUDE.md`); resolve any unclear or
contradictory rule in our docs, never by changing the manual. Transcribe formulas
and tables faithfully; do not "fix" the manual's spellings in quoted prose, but
our converted prose should be clean (the source contains obvious typos —
"traget", "casualiyy", "looses" — which simply should not be reproduced in our
page).

There is **no** `notes/combat.md`; this conversion has no supplementary working
note to mine. The unit stats it relies on are already settled in `weapons.md` and
`ship-systems.md`.

The source carries these authoritative data points the page must render exactly
(verify each against the source — do not trust this list):

1. **Military supplies** — one `MTSP` consumed per soldier unit per combat round.
2. **Percentage of commitment** — applies to `SLD`/`MRBT` for raids and
   invasions; to fuel (for `EWP`) and missiles for bombard orders.
3. **Combat-factor table** — `ASC` `10 x TL`, `ASW` `2 x TL`, `SLD` `1`,
   `MRBT` `2 x TL`; total = soldier factor + weapon factor.
4. **Bombardment distance-factor table** (colonies only) — surface→surface 1,
   surface→orbiting 2, orbiting→orbiting 3.
5. **Ship range** — distance is a random 1–100 in 10,000-mile increments; a ship
   cannot fire `MSS`/`EWP` until within range 10 (100,000 miles).
6. **Transport combat figures** — `0.01 x TL²` fuel units per round trip;
   carrying capacity `3 x TL` mass units per combat round (combat figures differ
   from transfer figures, which live in `ship-systems.md`).
7. **Military robots** — replace `TL x 2` soldier units; commitment applies.
8. **Invasion casualty formulas** — `((A / D) x R₁) x D = DL` and
   `((D / A) x R₂) x A = AL`, with `R₁`,`R₂` random 0.1–0.5; lost-unit % equals
   lost-combat-factor %; 70% of casualties killed (removed), 30% wounded → `UEM`.
9. **Troop-transport casualties** — an `ASC`/`TPT` hit by an energy beam or
   anti-missile is destroyed with all aboard.
10. **Bombardment casualties** — 75% of hits strike `EWP`/`MSL`/`SDRV`; 25% strike
    other parts, possibly population.
11. **Raiding casualties** — invasion formula result × 0.01.
12. **Energy-weapon damage** — beam energy `10 x TL`; damage `((F + D) x E) - SH =
    DA`; 75% of mass-unit damage to `MSL`/`EWP`/`SDRV`; hit-rate tables vs
    `ASC`/`TPT` (surface 50% fire / 10% hit; orbiting 75% / 20%; ship 100% / 40%)
    and vs missiles (`25% + 5% x TL`).
13. **Energy shields** — deflect `10 x TL` energy units per round (the `SH` term).
14. **Missiles** — `M / D² = H`; each hit does `100 x TL` mass-unit damage; same
    75/25 split; `MSL` TL subtracted from `D²` for accuracy, floored at `D² = 1`.
15. **Anti-missiles** — one per `MSL` per attack; vs missiles `50 + (TL x 5)`%;
    vs `ASC`/`TPT` use the missile hit formula, ÷2 for transports and ÷4 for
    assault craft, `ASC` absorbed first.
16. **Surrender** — at 6:1 odds soldier units surrender automatically and become
    `UEM` in place; `MRBT` fight until killed.
17. **Capture** — a ship/colony whose defenders are destroyed/surrendered becomes
    the attacker's if the attacker still has troops there.
18. **Captured population / TL** — on transfer 50% of loyal pop → rebels, 50% of
    rebels → loyal, remaining soldiers disbanded → `UEM`; foreign-race pop rebels
    at double rate; a captured ship/colony drops one TL (floor TL1); a colony that
    loses ≥20% population to bombardment or rebellion drops one TL (floor TL1).

## Overlap map (link, do not restate)

| Source statement | Already covered in — link, don't restate |
| ---------------- | ---------------------------------------- |
| `EWP`, `MSS`, `ANM`, `ESH`, `ASW` unit stats (mass, fuel, TL behavior) | `weapons.md` (the **stats owner**; this page links them and adds only combat procedure) |
| `MSL` launches `MSS`/`ANM`; accuracy depends on launcher TL | `weapons.md#missile-launchers` |
| `MRBT` replaces `TL x 2` `SLD`; cannot replace a `SPY`'s soldier | `weapons.md#military-robots` |
| `ASC`/`ASW`/`MTSP` unit stats | `weapons.md#assault-craft`, `#assault-weapons`, `#military-supplies` |
| `SDRV` thrust/combat-movement/fuel; transport transfer stats | `ship-systems.md#space-drives`, `#transports` |
| `SLD`, `MRBT`, `UEM` codes; "Differences from the rule book" | `units.md#population-units`, `units.md#differences-from-the-rule-book` |
| 70%/30% killed-vs-wounded; `UEM` definition | `population.md#population-classes`; `units.md` |
| Ships/colonies as combatants; capture changing the owner | `colonies-and-ships.md` |
| Captured loyal pop → rebels; foreign race → double rate; ≥20% loss → TL drop | `rebellion.md#loyalty-on-capture`, `rebellion.md#when-rebellion-occurs` (DONE — link the `#`-anchors, do **not** restate) |
| What a TL is; TL transfer/upgrade | `technological-advancement.md` (link page level / `#technology-transfer`) |
| Raid/bombard/invade/support order syntax | `writing-orders.md` (stub — **page-level** link only; order-type anchors do not exist yet) |

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Map the
manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| "player" | **nation** |
| Soldier unit(s) | `SLD` |
| Military robot(s) | `MRBT` |
| Assault craft | `ASC` |
| Assault weapon(s) | `ASW` |
| Transport(s) | `TPT` |
| Military supplies | `MTSP` |
| Missile(s) | `MSS` |
| Missile launcher(s) | `MSL` |
| Anti-missile(s) | `ANM` |
| Energy weapon(s) / energy beam | `EWP` |
| Energy shield(s) | `ESH` |
| Space drive(s) | `SDRV` |
| Unemployables | `UEM` |
| Fuel | `FUEL` |
| Technological level / TL | `TL` (link `technological-advancement.md`) |

Render the formula variables as the manual gives them (`A`, `D`, `DL`, `AL`,
`R₁`, `R₂`, `F`, `E`, `SH`, `DA`, `M`, `H`, `DF`) inside fenced ` ```text ` blocks
and accompanying variable tables, exactly as `manufacturing.md` renders its
formulas.

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Combat`. Weight: `120`
  (see "Page weight and ordering" below).
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Weapons]({{< relref "weapons.md#energy-weapons" >}})`. Same-page links use a
  bare anchor, e.g. `[Combat factor](#combat-factor)`.
- **Footnotes:** the source uses Markdoc `{% footnotes %}` / `{% footnote %}` /
  `{% fnref %}` shortcodes (four `fnref` call-sites, four footnote bodies). These
  do **not** render in Hugo/Hextra. Fold each into the prose or a
  `{{< callout type="info" >}}` block at the point it is referenced. No Markdoc
  `{%` may survive in the output. The four footnotes are:
  - **fn1** (on "invade another ship/colony"): an invasion of a ship is a
    boarding party → fold into Attack orders / invasion (Task 2).
  - **fn2** (on defensive energy beams): a surface colony cannot fire `EWP` at
    another surface colony → fold into Defense against soldier units (Task 5);
    consistent with the `EWP` exclusion already in `weapons.md`.
  - **fn3 / fn4** (identical text, on defensive fire in soldier defense and in
    bombardment defense): if two or more nations attack, only one nation's
    ships/colonies are fired upon → fold into Defense against soldier units and
    Defense against bombardment respectively (Task 5).
- **Existing source link to fix:** the source's Ship Movement section links
  `(/docs/user-manuals/space-drives)` — replace with
  `{{< relref "ship-systems.md#space-drives" >}}`.
- **Callouts:** `{{< callout type="info" >}}` for clarifications;
  `{{< callout type="warning" >}}` for `TODO`s pointing at not-yet-converted
  sibling sections (Espionage, Control of Planets — see Dependencies).
- **Codes** in backticks (`EWP`, `SLD`, `ASC`, `MTSP`, …).
- **No duplication:** state the combat procedure and its formulas/tables
  authoritatively here; link out for every unit stat and for the rebellion/TL
  rules already owned elsewhere (overlap map).
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Page outline and anchors (fixed — all tasks and the wiring must agree)

Mirror the source's 11.x structure (Diátaxis "respect the structure of the
machinery"). Use exactly these headings so the wiring anchors in Task 12 are
predetermined:

```
## Description                          #description                       (Task 1)
## Military supplies                    #military-supplies                 (Task 1)
## Percentage of commitment             #percentage-of-commitment          (Task 1)
## Attack                               #attack                            (Task 2)
### Attack orders                       #attack-orders                     (Task 2)
### Raids and invasions                 #raids-and-invasions               (Task 3)
#### Assault craft                      #assault-craft                     (Task 3)
#### Assault weapons                    #assault-weapons                   (Task 3)
#### Transports                         #transports                        (Task 3)
#### Military robots                     #military-robots                   (Task 3)
### Bombardment                         #bombardment                       (Task 4)
#### Bombardment by colonies            #bombardment-by-colonies           (Task 4)
#### Bombardment by ships               #bombardment-by-ships              (Task 4)
## Defense                              #defense                           (Task 5)
### Defense against soldier units       #defense-against-soldier-units     (Task 5)
### Defense against bombardment         #defense-against-bombardment       (Task 5)
### Defense while invading              #defense-while-invading            (Task 5)
### Defense against raids               #defense-against-raids             (Task 5)
### Defense support                     #defense-support                   (Task 5)
## Combat factor                        #combat-factor                     (Task 6)
## Casualties                           #casualties                        (Task 7)
### Invasion casualties                 #invasion-casualties               (Task 7)
### Troop transport casualties          #troop-transport-casualties        (Task 7)
### Bombardment casualties              #bombardment-casualties            (Task 7)
### Raiding casualties                  #raiding-casualties                (Task 7)
## Damage                               #damage                            (Task 8)
### Energy weapons                      #energy-weapons                    (Task 8)
### Missiles                            #missiles                          (Task 9)
### Anti-missiles                       #anti-missiles                     (Task 9)
## Ship movement during combat          #ship-movement-during-combat       (Task 10)
## End of round                         #end-of-round                      (Task 10)
## Surrender                            #surrender                         (Task 11)
## Captured colonies                    #captured-colonies                 (Task 11)
### Captured population units           #captured-population-units         (Task 11)
## Combat and ship or colony TL         #combat-and-ship-or-colony-tl      (Task 11)
```

(These anchors live on `combat.md`; `weapons.md` having its own `#energy-weapons`
/ `#missiles` / `#anti-missiles` is no conflict — `relref` anchors are
page-scoped.)

## Page weight and ordering (resolved)

Reference-page weights step by ten in Working-Index order. Combat is section 11;
the neighbouring converted pages are Rebellion (10) at `weight: 110` and the
not-yet-converted Espionage (12) which will take `weight: 130`. Combat's weight is
therefore **120**, which is free between `rebellion.md` (110) and the next
converted page. No re-weighting of any other page is required.

## Link targets — existing vs. pending

**Exist now (link freely, at the verified anchors above):** `weapons.md`,
`ship-systems.md`, `units.md`, `population.md`, `colonies-and-ships.md`,
`rebellion.md`, `technological-advancement.md`, `glossary.md`.

**Stub (page-level link only — order-type anchors absent):** `writing-orders.md`.

**Do not exist yet (do NOT invent links):** Espionage (Working-Index 12) and
Control of Planets (Working-Index 13) have no pages. Reference them at page level
in prose and/or leave a `{{< callout type="warning" >}}` `TODO`. See Dependencies.

## Dependencies to flag explicitly

Three tightly-coupled siblings are **not yet converted**; the page must not
fabricate links to them:

- **Control of Planets** (Working-Index 13) — capture leads to *control* of a
  planet. Capture in Task 11 should note this hand-off with a `warning` callout,
  not a link.
- **Espionage** (Working-Index 12) — rebels, `SPY`, incite rebellion border on
  combat's capture/loyalty rules. Where captured-population loyalty is described
  (Task 11), link `rebellion.md#loyalty-on-capture` (which exists) and leave
  Espionage as a page-level mention / `warning` `TODO`.
- **Technological Advancement** (section 7) — the TL mechanic *does* have a page
  (`technological-advancement.md`); link it for what a TL is, but combat **owns**
  the TL-loss-on-capture and ≥20%-loss rules (Task 11).

---

## Task 1 — Create the page; Description, Military supplies, Percentage of commitment

**Status:** TODO

**Scope:** create `content/reference/combat.md` with front matter, the intro
`## Description`, `## Military supplies`, and `## Percentage of commitment`.

**Steps:**

1. Front matter: `title: Combat`, `weight: 120`.
2. `## Description`: combat occurs when a nation orders an attack by its ships or
   colonies against another nation's ships or colonies; attacker and target must
   be at the same orbit within the same system; combat runs in indefinite rounds
   bounded by mission completion or exhaustion of troops, `FUEL`, missiles, and
   `MTSP`; raids are the exception — one round only. Link
   `colonies-and-ships.md` for the combatant entities.
3. `## Military supplies`: one `MTSP` is consumed per `SLD` unit per combat round.
   Link `weapons.md#military-supplies` for the unit stat; state only the
   consumption rule here.
4. `## Percentage of commitment`: every combat order carries a commitment
   percentage — the share of units committed to the attack. For invasions and
   raids it applies to `SLD` and `MRBT`; for bombard orders it applies to `FUEL`
   (for `EWP`) and missiles. Note uncommitted units remain for defense (forward
   reference to Raids and invasions / Defense).

**Acceptance criteria:**

- `content/reference/combat.md` exists with valid front matter (`weight: 120`).
- The three sections are present, austere, and use codes; `MTSP` stat links out.
- No `{% … %}` Markdoc; "nation" per the mapping.

---

## Task 2 — Attack orders (four order types)

**Status:** TODO

**Scope:** add `## Attack` and `### Attack orders`.

**Steps:**

1. `## Attack`: one-line lead-in (combat orders are executed simultaneously; only
   one combat order per turn per ship/colony).
2. `### Attack orders`: describe the four order types — **raid** (steal one type
   of unit, including population, from another ship/colony), **invasion** (invade
   to capture), **bombard** (use `MSS` and `EWP` to destroy), **support** (assist
   another nation in an invasion, and for defense — see Defense support). State
   that the supporting and supported nations do not attack each other and fight as
   one unit. Link `writing-orders.md` at **page level** for the order syntax.
3. Fold **footnote 1** here: an invasion of a ship can be considered a boarding
   party (info callout or parenthetical).

**Acceptance criteria:**

- All four order types described with codes; fn1 folded in; `writing-orders.md`
  linked page-level only.
- Reference tone (states what each order does; no "you should raid when…").

---

## Task 3 — Raids and invasions (assault craft, assault weapons, transports, military robots)

**Status:** TODO

**Scope:** add `### Raids and invasions` and its four `####` sub-units.

**Steps:**

1. `### Raids and invasions`: round-one setup — committed troops are assigned to
   `ASC`; overflow goes into `TPT` armed with `ASW`; troops with neither remain
   with the uncommitted (defending) soldiers; uncommitted troops stay for defense.
2. `#### Assault craft`: `ASC` transports `SLD`; one `SLD` operates and is the
   max it holds. Link `weapons.md#assault-craft` for the stat.
3. `#### Assault weapons`: each `ASW` needs one `SLD` to operate; destroyed when
   its `SLD` is destroyed. Link `weapons.md#assault-weapons`.
4. `#### Transports`: combat fuel use `0.01 x TL²` `FUEL` per round trip; combat
   carrying capacity `3 x TL` mass units per combat round. State explicitly that
   these combat figures differ from the transfer figures in
   `ship-systems.md#transports` (link it).
5. `#### Military robots`: `MRBT` replace `SLD`, functioning as soldiers but
   quicker/stronger/harder to kill; each replaces `TL x 2` `SLD`; commitment
   applies. Link `weapons.md#military-robots`.

**Acceptance criteria:**

- All four sub-sections present, using codes; the transport **combat** figures
  are rendered and distinguished from transfer figures (link).
- `MRBT` `TL x 2` replacement stated; no duplication of the full unit stats.

---

## Task 4 — Bombardment (by colonies; by ships)

**Status:** TODO

**Scope:** add `### Bombardment`, `#### Bombardment by colonies`,
`#### Bombardment by ships`.

**Steps:**

1. `#### Bombardment by colonies`: colonies bombard with `MSS` or `EWP`, except a
   surface colony cannot use `EWP` against another surface colony (line-of-sight).
   Render the distance-factor (`DF`) table exactly:

   | Attacker | Defender | Distance factor (`DF`) |
   | -------- | -------- | ---------------------- |
   | Surface colony | Surface colony | 1 |
   | Surface colony | Orbiting colony | 2 |
   | Orbiting colony | Orbiting colony | 3 |

   Note `DF` is used by colonies only (it stands in for the ship `D` used in the
   damage formulas of Tasks 8–9).
2. `#### Bombardment by ships`: a ship's distance to the planet/orbiting
   colony/target ship is a random number `1`–`100` in increments of 10,000 miles;
   a ship cannot fire `MSS`/`EWP` until within range `10` (100,000 miles).

**Acceptance criteria:**

- The `DF` table is exact; the surface-to-surface `EWP` exclusion is stated and is
  consistent with `weapons.md`.
- Ship range rule (random 1–100; fire within 10) is stated.

---

## Task 5 — Defense (soldiers, bombardment, while invading, raids, support)

**Status:** TODO

**Scope:** add `## Defense` and its five `###` sub-sections.

**Steps:**

1. `## Defense`: a ship/colony automatically defends against raids, invasions, and
   bombardments.
2. `### Defense against soldier units`: defender's `EWP` and `ANM` fire on the
   attacking `ASC`/`TPT`; on the surface, attacking `ASC` are met by defending
   `ASC`, transported troops met by the defender's uncommitted `SLD`; defender
   fires `MSS` and `EWP` at the attacker. Fold **footnote 2** (surface colony
   cannot fire `EWP` at another surface colony) and **footnote 3** (if two or more
   nations attack, only one nation's ships/colonies are fired upon).
3. `### Defense against bombardment`: defender fires `ANM` at incoming `MSS`,
   raises `ESH` to deflect `EWP` beams, and fires `EWP`/`MSS` back. Fold
   **footnote 4** (same text as fn3 — only one attacking nation is fired upon).
4. `### Defense while invading`: a ship/colony attacked mid-invasion recalls its
   `SLD` home unless already successful, in which case only half return and the
   original order aborts.
5. `### Defense against raids`: as defense against soldier units, but a raid lasts
   one round.
6. `### Defense support`: support orders may assist another nation's defense; an
   invaded supporting ship/colony recalls its `SLD` home. Cross-link Attack orders
   (support) and `writing-orders.md` page-level.

**Acceptance criteria:**

- Five sub-sections present; footnotes 2, 3, and 4 folded in at the right points;
  no `{%` remains.
- Codes used throughout; reference tone.

---

## Task 6 — Combat factor (table + worked example)

**Status:** TODO

**Scope:** add `## Combat factor`.

**Steps:**

1. State that combat factors determine raid/invasion casualties; each unit gets a
   factor. Render the table exactly:

   | Unit | Combat factor |
   | ---- | ------------- |
   | `ASC` | `10 x TL` |
   | `ASW` | `2 x TL` |
   | `SLD` | 1 |
   | `MRBT` | `2 x TL` |

2. State the composition rule: a force's factor adds each soldier's base factor to
   its weapon's factor. Include the manual's illustration (5,000 `SLD` with `TL1`
   `ASW` + 5,000 `SLD` with `TL1` `ASC` → total 70,000) as an austere example.

**Acceptance criteria:**

- Table exact; composition rule and worked example present, kept illustrative.

---

## Task 7 — Casualties (invasion, troop transport, bombardment, raiding)

**Status:** TODO

**Scope:** add `## Casualties` and its four `###` sub-sections.

**Steps:**

1. `### Invasion casualties`: render the formulas in a ` ```text ` block exactly:

   ```text
   ((A / D) x R₁) x D = DL
   ((D / A) x R₂) x A = AL
   ```

   with a variable table (`A` attacker factors, `D` defender factors, `DL`/`AL`
   losses, `R₁`/`R₂` random 0.1–0.5). Include the manual's worked example
   (A=500, D=100 → DL=150, AL=50). State that the **percentage** of unit losses
   equals the percentage of combat-factor losses (so the example attacker loses
   10% of `SLD`/`ASC`/`ASW`; the defender loses all). State the 70%-killed
   (removed from play) / 30%-wounded (→ `UEM`) split; link
   `population.md#population-classes` / `units.md` for `UEM`.
2. `### Troop transport casualties`: applies to `SLD` in `TPT` and `ASC` while
   moving to the target — an `ASC`/`TPT` hit by an energy beam or `ANM` is
   destroyed with all aboard.
3. `### Bombardment casualties`: 75% of hits strike `EWP`/`MSL`/`SDRV`; 25% strike
   other parts and may include population; the computer randomly selects which
   units are hit.
4. `### Raiding casualties`: the invasion formula result × 0.01, for both sides.

**Acceptance criteria:**

- Formulas and variable tables exact; worked example present; 70/30 split stated
  with `UEM` linked.
- All four sub-sections present; reference tone.

---

## Task 8 — Damage: energy weapons (+ energy shields)

**Status:** TODO

**Scope:** add `## Damage` lead-in and `### Energy weapons` with its sub-points
(against ships/colonies, against transports/assault craft, against missiles,
energy shields).

**Steps:**

1. `## Damage`: one-line lead-in. `### Energy weapons`: an `EWP` fires once per
   round at a ship/colony and fires at `MSS`/`TPT`/`ASC` when they attack; beam
   energy is `10 x TL`; each energy unit striking destroys one mass unit. Link
   `weapons.md#energy-weapons` for the unit stat.
2. Render the damage formula exactly:

   ```text
   ((F + D) x E) - SH = DA
   ```

   with the variable table (`F` weapons fired, `D` distance, `E` energy per
   weapon, `SH` shield deflection, `DA` damage in mass units). Include the
   manual's worked example (10,000 `TL1` `EWP` at `DF` 5, 1,000 `TL1` `ESH` →
   10,000 mass units), and the 75% (`MSL`/`EWP`/`SDRV`) / balance split for the
   damage applied. **Verify the example against the source's arithmetic and
   transcribe what the source states** (do not silently "correct" it).
3. Against transports and assault craft — render the fire/hit table exactly:

   | Target raided/invaded | `EWP` that fire | Beams that hit |
   | --------------------- | --------------- | -------------- |
   | Surface colony | 50% | 10% |
   | Orbiting colony | 75% | 20% |
   | Ship | 100% | 40% |

   A hit `ASC`/`TPT` is destroyed with all aboard.
4. Against missiles: all `EWP` fire; `25% + (5% x TL)` of beams hit; a hit `MSS`
   is destroyed.
5. Energy shields: an `ESH` deflects `10 x TL` energy units per round (the `SH`
   term). Link `weapons.md#energy-shields`.

**Acceptance criteria:**

- `((F + D) x E) - SH = DA` and the fire/hit table rendered exactly; `SH` tied to
  `ESH` deflection; worked example transcribed faithfully.
- Unit stats linked, not duplicated.

---

## Task 9 — Damage: missiles and anti-missiles

**Status:** TODO

**Scope:** add `### Missiles` (with missile-launcher accuracy) and
`### Anti-missiles` (against missiles; against transports/assault craft).

**Steps:**

1. `### Missiles`: launched by `MSL`, one `MSS` per `MSL` per round, only at ships
   and colonies. Render the hit formula exactly:

   ```text
   M / D² = H
   ```

   with the variable table (`M` missiles fired, `D` distance, `H` max hits), the
   manual's worked example (M=1,000, D=2 → 250 hits), and the rule that each hit
   does `100 x TL` mass-unit damage with the same 75% (`SDRV`/`MSL`/`EWP`) / 25%
   split. Note hits are reduced by `MSS` destroyed by `EWP` and `ANM`. State the
   missile-launcher accuracy rule: subtract the average `MSL` TL from `D²`,
   floored at `D² = 1`; `MSL` TL has no effect on `ANM`. Link
   `weapons.md#missiles` and `weapons.md#missile-launchers`.
2. `### Anti-missiles`: `ANM` destroy small fast targets (`MSS`, `TPT`, `ASC`);
   one `ANM` per `MSL` per attack; launching `ANM` does not inhibit `MSS`.
   - Against missiles: `50 + (TL x 5)`% hit; each hit destroys a `MSS` (example:
     300 `TL2` `ANM` → 60% → 180).
   - Against transports and assault craft: use the missile hit formula, ÷2 for
     `TPT` hit and ÷4 for `ASC` hit; `ASC` absorb hits first, overflow to `TPT`; a
     hit `ASC`/`TPT` is destroyed with all aboard.
   Link `weapons.md#anti-missiles`.

**Acceptance criteria:**

- `M / D² = H`, the launcher-accuracy `D²` adjustment (floor 1), and the `ANM`
  percentages/divisors rendered exactly, with the worked examples.
- Unit stats linked, not duplicated.

---

## Task 10 — Ship movement during combat; End of round

**Status:** TODO

**Scope:** add `## Ship movement during combat` and `## End of round`.

**Steps:**

1. `## Ship movement during combat`: ships move only under a bombard order; they
   move each round after weapons fire and casualties/damage are resolved; distance
   per round is set by speed; a bombarding ship is moved toward its target, a
   non-bombarding ship under attack is moved away. Replace the source's
   `(/docs/user-manuals/space-drives)` link with
   `{{< relref "ship-systems.md#space-drives" >}}`.
2. `## End of round`: combat continues another round if targets are not yet
   captured/destroyed and committed `SLD`/`FUEL`/`MTSP`/`MSS` remain; otherwise it
   stops.

**Acceptance criteria:**

- Both sections present; the broken absolute link is replaced with a working
  `relref` to `ship-systems.md#space-drives`.

---

## Task 11 — Surrender; Captured colonies; Combat and ship/colony TL

**Status:** TODO

**Scope:** add `## Surrender`, `## Captured colonies` (+ `### Captured population
units`), and `## Combat and ship or colony TL`.

**Steps:**

1. `## Surrender`: at 6:1 odds, invading or defending `SLD` surrender
   automatically and become `UEM` in the colony where they surrendered; `MRBT`
   fight until killed.
2. `## Captured colonies`: when a ship/colony's defenders are destroyed or have
   surrendered, it becomes the attacker's property **if** the attacker still has
   troops there. Add a `{{< callout type="warning" >}}` `TODO` noting that capture
   leads to *control of a planet*, covered in the not-yet-converted Control of
   Planets section (page-level mention; **no** link).
3. `### Captured population units`: on transfer, 50% of loyal population → rebels,
   50% of rebels → loyal, remaining soldiers disbanded → `UEM`; foreign-race
   population rebels at double rate. **Do not restate the rebellion mechanics** —
   link `rebellion.md#loyalty-on-capture` (which states exactly these rules) and
   keep this section to a brief pointer.
4. `## Combat and ship or colony TL`: a captured ship/colony drops one `TL`
   (floor `TL1`); a colony not captured but losing ≥20% population to bombardment
   or rebellion drops one `TL` (floor `TL1`). Link
   `technological-advancement.md` for what a `TL` is and
   `rebellion.md#when-rebellion-occurs` for the rebellion-driven 20% loss (which
   already states the TL drop).

**Acceptance criteria:**

- All three sections present; surrender 6:1 / `MRBT`-fight-on stated; capture
  ownership rule stated with a `warning` `TODO` for Control of Planets (no
  invented link).
- Captured-population rules link `rebellion.md#loyalty-on-capture` rather than
  restating them; TL-loss rules stated and linked.

---

## Task 12 — Wire the page into the site and apply weight

**Status:** TODO

**Scope:** make the page reachable and convert the Working-Index `11`/`11.x`
sub-tree to links/anchors. No new body content.

**Steps:**

1. **Working Index** in `content/_index.md`: replace every bare-text line from
   `11 - COMBAT` through `11.13 - Combat and Ship/Colony TL` with `relref` links
   into `combat.md` at the anchors fixed in the Page outline above. Map each
   Working-Index entry to its heading anchor:
   - `11` → `combat.md` (page top)
   - `11.1` → `#description`; `11.2` → `#military-supplies`;
     `11.3` → `#percentage-of-commitment`
   - `11.4` → `#attack`; `11.4.1` → `#attack-orders`;
     `11.4.2` → `#raids-and-invasions`; `11.4.2.1` → `#assault-craft`;
     `11.4.2.2` → `#assault-weapons`; `11.4.2.3` → `#transports`;
     `11.4.2.4` → `#military-robots`; `11.4.3` → `#bombardment`;
     `11.4.3.1` → `#bombardment-by-colonies`; `11.4.3.2` → `#bombardment-by-ships`
   - `11.5` → `#defense`; `11.5.1` → `#defense-against-soldier-units`;
     `11.5.2` → `#defense-against-bombardment`;
     `11.5.3` → `#defense-while-invading`; `11.5.4` → `#defense-against-raids`;
     `11.5.5` → `#defense-support`
   - `11.6` → `#combat-factor`
   - `11.7` → `#casualties`; `11.7.1` → `#invasion-casualties`;
     `11.7.2` → `#troop-transport-casualties`;
     `11.7.3` → `#bombardment-casualties`; `11.7.4` → `#raiding-casualties`
   - `11.8` → `#damage`; `11.8.1` → `#energy-weapons`;
     `11.8.1.1`–`11.8.1.5` → `#energy-weapons` (no separate sub-headings in our
     page — point them all at `#energy-weapons`); `11.8.2` → `#missiles`;
     `11.8.2.1` → `#missiles` (launcher accuracy lives under Missiles);
     `11.8.3` → `#anti-missiles`; `11.8.3.1`–`11.8.3.3` → `#anti-missiles`
   - `11.9` → `#ship-movement-during-combat`; `11.10` → `#end-of-round`;
     `11.11` → `#surrender`; `11.12` → `#captured-colonies`;
     `11.12.1` → `#captured-population-units`;
     `11.13` → `#combat-and-ship-or-colony-tl`

   (Where our page collapses several source sub-points into one section — the
   `11.8.1.x` energy-weapon points and the `11.8.3.x` anti-missile points — point
   the finer Working-Index lines at the containing anchor rather than inventing
   headings the page does not have.)
2. **Glossary** (`glossary.md`): add the alphabetical entries that do not yet
   exist, each linking the right `combat.md` anchor: **Bombard / bombardment**,
   **Combat**, **Combat factor**, **Commitment (percentage of commitment)**,
   **Distance factor (`DF`)**, **Invasion**, **Raid**, **Support order**,
   **Surrender**, **Captured colony / capture**. For terms already present
   (`Anti-missile`, `Assault craft`, `Assault weapon`, `Combat round`, `Energy
   weapon`, `Military robot`, `Military supplies`, `Missile`, `Missile launcher`,
   `Soldier`, `Space drive`, `Transport`, `Thrust factor`, `Weapon`), optionally
   add a secondary link to the relevant `combat.md` anchor where it clarifies the
   combat role — but do not duplicate the existing `weapons.md` stat links.
3. **Reciprocal links** where genuinely helpful: `weapons.md` and
   `ship-systems.md` currently say combat procedure belongs "with the combat
   reference material when that section is converted" — update those sentences to
   `relref` `combat.md` now that it exists (`weapons.md` intro/lead line;
   `ship-systems.md` Transports "Combat transport fuel use…" line and the
   Space Drives combat-movement context). `rebellion.md#loyalty-on-capture` may
   link back to `combat.md#captured-colonies`. Keep existing wording; add the
   `relref` only.

**Acceptance criteria:**

- `content/_index.md` has no bare `COMBAT` / `11.x` text; every line resolves via
  `relref` to a real `combat.md` anchor (or to the containing anchor for collapsed
  sub-points).
- New glossary entries exist and link correctly; no duplicate `weapons.md` stat
  links introduced.
- The two "when that section is converted" deferrals in `weapons.md` and
  `ship-systems.md` now link `combat.md`; any reciprocal links resolve and
  preserve host wording.

---

## Task 13 — Build, verify, and consistency pass

**Status:** TODO

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build with **no** `relref` "not found"
   errors and no duplicate-weight warnings.
2. Grep the new and changed pages for leftover Markdoc shortcodes (`{%`), the
   broken absolute link (`/docs/user-manuals/`), broken/relative Markdown links,
   and the string "Empyrean Challenge". All four `{% fnref %}`/`{% footnote %}`
   constructs from the source must be gone (folded into prose/callouts).
3. Confirm sidebar order: `combat` (120) sits after `rebellion` (110) and before
   the next converted reference page.
4. Confirm every `relref` in `combat.md` targets an existing file and anchor —
   `weapons.md#energy-weapons`, `#missiles`, `#anti-missiles`,
   `#energy-shields`, `#military-supplies`, `#assault-craft`, `#assault-weapons`,
   `#military-robots`, `#missile-launchers`; `ship-systems.md#space-drives`,
   `#transports`; `units.md#population-units`, `#differences-from-the-rule-book`;
   `population.md#population-classes`; `colonies-and-ships.md`;
   `rebellion.md#loyalty-on-capture`, `#when-rebellion-occurs`;
   `technological-advancement.md` — and that `writing-orders.md` is linked
   page-level only.
5. Confirm no link was invented to a non-existent Espionage or Control-of-Planets
   page; those remain page-level mentions / `warning` `TODO`s.
6. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed —
   no instructional "you should"), no engine code added, no duplication of the
   unit stats owned by `weapons.md`/`ship-systems.md` or the rebellion rules owned
   by `rebellion.md`.

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{%` shortcodes, no `/docs/user-manuals/` link, no "Empyrean Challenge", no
  broken links in any changed or new file.
- The page reads as authoritative reference and defers (via links) to the overlap
  pages for shared rules; sidebar order is correct.

---

## Out of scope

- Weapon and drive **unit stats** — mass, fuel, TL behavior — owned by
  `weapons.md` and `ship-systems.md`. This page links them and adds only combat
  procedure.
- Re-converting Rebellion (owned by `rebellion.md`) — link
  `#loyalty-on-capture` / `#when-rebellion-occurs` for captured-population and
  TL-loss-by-rebellion rules.
- Writing the Espionage (12) or Control of Planets (13) pages, or inventing links
  to them — page-level mentions / `warning` `TODO`s only.
- Writing the Writing Orders chapter (`writing-orders.md` is a stub — page-level
  link only).
- Any engine code, including the combat resolver (lives in the separate `pyre`
  repo).
- Editing `user-manual/combat.md` (sacred; typo fixes only, and none are required
  for this conversion).
</content>
</invoke>
