---
title: Population
weight: 55
---

Population units represent the people held by a ship or colony. Population
classes represent 100 people. Population cadres are tracked separately from the
main classes, but they are not separate population classes. Census counts remain
in the main classes; cadre counts show where those citizens are allocated. Spy
and construction-worker cadres represent 200 people.

For FOOD consumption, rationing, morale, and starvation, see
[Food]({{< relref "food.md" >}}).

## Population Classes

| Code | Type | Definition | People per unit | Standard CNGD pay per turn | Non-combat death rate per turn |
| ---- | ---- | ---------- | ---------------- | -------------------------- | ------------------------------ |
| `USK` | Unskilled workers | Workers who do not require long apprenticeships or extensive training. | 100 | 0.125 | 0.0625% |
| `PRO` | Professionals | Workers who require long apprenticeships or extensive training. | 100 | 0.375 | 0.0625% |
| `SLD` | Soldiers | All military personnel. | 100 | 0.250 | 0.0625% |
| `UEM` | Unemployables | All other citizens not represented by the working or soldier classes. All birth increases enter this type. | 100 | 0.000 | 0.0625% |

## Population Cadres

| Code | Type | Allocation basis | People represented per unit |
| ---- | ---- | ---------------- | --------------------------- |
| `TRN` | Trainees | Allocated from `USK` while training to become `PRO`. | 100 USK |
| `SPY` | Spies | Allocated from 1 `PRO` and 1 `SLD`; reports on other players and incites rebellion. | 100 PRO + 100 SLD |
| `CNW` | Construction workers | Allocated from 1 `PRO` and 1 `USK`; executes assembly and dis-assembly orders. | 100 PRO + 100 USK |
| `RBL` | Rebels | A tally of citizens in other population segments who are willing to rebel. | 100 |

{{< callout type="info" >}}
The number of `PRO`, `SLD`, and `USK` units assigned to cadres can not exceed the total number of units in the ship/colony.
{{< /callout >}}

Players cannot set pay rates for cadre because cadres are not an actual population
class and are already included in other population segments.

Cadre allocation does not reduce the census count of the underlying population
classes. For example, a population with 100 `PRO`, 200 `USK`, and 50 `SLD` may
also report 50 `CNW` and 50 `SPY`; the census still shows 100 `PRO`, 200 `USK`,
and 50 `SLD`, with the cadre counts showing where those citizens are allocated.

## Population Changes

| Change | Rule |
| ------ | ---- |
| Birth increase | Colonies (never ships) experience population grown between 0.25% and 2.5% of the total population (rounded down) per turn. Birth increases are added as `UEM` units.  |
| Birth increase factors | Birth increases are based on unpopulated habitable land and inversely on standard of living. |
| Unemployable maturation | On any turn when `UEM` is greater than 30% of total population, 2% of `UEM` (rounded down) become `USK`. |
| Professional training | Any number of `USK` may be trained as `TRN` on any turn. Each 100 `TRN` units require the services of 1 `PRO` unit. |
| Trainee graduation | 5% of all `TRN` (rounded down) graduate into `PRO` each turn. |
| Soldier retirement | 1.25% of all `SLD` (rounded up) retire as `PRO` each turn. |
| Drafting | `SLD` may be drafted from `USK` on any turn, as long as the drafted number does not exceed the number of `SLD` at the time of the draft. |
| Disbanding | Any number of `SLD` may be disbanded on any turn. Disbanded soldiers become `USK`. |
| Spy assembly | A `SPY` unit may be assembled or disassembled on any turn. |
| Construction-worker assembly | A `CNW` unit may be assembled or disassembled on any turn. |
| Rebel increase | `RBL` increases when the standard of living decreases, the general population is underpaid or underfed, and especially when starvation occurs. |

Total population in census reports excludes cadres because cadres are already counted within other population segments.

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
