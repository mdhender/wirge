---
title: Manufacturing
weight: 70
---

Manufacturing is how a colony turns natural resources into finished units. Only
colonies operate [factory units]({{< relref "units.md#production" >}}) (`FACT`);
ships never manufacture. A factory group builds a single unit type, consuming
labor and materials each turn until the unit is complete.

## Factory groups

A factory group is formed by an [assembly order]({{< relref "writing-orders.md" >}})
and manufactures every unit **except** the natural resources (`METS`, `NMTS`,
`FUEL`, `GOLD`), `FOOD`, and population. A group produces one unit type at a time
and may contain factory units of different technological levels.

Manufacturing any unit takes one year — four turns. For how output advances
through the year and how a shortage delays delivery, see
[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}) and
[Work in process and timing]({{< relref "shortages.md#work-in-process-and-timing" >}}).

## Labor

A factory group consumes `PRO` and `USK` each turn in proportion to its factory
units. A larger group is more efficient and spends less labor per factory unit.

| Factory units in group | `PRO` per `FACT` | `USK` per `FACT` |
| ---------------------- | ---------------- | ---------------- |
| 1–4                    | 6                | 18               |
| 5–49                   | 5                | 15               |
| 50–499                 | 4                | 12               |
| 500–4,999              | 3                | 9                |
| 5,000–49,999           | 2                | 6                |
| 50,000+                | 1                | 3                |

[Automation units]({{< relref "ship-systems.md#automation" >}}) (`AUT`) may
replace the `USK` in this requirement.

## Build costs

Each output unit costs a fixed quantity of metallic (`METS`) and non-metallic
(`NMTS`) resources. Where a formula includes `TL`, it is the technological level
of the unit being built.

| Unit                       | `METS` per unit | `NMTS` per unit |
| -------------------------- | --------------- | --------------- |
| Assault weapon (`ASW`)     | 1 × TL          | 1 × TL          |
| Assault craft (`ASC`)      | 3 × TL          | 2 × TL          |
| Anti-missile (`ANM`)       | 2 × TL          | 2 × TL          |
| Automation (`AUT`)         | 2 × TL          | 2 × TL          |
| Consumer good (`CNGD`)     | 0.2             | 0.4             |
| Energy shield (`ESH`)      | 25 × TL         | 25 × TL         |
| Energy weapon (`EWP`)      | 5 × TL          | 5 × TL          |
| Factory (`FACT`)           | 8 + TL          | 4 + TL          |
| Farm (`FARM`)              | 4 + TL          | 2 + TL          |
| Hyperdrive (`HDRV`)        | 25 × TL         | 20 × TL         |
| Life support (`LSP`)       | 3 × TL          | 5 × TL          |
| Light structural (`STU-2`) | 0.01            | 0.04            |
| Military robot (`MRBT`)    | 10 + TL         | 10 + TL         |
| Military supplies (`MTSP`) | 0.02            | 0.02            |
| Mine (`MINE`)              | 5 + TL          | 5 + TL          |
| Missile (`MSS`)            | 2 × TL          | 2 × TL          |
| Missile launcher (`MSL`)   | 15 × TL         | 10 × TL         |
| Sensor (`SEN`)             | 999 + TL        | 1,999 + TL      |
| Space drive (`SDRV`)       | 15 × TL         | 10 × TL         |
| Structural (`STU-1`)       | 0.1             | 0.4             |
| Structural (`STU-2`)       | 0.01            | 0.04            |
| Transport (`TPT`)          | 3 × TL          | 1 × TL          |

`STU-2` is built only by orbiting colonies, which do not build `STU-1`; see
[Structural Units]({{< relref "ship-systems.md#structural-units" >}}).

## Factory units required

Each factory unit converts `20 × TL` mass units of natural resources per year. A
unit whose combined `METS` + `NMTS` cost exceeds a factory unit's yearly
throughput needs more than one factory unit to build within a year.

For example, a `TL-2` `HDRV` costs 90 resource units (50 `METS` + 40 `NMTS`). A
`TL-2` factory unit converts 40 mass units a year, so building one `TL-2` `HDRV`
in a year requires three `TL-2` factory units.

## Retooling

A [build change order]({{< relref "writing-orders.md" >}}) directs a factory
group to retool — to switch the unit type it produces. Retooling takes one turn
or more: any work in process must finish before the group retools. The turn
report states when the group is ready to begin producing the new unit.

## Assembling

[Assembly orders]({{< relref "writing-orders.md" >}}) form the `CNW` and `SPY`
[population cadres]({{< relref "population.md#population-cadres" >}}) and make
**operational** units functional. An operational unit must be assembled after it
is taken out of [storage]({{< relref "mass.md#storage" >}}) before it will
function. The operational units are `SDRV`, `SEN`, `AUT`, `LSP`, `EWP`, `ESH`,
`MINE`, `FACT`, `FARM`, `HDRV`, `STU-1`, `STU-2`, and `MSL`.

Assembling every 500 [mass units]({{< relref "mass.md" >}}) of an operational
unit requires one construction worker (`CNW`). Assembly orders also add `FACT` to
an existing factory group and `MINE` to an existing mine group.

## Dis-assembling

[Dis-assembly orders]({{< relref "writing-orders.md" >}}) reverse assembly.
Dis-assembling loses 10% of the units dis-assembled, except for `SPY` and `CNW`.
The number of construction workers required is the same as for assembly.
