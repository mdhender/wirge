---
title: Units
weight: 50
---

Every unit that may be held by a ship or colony in Epimethean Challenge. This
catalog gives the engine code, category, and a short description; detailed
formulas and constraints live on the linked reference pages.

A unit's TL determines its mass, cost, and effectiveness. The codes in the _Code_
column are the game engine's authoritative codes. Where they differ from the
original rule book or sample turn reports, see [Differences from the rule
book](#differences-from-the-rule-book).

## Basic units

These are the units that make up ships and colonies.

### Population units

These are the citizens of the nation. See
[Population]({{< relref "population.md" >}}) for definitions, pay, death rates,
population changes, population orders, and shipboard population rules.

Population classes:

| Code | Full name         | Notes | Detail |
| ---- | ----------------- | ----- | ------ |
| USK  | Unskilled Workers | Labor needing little training. | [Population]({{< relref "population.md#population-classes" >}}) |
| PRO  | Professionals     | Skilled labor requiring long apprenticeships. | [Population]({{< relref "population.md#population-classes" >}}) |
| SLD  | Soldiers          | All military personnel. | [Population]({{< relref "population.md#population-classes" >}}) |
| UEM  | Unemployables     | All other citizens. All birth increases enter here. | [Population]({{< relref "population.md#population-classes" >}}) |

Population cadres:

| Code | Full name            | Notes | Detail |
| ---- | -------------------- | ----- | ------ |
| TRN  | Trainees             | Allocation of USK being trained as professionals. | [Population]({{< relref "population.md#population-cadres" >}}) |
| SPY  | Spies                | Allocation of 1 PRO + 1 SLD. | [Population]({{< relref "population.md#population-cadres" >}}) |
| CNW  | Construction Workers | Allocation of 1 PRO + 1 USK. | [Population]({{< relref "population.md#population-cadres" >}}) |
| RBL  | Rebels               | A tally of population willing to rebel. | [Rebellion]({{< relref "rebellion.md" >}}) |

### Production

These are produced by FACT and may be traded. All carry a technological level.

| Code | Full name | Notes | Detail |
| ---- | --------- | ----- | ------ |
| MINE | Mines     | Extract resources from deposits. | [Mining]({{< relref "mining.md" >}}) |
| FACT | Factories | Manufacture units. | [Manufacturing]({{< relref "manufacturing.md" >}}); [Shortages]({{< relref "shortages.md" >}}) |
| FARM | Farms     | Produce food. | [Farming]({{< relref "farming.md" >}}) |

### Miscellaneous

These are produced by FACT and may be traded. All carry a technological level.
See [Ship Systems and Miscellaneous Units]({{< relref "ship-systems.md" >}})
for fuel use, mass formulas, capacity formulas, and operational constraints.

| Code | Full name        | Notes | Detail |
| ---- | ---------------- | ----- | ------ |
| AUT  | Automation       | Replace USK in FARM, MINE, and FACT. | [Automation]({{< relref "ship-systems.md#automation" >}}) |
| LSP  | Life Support     | Recycle air and water in ships and enclosed colonies. | [Life Support]({{< relref "ship-systems.md#life-support" >}}) |
| HDRV | Hyperdrives      | Propel ships through hyper-space. | [Hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}}) |
| SDRV | Space Drives     | Maintain orbit and maneuver in combat. | [Space Drives]({{< relref "ship-systems.md#space-drives" >}}) |
| SEN  | Sensors          | Report on systems, ships/colonies, and conduct probes. | [Sensors]({{< relref "ship-systems.md#sensors" >}}) |
| TPT  | Transports       | Move units between ships/colonies or assist in combat. | [Transports]({{< relref "ship-systems.md#transports" >}}) |
| STU  | Structural Units | Frame for ships and colonies. | [Structural Units]({{< relref "ship-systems.md#structural-units" >}}) |

### Weapons

These are produced by FACT and may be traded or consumed. All carry a technological level.
See [Weapons]({{< relref "weapons.md" >}}) for fuel use, mass formulas, TL
behavior, and stated combat applicability.

| Code | Full name         | Notes | Detail |
| ---- | ----------------- | ----- | ------ |
| ASW  | Assault Weapons   | Carried by SLD in surface combat. | [Weapons]({{< relref "weapons.md#assault-weapons" >}}) |
| ASC  | Assault Craft     | Land/space vehicles used to invade ships/colonies. | [Weapons]({{< relref "weapons.md#assault-craft" >}}) |
| MRBT | Military Robots   | Replace SLD units in combat. | [Weapons]({{< relref "weapons.md#military-robots" >}}) |
| MSS  | Missiles          | Indirect combat weapon. | [Weapons]({{< relref "weapons.md#missiles" >}}) |
| MSL  | Missile Launchers | Launch MSS and ANM. | [Weapons]({{< relref "weapons.md#missile-launchers" >}}) |
| ANM  | Anti-Missiles     | Destroy incoming MSS. | [Weapons]({{< relref "weapons.md#anti-missiles" >}}) |
| EWP  | Energy Weapons    | Line-of-sight combat weapon. | [Weapons]({{< relref "weapons.md#energy-weapons" >}}) |
| ESH  | Energy Shields    | Absorb EWP damage. | [Weapons]({{< relref "weapons.md#energy-shields" >}}) |
| MTSP | Military Supplies | SLD combat supplies. | [Weapons]({{< relref "weapons.md#military-supplies" >}}) |

### Prototypes

These may be traded or consumed and all carry a technological level. `RSCH` is
produced by FACT; `PRTO` is formed by the engine from accumulated `RSCH`.

