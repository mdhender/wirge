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
factory group from manufacturing to research. The order names the level to
research, `research-N`, where `N` is that level — for example,
`17, build change, research-2` sets the group to research level 2. The group
completes its [work in process]({{< relref "manufacturing.md#retooling" >}})
before beginning research.

A colony may research any level up to one above its current `TL`: a `TL-1`
colony may order `research-1` or `research-2`, but not `research-3`. Reaching a
higher level requires advancing one level at a time, or acquiring a higher-level
prototype by trade or [transfer](#technology-transfer).

A researching group manufactures research points at the ordered level
(`RSCH-N`), producing one `RSCH-N` per factory unit (`FACT`) × that factory
unit's `TL`, per year — paralleling manufacturing's `20 × TL`
mass-units-per-year
[throughput]({{< relref "manufacturing.md#factory-units-required" >}}). The
`RSCH-N` follow the normal manufacturing rules: the group delivers them to
[storage]({{< relref "mass.md#storage" >}}) once per year (every four turns),
and a [shortage]({{< relref "shortages.md" >}}) throttles and delays the
delivery. For when an annual figure lands, see
[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}).

`RSCH-N` accumulate in storage across years. When the stored quantity of
`RSCH-N` reaches the requirement for level `N` below, the engine removes that
quantity from storage and replaces it with a single `PRTO-N` — a prototype at
technological level `N`.

Each level requires the following `RSCH-N` to form its `PRTO-N`. The requirement
doubles at each level. `TL 1` is included for completeness.

| Level | `RSCH-N` required |
| ----- | ----------------- |
| 1     | 50,000            |
| 2     | 100,000           |
| 3     | 200,000           |
| 4     | 400,000           |
| 5     | 800,000           |
| 6     | 1,600,000         |
| 7     | 3,200,000         |
| 8     | 6,400,000         |
| 9     | 12,800,000        |
| 10    | 25,600,000        |

A `PRTO-N` is a storable, tradeable unit. Forming one does not by itself change
any `TL`; a separate upgrade order applies it.

## Upgrading

A colony applies a prototype with an **upgrade order**. Its general form is
`<colony>, upgrade, <target>, PRTO-N, <CNW>` — the issuing colony, the target
entity, the prototype level to apply, and the maximum
[construction workers]({{< relref "population.md#labor" >}}) (`CNW`) to allocate
to the work. The issuing colony holds the `PRTO-N` and consumes it on
completion; the prototype may have been [researched](#research) by that colony
or acquired by trade or [transfer](#technology-transfer).

The target may be the colony itself or another entity in the same orbit:

- `17, upgrade, 17, PRTO-3, 5000 CNW` — colony 17 upgrades itself.
- `17, upgrade, 99, PRTO-3, 5000 CNW` — colony 17 upgrades entity 99, a colony
  or ship in the same orbit. Only the `CNW` travel to the target, so colony 17
  needs enough [transports]({{< relref "ship-systems.md#transports" >}}) to
  carry them; the `PRTO-N` stays with colony 17. This is how a colony upgrades a
  ship that could not itself hold the prototype.

Only a colony issues an upgrade order. A ship cannot upgrade itself or another
entity, but a colony may upgrade a ship in its orbit.

The order requires `CNW` equal to the square of the difference between `N` and
the **target's** current `TL`, times the number of
[structural units]({{< relref "ship-systems.md#structural-units" >}}) (`STU`)
that form the target's hull. Upgrading a `TL-2` target of 5,000 `STU` to `TL 3`
with a `PRTO-3` requires (3 − 2)² × 5,000 = 5,000 `CNW`.

Like a [set up order]({{< relref "colonies-and-ships.md#establishment" >}}), an
upgrade accumulates this labor across turns when fewer `CNW` are allocated or
available than the work requires: the colony applies what it can each turn and
carries the remainder forward. An upgrade needing 5,000 `CNW` with 3,000 applied
per turn completes in two turns. The turn report lists the order under its
**Set up** section with the running totals.

A successful upgrade raises the target to `TL N`, and may skip levels: a target
at `TL 3` upgraded with a `PRTO-10` rises directly to `TL 10`. The order must
raise the target's `TL`: if `N` is at or below the target's current `TL`, the
engine refuses the order, consuming no prototype and claiming no `CNW`.

{{< callout type="warning" >}}
**TODO:** The rules for holding and moving a `PRTO` are still being settled. A
colony may hold a prototype of any level, but a ship may carry one only up to
its own `TL` (a raid can capture a higher one). Document the prototype's holding,
trade, and transfer limits with the Trade and Combat material once those pages
exist.
{{< /callout >}}

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
