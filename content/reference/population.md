---
title: Population
weight: 55
---

Population units represent the people held by a ship or colony. Population
classes represent 100 people. Population cadres are tracked separately from the
main classes, but they are not separate population classes. Census counts remain
in the main classes. Non-`RBL` cadre counts are detailed in a separate turn-report
chart; `RBL` is hidden unless discovered by a spy. Spy and construction-worker
cadres represent 200 people.

For FOOD consumption, rationing, morale, and starvation, see
[Food]({{< relref "food.md" >}}).

## Population Classes

| Code | Type | Definition | People per unit | Standard CNGD pay per turn | Non-combat death rate per turn |
| ---- | ---- | ---------- | ---------------- | -------------------------- | ------------------------------ |
| `USK` | Unskilled workers | Workers who do not require long apprenticeships or extensive training. | 100 | 0.125 | 0.0625% |
| `PRO` | Professionals | Workers who require long apprenticeships or extensive training. | 100 | 0.375 | 0.0625% |
| `SLD` | Soldiers | All military personnel. | 100 | 0.250 | 0.0625% |
| `UEM` | Unemployables | All other citizens. | 100 | 0.000 | 0.0625% |

{{< callout type="info" >}}
`POP` is a catch-all code for any population class (`USK`, `PRO`, `SLD`, or `UEM`), used where a rule applies regardless of class.
{{< /callout >}}

## Population Cadres

| Code | Type | Allocation basis | Population units per cadre |
| ---- | ---- | ---------------- | --------------------------- |
| `TRN` | Trainees | Allocated from `USK` while training to become `PRO`. | 1 USK |
| `SPY` | Spies | Allocated from 1 `PRO` and 1 `SLD`. | 1 PRO + 1 SLD |
| `CNW` | Construction workers | Allocated from 1 `PRO` and 1 `USK`. | 1 PRO + 1 USK |
| `RBL` | Rebels | A tally of citizens who are willing to rebel. | 1 |

{{< callout type="info" >}}
The number of `PRO`, `SLD`, and `USK` units assigned to non-`RBL` cadres can not exceed the total number of units in the ship/colony.
{{< /callout >}}

{{< callout type="info" >}}
Rebel counts are never reported directly. The engine tracks `RBL`, but a player learns the number of rebels — and their population type — only by assigning a `SPY` to that ship or colony. See [Rebellion]({{< relref "rebellion.md" >}}).
{{< /callout >}}

Players cannot set pay rates for cadres.

{{< callout type="info" >}}
The original rule book says pay rates for all population classes may be
adjusted. The engine applies player-set pay rates to population classes, while
cadre pay is derived from the classes allocated to the cadre.
{{< /callout >}}

Cadre counts are never included in population-class census totals. `TRN`, `SPY`,
and `CNW` are detailed in a separate turn-report chart; `RBL` is not reported
there.

| Cadre | Standard CNGD pay per turn | Non-combat death rate per turn |
| ----- | -------------------------- | ------------------------------ |
| `TRN` | Same as the underlying `USK` unit | Same as the underlying `USK` unit |
| `SPY` | 0.625 (0.375 + 0.250) | 0.0625% |
| `CNW` | 0.500 (0.375 + 0.125) | 0.0625% |
| `RBL` | N/A | N/A |

## Labor

Population supplies the labor that every process requires each turn —
[farming]({{< relref "farming.md" >}}),
[mining]({{< relref "mining.md" >}}),
[manufacturing]({{< relref "manufacturing.md" >}}),
[assembling]({{< relref "manufacturing.md#assembling" >}}),
[upgrading]({{< relref "technological-advancement.md#upgrading" >}}), combat, and
the rest. A process draws the labor it needs from the ship or colony's pool for
the turn and returns it to the pool at the end of the turn; labor is never
consumed. A process that cannot draw the labor it requires is throttled — see
[Shortages]({{< relref "shortages.md" >}}).

## Population Changes

| Change | Rule |
| ------ | ---- |
| Birth increase | Colonies (never ships) experience population growth between 0.25% and 2.5% of the total population (rounded down) per turn. Birth increases are added as `UEM` units.  |
| Birth increase factors | Birth increases are based on unpopulated habitable land and inversely on standard of living. |
| Unemployable maturation | On any turn when `UEM` is greater than 30% of total population, 2% of `UEM` (rounded down) become `USK`. |
| Professional training | Any number of `USK` may be trained as `TRN` on any turn. Each 100 `TRN` units require the services of 1 `PRO` unit. |
| Trainee graduation | 5% of all `TRN` (rounded down) graduate into `PRO` each turn. |
| Soldier retirement | 1.25% of all `SLD` (rounded up) retire as `PRO` each turn. |
| Drafting | `SLD` units may be created from `USK` units. The drafted amount may not exceed the current `SLD` count. |
| Disbanding | Any number of `SLD` may be disbanded on any turn. Disbanded soldiers become `USK`. |
| Spy assembly | `SPY` cadres may be assembled or disassembled on any turn. |
| Construction-worker assembly | `CNW` cadres may be assembled or disassembled on any turn. |
| Rebel increase | `RBL` increases when the standard of living decreases — e.g. when the population is underpaid, underfed, or starving. |

Total population in census reports excludes cadres because cadres are already counted within other population classes.
The hidden `RBL` tally does not affect `UEM` maturation.

## Orders

| Order | Population effect |
| ----- | ----------------- |
| `RATION` | Sets the FOOD ration for a ship or colony. Ration orders apply to the population as a whole, not to individual population types. See [Food]({{< relref "food.md#rations" >}}). |
| `PAY` | Sets population pay rates for a ship/colony. Pay rates remain in effect until changed. |
| `DRAFT` | Recruits `SLD` or `TRN` units. |
| `ASSEMBLY` | Creates or removes `SPY` and `CNW` cadre allocations. Assembly orders also have non-population uses. |

## Ships

Population units on ships follow these additional rules:

| Rule | Value |
| ---- | ----- |
| Population increase | No population increases occur on ships. |
| Crew wages | The crew of a ship consists entirely of `PRO` units. They are paid 0.01 `GOLD` per population unit per turn. |
| Soldier wages | All `SLD` units transported by or assigned to the ship are paid 0.005 `GOLD` per population unit per turn. This includes units that are assigned to a `SPY` cadre. |
| Transported units | `USK` and `UEM` that are transported as passengers or cargo receive no wages (`GOLD` or `CNGD`), but do receive FOOD. |
| Gold exchange | Ship wages received in `GOLD` are exchanged for `CNGD` when the ship reaches its home-planet market or a trade station. |
| Crew payment timing | A ship's crew is paid on any turn when the ship is at a colony owned by the ship owner, if that colony has enough `GOLD` on hand. |
