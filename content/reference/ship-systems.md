---
title: Ship Systems and Miscellaneous Units
weight: 57
---

Miscellaneous units are manufactured units that support production, population
pay, movement, detection, transfer, and construction. Most carry a technological
level (TL). Consumer goods do not.

For the full unit catalog and code differences from the original rule book, see
[Units]({{< relref "units.md" >}}).

## Summary

| Code | Unit | Primary role | Fuel use | Mass per unit |
| ---- | ---- | ------------ | -------- | ------------- |
| `AUT` | Automation | Replaces `USK` labor in `FARM`, `MINE`, and `FACT` production. | 0 | 4 x TL MU |
| `CNGD` | Consumer goods | Pays colony population. | 0 | 0.6 MU |
| `LSP` | Life support | Supports population in ships, enclosed colonies, and orbiting colonies. | TL FUEL per turn | 8 x TL MU |
| `HDRV` | Hyperdrive | Moves ships through hyper-space. | 40 FUEL x distance jumped per operating hyperdrive | 45 x TL MU |
| `SDRV` | Space drive | Maintains ship orbit and maneuvers in combat. | TL^2 FUEL per combat round | 25 x TL MU |
| `SEN` | Sensor | Reports systems, ships, colonies, and probes planets. | TL / 20 FUEL per turn | 2,998 + (2 x TL) MU |
| `TPT` | Transport | Transfers population and material at a planet; carries soldiers in combat. | TL^2 / 10 FUEL per turn, proportional to capacity used | 4 x TL MU |
| `STU` | Structural unit | Provides the frame for ships and colonies. | 0 | 0.5 MU for `STU-1`; 0.05 MU for `STU-2` |

## Automation

`AUT` units replace unskilled-worker labor for production units. They apply to:

- [Farms]({{< relref "farming.md#inputs" >}})
- [Mines]({{< relref "mining.md#inputs" >}})
- [Factory units]({{< relref "units.md#production" >}})

One automation unit replaces unskilled-worker units equal to its TL:

```text
USK replaced = AUT units x TL
```

For example, 20 `AUT-4` units replace 80 `USK` units.

| Field | Value |
| ----- | ----- |
| Code | `AUT` |
| Full name | Automation |
| Labor replaced | TL `USK` units per `AUT` unit |
| Fuel use | 0 |
| Mass | 4 x TL MU |

## Consumer Goods

`CNGD` units are factory output used to pay colony population. Standard colony
pay rates by population class are listed in
[Population]({{< relref "population.md#population-classes" >}}).
For factory production context, see
[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}).

| Field | Value |
| ----- | ----- |
| Code | `CNGD` |
| Full name | Consumer goods |
| Produced by | `FACT` units |
| Used for | Population pay |
| Fuel use | 0 |
| Mass | 0.6 MU |

Food is a separate resource. For rations, consumption, morale, and starvation,
see [Food]({{< relref "food.md" >}}).

## Life Support

`LSP` units recycle air and water. They are required by ships, enclosed colonies,
and orbiting colonies. Open-air colonies do not require life support.

Population capacity is the unit's TL squared:

```text
POP capacity = TL^2
```

For example, one `LSP-5` supports 25 population units.

| Field | Value |
| ----- | ----- |
| Code | `LSP` |
| Full name | Life support |
| Required by | `SHIP`, `CENC`, `CORB` |
| Capacity | TL^2 population units |
| Fuel use | TL FUEL per turn |
| Mass | 8 x TL MU |

## Hyperdrives

`HDRV` units propel ships through hyper-space, both within a solar system and
between solar systems. They are used only by ships.

| Field | Value |
| ----- | ----- |
| Code | `HDRV` |
| Full name | Hyperdrive |
| Jump range | TL light years |
| Propulsion capacity | 1,000 x TL MU per hyperdrive |
| Fuel use | 40 FUEL x distance jumped per operating hyperdrive |
| Mass | 45 x TL MU |

A ship may carry any number of hyperdrives. All hyperdrives on a ship should
be the same TL. If a ship has mixed-TL hyperdrives, the lowest TL sets the
ship's jump range.

