---
title: Units
weight: 10
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

These are the citizens of the empire.

| Full name            | Code | Notes                                                         |
| -------------------- | ---- | ------------------------------------------------------------- |
| Unemployables        | UEM  | Non-working population. All birth increases enter here.       |
| Unskilled Workers    | USK  | Labor needing little training.                                |
| Professionals        | PRO  | Skilled labor requiring long apprenticeships.                 |
| Trainees             | TRNE | Unskilled workers being trained as professionals.             |
| Soldiers             | SLD  | All military personnel.                                       |
| Spies                | SPY  | Cadre of 1 PRO + 1 SLD.                                       |
| Construction Workers | CNW  | Cadre of 1 PRO + 1 USK.                                       |
| Rebels               | RBL  | A tally of population willing to rebel, not a separate class. |

### Production

These are produced by FACT and may be traded. All carry a technological level.

| Full name | Code | Notes                            |
| --------- | ---- | -------------------------------- |
| Mines     | MINE | Extract resources from deposits. |
| Factories | FACT | Manufacture units.               |
| Farms     | FARM | Produce food.                    |

### Miscellaneous

These are produced by FACT and may be traded. All carry a technological level.

| Full name        | Code | Notes                                                  |
| ---------------- | ---- | ------------------------------------------------------ |
| Automation       | AUT  | Replace USK in FARM, MINE, and FACT.                   |
| Life Support     | LSP  | Recycle air and water in ships and enclosed colonies.  |
| Hyper Engines    | HPD  | Propel ships through hyper-space.                      |
| Space Drives     | SPD  | Maintain orbit and maneuver in combat.                 |
| Sensors          | SEN  | Report on systems, ships/colonies, and conduct probes. |
| Transports       | TPT  | Move units between ships/colonies or assist in combat. |
| Structural Units | STU  | Frame for ships and colonies.                          |

### Weapons

These are produced by FACT and may be traded or consumed. All carry a technological level.

| Full name         | Code | Notes                                              |
| ----------------- | ---- | -------------------------------------------------- |
| Assault Weapons   | ASW  | Carried by SLD in surface combat.                  |
| Assault Craft     | ASC  | Land/space vehicles used to invade ships/colonies. |
| Military Robots   | MRBT | Replace SLD units in combat.                       |
| Missiles          | MSS  | Indirect combat weapon.                            |
| Missile Launchers | MSL  | Launch MSS and ANM.                                |
| Anti-Missiles     | ANM  | Destroy incoming MSS.                              |
| Energy Weapons    | EWP  | Line of sight combat weapon.                       |
| Energy Shields    | ESH  | Absorb EWP damage.                                 |
| Military Supplies | MTSP | SLD combat supplies.                               |

### Prototypes

These are produced by FACT and may be traded or consumed. All carry a technological level.

| Full name       | Code | Notes                                      |
| --------------- | ---- | ------------------------------------------ |
| Research Points | RSCH | Used to pay for technological advancement. |

## Materials

These are produced by FACT and may be traded or consumed. None carry a technological level.

| Full name      | Code | Notes                       |
| -------------- | ---- | --------------------------- |
| Consumer Goods | CNGD | Used to pay the population. |

## Resources

These are farmed or mined, not produced by FACT. None carry a technological level.

| Full name              | Code | Source | Notes                                                |
| ---------------------- | ---- | ------ | ---------------------------------------------------- |
| Food                   | FOOD | FARM   | Feeds the population.                                |
| Metallic Resources     | METS | MINE   | Raw material consumed by factories to build units.   |
| Non-Metallic Resources | NMTS | MINE   | Raw material consumed by factories to build units.   |
| Fuel                   | FUEL | MINE   | Powers mines, farms, factories, engines, and combat. |
| Gold                   | GOLD | MINE   | Currency used in the market and for wages.           |

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
