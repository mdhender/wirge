---
title: Technological Advancement
weight: 80
---

Home colonies (nations) start at `TL 1` and advance through the technological
levels in consecutive order. A colony's `TL` caps the highest-`TL` unit its
[factories]({{< relref "manufacturing.md" >}}) can build: a level-5 colony builds
`TL 1`–`TL 5` units. A factory's **own** `TL` governs only its
[output rate]({{< relref "manufacturing.md#factory-units-required" >}}), not the
`TL` of what it builds. Once a unit is manufactured, its `TL` is fixed and cannot
change. For what `TL` does to a unit's mass, cost, and effectiveness, see
[Units]({{< relref "units.md" >}}).

A ship or colony's `TL` is raised in three ways: research, technology transfer,
and buying technology.

## Research

A [build change order]({{< relref "manufacturing.md#retooling" >}}) switches a
factory group from manufacturing to research. The group completes its
[work in process]({{< relref "manufacturing.md#retooling" >}}) before beginning
research.

A researching group produces one research point (`RSCH`) per factory unit
(`FACT`) × that factory unit's `TL`, per year — paralleling manufacturing's
`20 × TL` mass-units-per-year
[throughput]({{< relref "manufacturing.md#factory-units-required" >}}). For when an
annual figure lands, see
[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}).

Each level requires the following `RSCH`. The cost doubles at each level. `TL 1`
has no row — nations begin there.

| Level | `RSCH` required |
| ----- | --------------- |
| 2     | 100,000         |
| 3     | 200,000         |
| 4     | 400,000         |
| 5     | 800,000         |
| 6     | 1,600,000       |
| 7     | 3,200,000       |
| 8     | 6,400,000       |
| 9     | 12,800,000      |
| 10    | 25,600,000      |

## Technology transfer

An established ship or colony has the same `TL` as the ship or colony that
established it. The [set up order]({{< relref "colonies-and-ships.md#establishment" >}})
is the mechanism; the new entity inherits the establisher's `TL`.

More than one level transfers at once: a `TL 2` colony can receive levels 3
through 6 and rise to `TL 6`.

A ship transfers only levels up to its own `TL`. To transfer level 6, the ship
must itself be `TL 6`.

## Buying technology

`TL` can be bought at a market or trade station, through the
[market order]({{< relref "writing-orders.md" >}}).

{{< callout type="warning" >}}
**TODO:** The Trade reference page (markets and trade stations) is not yet
converted. Link the market and trade-station detail here once it exists.
{{< /callout >}}
