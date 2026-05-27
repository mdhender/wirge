---
title: Farming
weight: 55
---

**Farming** produces [FOOD]({{< relref "units.md#resources" >}}), which feeds a
nation's population. A player groups [farm units]({{< relref "units.md#production" >}})
(`FARM`) in a colony — or, at the highest tech levels, a ship — and the group
delivers its harvest once a year.

## Farm groups

A **farm group** is a set of `FARM` units that produce FOOD together. A group may
contain farm units of **different technological levels** — for example, 100 `FARM-1`
and 50 `FARM-2` in the same group.

Each farm group tracks its units in four **quarter buckets** that record progress
toward the next harvest:

| Field          | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| `group_number` | Identifies the group within the colony.                           |
| `units`        | The `FARM` units in the group, by technological level.            |
| `quantity`     | The number of `FARM` units in the group, by technological level.  |
| `buckets`      | Four stages (q1–q4) tracking units' progress toward harvest.      |

{{< callout type="info" >}}
**Group number** is never reused.
{{< /callout >}}

## Harvest cycle

Farm units produce FOOD **once per year**, not every turn the way mines do. A unit's
growing FOOD climbs four quarter-stages while the unit stays supplied and is delivered
on the fourth. Because each turn's production is calculated before assembly orders are
processed, a unit does no work the turn it is assembled — it only joins the group. Its
first quarter of growth lands the next turn, so the first harvest arrives four turns
after assembly:

```
assembled → 25% → 50% → 75% → harvest (delivers FOOD, restarts)
```

Each supplied turn advances a unit one quarter. A unit that reaches the fourth quarter
delivers its full annual FOOD to storage that turn and immediately begins the next
year's growth. The buckets hold this work in process — the FOOD being grown — so a
group's units may sit in different buckets at once.

## Food output

Annual output per farm unit depends on its technological level. The harvest
delivers the **full annual amount at once**, not spread across the year.

| Tech level | Annual output (FOOD) | Fuel per turn |
| ---------- | -------------------- | ------------- |
| FARM-1     | 100                  | 0.5           |
| FARM-2     | 40                   | 1.0           |
| FARM-3     | 60                   | 1.5           |
| FARM-4     | 80                   | 2.0           |
| FARM-5     | 100                  | 2.5           |
| FARM-6     | 120                  | 6.0           |
| FARM-7     | 140                  | 7.0           |
| FARM-8     | 160                  | 8.0           |
| FARM-9     | 180                  | 9.0           |
| FARM-10    | 200                  | 10.0          |

Output is **20 × TL** food units a year, with one exception: `FARM-1` produces 100,
not 20. Fuel is **0.5 × TL** per turn through `FARM-5`, then jumps to **1 × TL** from
`FARM-6` up, because those farms run on artificial sunlight.

## Types and placement

Where a farm can operate depends on its technological level and the colony's type:

| Tech level         | Type                          | Where it can operate                                          |
| ------------------ | ----------------------------- | ------------------------------------------------------------- |
| FARM-1             | Open-air                      | Open-air colonies only, on habitable planets.                 |
| FARM-2 – FARM-5    | Hydroponic (solar)            | Enclosed and orbiting colonies, and surface colonies within orbits 1–5. |
| FARM-6 – FARM-10   | Hydroponic (artificial light) | Ships, and colonies beyond the fifth orbit.                   |

Only **open-air colonies** may use `FARM-1`. Enclosed and orbiting colonies must
farm with `FARM-2` through `FARM-10`.

The number of `FARM-1` units an open-air colony may place is capped by the planet's
[habitability number]({{< relref "habitability.md" >}}): HN × 100,000.

## Inputs

### Labor

Each FARM unit requires, regardless of group size:

- 3 unskilled worker units (`USK`), or the equivalent in
  [automation units]({{< relref "units.md#miscellaneous" >}}) (`AUT`), and
- 1 professional unit (`PRO`).

### Fuel

Each FARM unit consumes the fuel shown in the output table above. Fuel — like every
production input — is allocated to MINE and FARM units **before** FACT units, so a
shortage starves the FACT units first. See
[Shortages]({{< relref "shortages.md#allocation-priority" >}}) for the full rules.

{{< callout type="info" >}}
FARM units on **orbiting** colonies within the fifth orbit run on solar power and
require no fuel. Surface farms and farms beyond the fifth orbit always consume fuel.
{{< /callout >}}

## Harvest failure

If a farm group lacks enough fuel or labor when a bucket's units are due to advance,
that **harvest fails**: the affected units reset to 0% and begin the full one-year
cycle over again. If inputs are still short the next quarter, the clock resets again,
and so on until inputs are restored.

Because shortages reset only the affected units, a group that has weathered a
shortage can end up with its units scattered across different buckets, each on its
own harvest schedule. See [Shortages]({{< relref "shortages.md" >}}) for how the
engine chooses which units are fed when a group cannot run at full capacity.

{{< callout type="info" >}}
Farming's shortage rule is harsher than mining's. A short turn costs a MINE group
only that turn's output, but it throws a FARM group back to 0% and forfeits the
whole year's progress.
{{< /callout >}}