| Code | Full name       | Notes | Detail |
| ---- | --------------- | ----- | ------ |
| RSCH | Research Points | Manufactured by a researching factory group; accumulates toward a prototype. | [Technological Advancement]({{< relref "technological-advancement.md#research" >}}) |
| PRTO | Prototype       | Formed from accumulated `RSCH`; consumed by a colony's upgrade order to raise a colony's or ship's `TL`. | [Technological Advancement]({{< relref "technological-advancement.md#upgrading" >}}) |

### Materials

These are produced by FACT and may be traded or consumed. None carry a technological level.

| Code | Full name      | Notes | Detail |
| ---- | -------------- | ----- | ------ |
| CNGD | Consumer Goods | Used to pay the population. | [Consumer Goods]({{< relref "ship-systems.md#consumer-goods" >}}) |

### Resources

These are farmed or mined, not produced by FACT. None carry a technological level.

| Code | Full name              | Source | Notes | Detail |
| ---- | ---------------------- | ------ | ----- | ------ |
| FOOD | Food                   | FARM   | Feeds the population. | [Food]({{< relref "food.md" >}}) |
| METS | Metallic Resources     | MINE   | Raw material consumed by factories to build units. | [Mining]({{< relref "mining.md" >}}) |
| NMTS | Non-Metallic Resources | MINE   | Raw material consumed by factories to build units. | [Mining]({{< relref "mining.md" >}}) |
| FUEL | Fuel                   | MINE   | Powers mines, farms, factories, engines, and combat. | [Mining]({{< relref "mining.md" >}}) |
| GOLD | Gold                   | MINE   | Currency used in the market and for wages. | [Mining]({{< relref "mining.md" >}}) |

## Entities

Entities are ships or colonies and are frequently called "S/C" units in reports and documentation.

| Code | Full Name       | LSP required? | FARM TL? | FACT allowed? | MINE allowed? | Notes                                       |
| ---- | --------------- | ------------- | -------- | ------------- | ------------- | ------------------------------------------- |
| SHIP | Ship            | yes           | TL 6-10  | no            | no            | Allowed to move between orbits and systems. |
| COPN | Open Air Colony | no            | TL 1-10  | yes           | yes           | Surface colony.                             |
| CENC | Enclosed Colony | yes           | TL 2-10  | yes           | yes           | Surface colony.                             |
| CORB | Orbital Colony  | yes           | TL 2-10  | yes           | no            | Allowed to build STU-2 units.               |

## Quantities represented

How many items each unit stands for. Most units represent a single item; the
exceptions are noted below.

| Code | Number of items per unit |
| ---- | ------------------------ |
| ANM | 1 |
| ASC | 1 |
| ASW | Enough to arm 1 `SLD` unit |
| AUT | Enough to replace 1 `USK` unit times its TL |
| CNGD | Indeterminate |
| ESH | 1 |
| EWP | 1 |
| FACT | 1 |
| FARM | 1 |
| HDRV | 1 |
| LSP | 1 |
| MINE | 1 |
| MRBT | 100 robots |
| MSL | 1 |
| MSS | 1 |
| MTSP | Enough for 1 `SLD` unit per combat round |
| SDRV | 1 |
| SEN | 1 |
| STU-1 | Houses 1 `MU` |
| STU-2 | Houses 1 `MU` |
| TPT | 1 |

Each natural-resource unit is 1 [mass unit]({{< relref "mass.md" >}}) (`MU`) of
that resource.

{{< callout type="info" >}}
The structural quantities follow the current one-`MU`-per-`STU` model. They will
change with the planned `STU-2` revision tracked in
[Manufacturing]({{< relref "manufacturing.md#build-costs" >}}).
{{< /callout >}}

## Differences from the rule book

The game engine's codes and technological levels depart from the original rule book and sample turn reports in a few places:

- **Codes.** The engine uses longer, more readable codes (for example `MINE`, `FACT`, and `FARM`) in place of the rule book's shorter forms (`MIN`, `FCT`, `FRM`).
- **Drive terminology and codes.** The original rule book calls `HDRV` units "hyper engines." The engine and published docs use "hyperdrive" and `HDRV`; they also use `SDRV` for space drives. These terms and codes intentionally depart from shorter rule-book-style abbreviations so they are harder to confuse with `SEN`.
- **Structural units.** The rule book used `STU` (or `STUN`) for the base structural unit and `STUL` for a lighter, stronger version; later rule books added `SSTL` for an even lighter version. The engine replaces these with technological levels: `STU-1` replaces `STU`, and `STU-2` replaces `STUL`.
- **Military supplies.** The rule book used `MTSP` with no TL, usable with any level of combat weapon. The engine adds a TL for consistency (`MTSP-1` replaces `MTSP`) but prohibits research to improve it.
- **Research points.** The rule book used `RSCH` with no TL, usable to pay for any level of technological advancement. The engine adds a TL for consistency (`RSCH-1` replaces `RSCH`) but prohibits [research]({{< relref "technological-advancement.md#research" >}}) to improve it.

{{< callout type="warning" >}}
**TODO:** A few classifications here are provisional and should be revisited:

- The _Prototypes_ category (RSCH and PRTO) is a placeholder. Revisit it when we design the Cargo section of the ship/colony turn reports; that work should clarify how RSCH, CNGD, and other factory output are grouped.
- GOLD is listed as a resource with a MINE source as a stopgap. The rule book gives GOLD no source; reclassify it once we settle how pay and trade work with CNGD.
{{< /callout >}}