When a ship jumps, only the number of hyperdrives required by the ship's mass
operate and consume fuel. The mass of the ship's hyperdrives is excluded when
calculating how many engines are required.

```text
hyperdrives required = ceiling(non-HDRV ship mass / (1,000 x hyperdrive TL))
```

For jump distance:

| Jump type | Distance |
| --------- | -------- |
| Interplanetary | Always 0.1 light years |
| Interstellar | Distance from the player's Star List |

Every jump must end at an interplanetary or interstellar location. A jump cannot
end in deep space.

## Space Drives

`SDRV` units maintain a ship's orbit around a planet and maneuver the ship in
combat. Every ship must have at least one space drive. A ship's space drives do
not have to share the same TL.

Space drives use anti-gravity generators and operate only close to a planet.
They cannot be used for interplanetary or interstellar travel.

| Field | Value |
| ----- | ----- |
| Code | `SDRV` |
| Full name | Space drive |
| Ship requirement | At least 1 per ship |
| Fuel use | TL^2 FUEL per combat round |
| Thrust factor | TL^2 x 1,000 |
| Combat movement | Total thrust factor / ship mass |
| Mass | 25 x TL MU |

Space-drive fuel is consumed only during combat.

## Sensors

`SEN` units report system, ship, colony, and planet information.

| Field | Value |
| ----- | ----- |
| Code | `SEN` |
| Full name | Sensor |
| Fuel use | TL / 20 FUEL per turn |
| Mass | 2,998 + (2 x TL) MU |
| Probe rate | TL planet probes per turn |

When a ship enters a solar system, its sensors automatically report:

- The number of planets in the system
- Each planet's type
- Each planet's orbit position

Sensors also automatically report orbital information to a ship or colony:

| Reported object | Sensor report |
| --------------- | ------------- |
| Ships in orbit | Number of ships and approximate mass of each ship |
| Colonies in orbit | Number of colonies, approximate mass of each colony, and approximate number of production units per colony |

Sensors can also conduct planet probes. A sensor unit conducts probes equal to
its TL each turn. For probe contents, see
[Probes]({{< relref "exploration.md#probes" >}}).

## Transports

`TPT` units move population and materials between ships, colonies, or ships and
colonies at the same planet. They can also carry soldiers into battle.

| Field | Value |
| ----- | ----- |
| Code | `TPT` |
| Full name | Transport |
| Transfer capacity | TL^2 x 200 MU per turn |
| Non-combat operators | 1 `PRO` unit per 10 `TPT` units |
| Combat operators | The soldiers being transported |
| Fuel use | TL^2 / 10 FUEL per turn, proportional to capacity used |
| Mass | 4 x TL MU |

The proportional fuel rule applies to non-combat transfer use. A transport group
using half of its transfer capacity uses half of its non-combat fuel.

"Material" includes:

- Resources
- Basic units other than population
- Research points
- Technological levels

Transports never transfer more population or material to a ship or colony than
its life support units or structural limits can support.

Combat transport fuel use belongs with the combat reference material when that
section is converted.

## Structural Units

`STU` units are required to build ships and colonies.

| Code | Rule-book unit | Role | Mass per unit | Manufacturing restriction |
| ---- | -------------- | ---- | ------------- | ------------------------- |
| `STU-1` | Structural unit | Standard frame for ships and colonies. | 0.5 MU | No Basic Units restriction stated. |
| `STU-2` | Light structural unit | May substitute for `STU-1` without exception. | 0.05 MU | Built only by orbiting colonies. |

Light structural units require the absence of gravity for manufacture. They are
cheaper to build and lighter than standard structural units.

{{< callout type="info" >}}
The original rule book distinguishes structural and light structural units by
name. The engine represents that distinction with TL: `STU-1` is the standard
structural unit, and `STU-2` is the light structural unit. See
[Differences from the rule book]({{< relref "units.md#differences-from-the-rule-book" >}}).
{{< /callout >}}
