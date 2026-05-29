---
title: Units
weight: 50
---

Every unit that may be held by a ship or colony in Epimethean Challenge, with its
code, whether it carries a technological level (TL), its category, and a short
description.

A unit's TL determines its mass, cost, and effectiveness. The codes in the _Code_
column are the game engine's authoritative codes. Where they differ from the
original rule book or sample turn reports, see [Differences from the rule
book](#differences-from-the-rule-book).

## Basic units

These are the units that make up ship/colonies.

### Population units

These are the citizens of the nation. See
[Population]({{< relref "population.md" >}}) for definitions, pay, death rates,
population changes, population orders, and shipboard population rules.

Population classes:

| Code | Full name         | Notes                                               |
| ---- | ----------------- | --------------------------------------------------- |
| USK  | Unskilled Workers | Labor needing little training.                      |
| PRO  | Professionals     | Skilled labor requiring long apprenticeships.       |
| SLD  | Soldiers          | All military personnel.                             |
| UEM  | Unemployables     | All other citizens. All birth increases enter here. |

Population cadres:

| Code | Full name            | Notes                                                         |
| ---- | -------------------- | ------------------------------------------------------------- |
| TRN  | Trainees             | Allocation of USK being trained as professionals.             |
| SPY  | Spies                | Allocation of 1 PRO + 1 SLD.                                  |
| CNW  | Construction Workers | Allocation of 1 PRO + 1 USK.                                  |
| RBL  | Rebels               | A tally of population willing to rebel.                       |

### Production

These are produced by FACT and may be traded. All carry a technological level.

| Code | Full name | Notes                            |
| ---- | --------- | -------------------------------- |
| MINE | Mines     | Extract resources from deposits. |
| FACT | Factories | Manufacture units.               |
| FARM | Farms     | Produce food.                    |

### Miscellaneous

These are produced by FACT and may be traded. All carry a technological level.
See [Ship Systems and Miscellaneous Units]({{< relref "ship-systems.md" >}})
for fuel use, mass formulas, capacity formulas, and operational constraints.

| Code | Full name        | Notes                                                  |
| ---- | ---------------- | ------------------------------------------------------ |
| AUT  | Automation       | Replace USK in FARM, MINE, and FACT.                   |
| LSP  | Life Support     | Recycle air and water in ships and enclosed colonies.  |
| HEN  | Hyper Engines    | Propel ships through hyper-space.                      |
| SPD  | Space Drives     | Maintain orbit and maneuver in combat.                 |
| SEN  | Sensors          | Report on systems, ships/colonies, and conduct probes. |
| TPT  | Transports       | Move units between ships/colonies or assist in combat. |
| STU  | Structural Units | Frame for ships and colonies.                          |

### Weapons

These are produced by FACT and may be traded or consumed. All carry a technological level.
See [Weapons]({{< relref "weapons.md" >}}) for fuel use, mass formulas, TL
behavior, and stated combat applicability.

| Code | Full name         | Notes                                              |
| ---- | ----------------- | -------------------------------------------------- |
| ASW  | Assault Weapons   | Carried by SLD in surface combat.                  |
| ASC  | Assault Craft     | Land/space vehicles used to invade ships/colonies. |
| MRBT | Military Robots   | Replace SLD units in combat.                       |
| MSS  | Missiles          | Indirect combat weapon.                            |
| MSL  | Missile Launchers | Launch MSS and ANM.                                |
| ANM  | Anti-Missiles     | Destroy incoming MSS.                              |
| EWP  | Energy Weapons    | Line of sight combat weapon.                       |
| ESH  | Energy Shields    | Absorb EWP damage.                                 |
| MTSP | Military Supplies | SLD combat supplies.                               |

### Prototypes

These are produced by FACT and may be traded or consumed. All carry a technological level.

| Code | Full name       | Notes                                      |
| ---- | --------------- | ------------------------------------------ |
| RSCH | Research Points | Used to pay for technological advancement. |

### Materials

These are produced by FACT and may be traded or consumed. None carry a technological level.

| Code | Full name      | Notes                       |
| ---- | -------------- | --------------------------- |
| CNGD | Consumer Goods | Used to pay the population. |

### Resources

These are farmed or mined, not produced by FACT. None carry a technological level.

| Code | Full name              | Source | Notes                                                |
| ---- | ---------------------- | ------ | ---------------------------------------------------- |
| FOOD | Food                   | FARM   | Feeds the population.                                |
| METS | Metallic Resources     | MINE   | Raw material consumed by factories to build units.   |
| NMTS | Non-Metallic Resources | MINE   | Raw material consumed by factories to build units.   |
| FUEL | Fuel                   | MINE   | Powers mines, farms, factories, engines, and combat. |
| GOLD | Gold                   | MINE   | Currency used in the market and for wages.           |

## Entities

Entities are ships or colonies and are frequently called "S/C" units in reports and documentation.

| Code | Full Name       | LSP required? | FARM TL? | FACT allowed? | MINE allowed? | Notes                                       |
| ---- | --------------- | ------------- | -------- | ------------- | ------------- | ------------------------------------------- |
| SHIP | Ship            | yes           | TL 6-10  | no            | no            | Allowed to move between orbits and systems. |
| COPN | Open Air Colony | no            | TL 1-10  | yes           | yes           | Surface colony.                             |
| CENC | Enclosed Colony | yes           | TL 2-10  | yes           | yes           | Surface colony.                             |
| CORB | Orbital Colony  | yes           | TL 2-10  | yes           | no            | Allowed to build STU-2 units.               |

## Differences from the rule book

The game engine's codes and technological levels depart from the original rule book and sample turn reports in a few places:

- **Codes.** The engine uses longer, more readable codes (for example `MINE`, `FACT`, and `FARM`) in place of the rule book's shorter forms (`MIN`, `FCT`, `FRM`).
- **Structural units.** The rule book used `STU` (or `STUN`) for the base structural unit and `STUL` for a lighter, stronger version; later rule books added `SSTL` for an even lighter version. The engine replaces these with technological levels: `STU-1` replaces `STU`, and `STU-2` replaces `STUL`.
- **Military supplies.** The rule book used `MTSP` with no TL, usable with any level of combat weapon. The engine adds a TL for consistency (`MTSP-1` replaces `MTSP`) but prohibits research to improve it.
- **Research points.** The rule book used `RSCH` with no TL, usable to pay for any level of technological advancement. The engine adds a TL for consistency (`RSCH-1` replaces `RSCH`) but prohibits research to improve it.

{{< callout type="warning" >}}
**TODO:** A few classifications here are provisional and should be revisited:

- The _Prototypes_ category (currently only RSCH) is a placeholder. Revisit it when we design the Cargo section of the ship/colony turn reports; that work should clarify how RSCH, CNGD, and other factory output are grouped.
- GOLD is listed as a resource with a MINE source as a stopgap. The rule book gives GOLD no source; reclassify it once we settle how pay and trade work with CNGD.
{{< /callout >}}
