---
title: Weapons
weight: 56
---

Weapons are combat units held by a ship or colony. The codes below are the game
engine's authoritative unit codes; where those codes or technological-level rules
differ from the original rule book, see
[Differences from the rule book]({{< relref "units.md#differences-from-the-rule-book" >}}).

This page describes weapon units only. Combat procedure belongs with the combat
reference material when that section is converted.

## Weapons Chart

| Code | Unit | Combat applicability | TL behavior | Fuel use per unit | Mass per unit |
| ---- | ---- | -------------------- | ----------- | ----------------- | ------------- |
| `ASW` | Assault weapons | Used by `SLD` units on a planet's surface. | No TL-based behavior stated in the Basic Units chart. | 0 | 20 MU |
| `ASC` | Assault craft | Land/space vehicles used to invade colonies or ships. | TL sets unit mass. | 0.1 FUEL per turn | 5 x TL MU |
| `MRBT` | Military robots | Replace `SLD` units in combat, but cannot replace the `SLD` unit assigned to a `SPY` cadre. | Each unit can replace `TL x 2` `SLD` units. | 0 | `(2 x TL) + 20` MU |
| `MSS` | Missiles | Usable in any kind of combat; less accurate than energy weapons. | TL sets unit mass. | 0 | 4 x TL MU |
| `MSL` | Missile launchers | Launch `MSS` and `ANM`. | The accuracy of an `MSS` depends on the TL of the `MSL` that launches it. | 0 | 25 x TL MU |
| `ANM` | Anti-missiles | Destroy incoming `MSS`; launched by `MSL`. | The percentage of attacking missiles destroyed depends on the TL of the `ANM`. | 0 | 4 x TL MU |
| `EWP` | Energy weapons | Usable in all combat situations except surface-colony-to-surface-colony combat. | Projects a concentrated energy beam; TL sets fuel use and mass. | 4 x TL FUEL per combat round | 10 x TL MU |
| `ESH` | Energy shields | Deflect energy beams. | The amount of energy deflected depends on shield TL per combat round. | 10 x TL FUEL | 50 x TL MU |
| `MTSP` | Military supplies | Ammunition, medicines, and other supplies consumed during combat. | The original rule book gives `MTSP` no TL. The engine stores military supplies as `MTSP-1` only. | 0 | 0.04 MU |

## Assault Weapons

`ASW` units are used by soldiers on the surface of a planet. They have fixed mass
and no fuel use.

| Field | Value |
| ----- | ----- |
| Code | `ASW` |
| Full name | Assault weapons |
| Fuel use | 0 |
| Mass | 20 MU |

## Assault Craft

`ASC` units are land/space vehicles used to invade colonies or ships. Their mass
scales with TL.

| Field | Value |
| ----- | ----- |
| Code | `ASC` |
| Full name | Assault craft |
| Fuel use | 0.1 FUEL per turn |
| Mass | 5 x TL MU |

## Military Robots

`MRBT` units replace soldiers in combat. A military robot cannot replace the
soldier assigned to a `SPY` cadre.

| Field | Value |
| ----- | ----- |
| Code | `MRBT` |
| Full name | Military robots |
| Soldier replacement | TL x 2 `SLD` units per `MRBT` unit |
| Fuel use | 0 |
| Mass | `(2 x TL) + 20` MU |

## Missiles

`MSS` units are usable in any kind of combat. They are less accurate than energy
weapons.

| Field | Value |
| ----- | ----- |
| Code | `MSS` |
| Full name | Missiles |
| Fuel use | 0 |
| Mass | 4 x TL MU |

## Missile Launchers

`MSL` units launch missiles and anti-missiles. Missile accuracy depends on the TL
of the missile launcher.

| Field | Value |
| ----- | ----- |
| Code | `MSL` |
| Full name | Missile launchers |
| Launches | `MSS`, `ANM` |
| TL effect | Determines missile accuracy |
| Fuel use | 0 |
| Mass | 25 x TL MU |

## Anti-Missiles

`ANM` units destroy attacking missiles and are launched by missile launchers. The
percentage of missiles destroyed depends on the TL of the anti-missile.

| Field | Value |
| ----- | ----- |
| Code | `ANM` |
| Full name | Anti-missiles |
| Launched by | `MSL` |
| TL effect | Determines the percentage of attacking `MSS` destroyed |
| Fuel use | 0 |
| Mass | 4 x TL MU |

## Energy Weapons

`EWP` units project concentrated energy beams. They are usable in all combat
situations except combat from one surface colony to another surface colony.

| Field | Value |
| ----- | ----- |
| Code | `EWP` |
| Full name | Energy weapons |
| Exclusion | Surface-colony-to-surface-colony combat |
| Fuel use | 4 x TL FUEL per combat round |
| Mass | 10 x TL MU |

## Energy Shields

`ESH` units deflect energy beams. The amount of energy deflected depends on the
shield TL per combat round.

| Field | Value |
| ----- | ----- |
| Code | `ESH` |
| Full name | Energy shields |
| Fuel use | 10 x TL FUEL |
| Mass | 50 x TL MU |

## Military Supplies

`MTSP` units are ammunition, medicines, and similar supplies consumed during
combat.

| Field | Value |
| ----- | ----- |
| Code | `MTSP` |
| Full name | Military supplies |
| Fuel use | 0 |
| Mass | 0.04 MU |

