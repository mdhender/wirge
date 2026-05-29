---
title: Technological Advancement
weight: 80
---

Home colonies (nations) start at `TL-1` and advance through the technological
levels in consecutive order. A colony's `TL` caps the highest-`TL` unit its
[factories]({{< relref "manufacturing.md" >}}) can build: a level-5 colony builds
`TL 1`–`TL 5` units. A factory's **own** `TL` governs only its
[output rate]({{< relref "manufacturing.md#factory-units-required" >}}), not the
`TL` of what it builds. Once a unit is manufactured, its `TL` is fixed and cannot
change. For what `TL` does to a unit's mass, cost, and effectiveness, see
[Units]({{< relref "units.md" >}}).

A nation raises the `TL` of a ship or colony by applying a prototype unit (`PRTO`) with an
upgrade order. A prototype is obtained by research, technology transfer, or
purchase.

## Research

A [build change order]({{< relref "manufacturing.md#retooling" >}}) switches a
factory group from manufacturing to research. The order names the level to
research, `RSCH-TL`, where `TL` is that level — for example,
`17, build change, RSCH-2` sets the group to research tech level 2. The group
completes its [work in process]({{< relref "manufacturing.md#retooling" >}})
before beginning research.

A colony may research any level up to one above its current `TL`: a `TL-1`
colony may order `RSCH-1` or `RSCH-2`, but not `RSCH-3`. Reaching a
higher level requires advancing one level at a time, or acquiring a higher-level
prototype by [transfer](#technology-transfer) or [purchase](#buying-technology).

A researching group manufactures research points at the ordered level
(`RSCH-TL`), producing one `RSCH-TL` per factory unit (`FACT`) × that factory
unit's `TL`, per year. The
`RSCH` follow the normal manufacturing rules: the group delivers them to
[storage]({{< relref "mass.md#storage" >}}) once per year (every four turns),
and a [shortage]({{< relref "shortages.md" >}}) throttles and delays the
delivery. For when an annual figure lands, see
[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}).

`RSCH` accumulate in storage across years. When the stored quantity of
`RSCH-TL` reaches the requirement for a tech level as given below, the engine
removes that quantity from storage and replaces it with a single `PRTO-TL` — a prototype at
technological level `TL`.

Each level requires the following `RSCH-TL` to form its `PRTO-TL`. The requirement
doubles at each level.

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

A `PRTO` is a storable, tradeable unit. Forming one does not by itself change
any `TL`; a separate upgrade order applies it.

## Upgrading

A colony applies a prototype with an **upgrade order**. Its general form is
`<colony>, upgrade, <target>, PRTO-TL, <CNW>` — the issuing colony, the target
entity, the prototype level to apply, and the maximum
[construction workers]({{< relref "population.md#labor" >}}) (`CNW`) to allocate
to the work. The issuing colony holds the `PRTO` and consumes it on
completion; the prototype may have been [researched](#research) by that colony,
or acquired by [transfer](#technology-transfer) or [purchase](#buying-technology).

The target may be the colony itself or another entity in the same orbit:

- `17, upgrade, 17, PRTO-3, 5000 CNW` — colony 17 upgrades itself.
- `17, upgrade, 99, PRTO-3, 5000 CNW` — colony 17 upgrades entity 99, a colony
  or ship in the same orbit. Only the `CNW` travel to the target, so colony 17
  needs enough [transports]({{< relref "ship-systems.md#transports" >}}) to
  carry them.

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

A successful upgrade raises the target to `TL-N`, and may skip levels: a target
at `TL-3` upgraded with a `PRTO-10` rises directly to `TL-10`. The order must
raise the target's `TL`: if `N` is at or below the target's current `TL`, the
engine refuses the order, consuming no prototype and claiming no `CNW`.

## Technology transfer

An established ship or colony has the same `TL` as the ship or colony that
established it.

Technology also moves as a [prototype](#research): a `PRTO` transferred from
one entity to another. A colony accepts a `PRTO` of any level. A ship accepts
a transfer of a `PRTO` no more than one level above its own `TL`: a `TL-4`
ship accepts a transfer of a `PRTO-5` but no higher.

A raid captures a `PRTO` of any level: a ship may carry a prototype it has
captured above the level it could accept by transfer. When a raided `PRTO`
exceeds that level, the raid order governs the outcome.

{{< callout type="warning" >}}
**TODO:** The raid order is documented with the Combat material once that page
exists. Link the raid detail here then, including the chance that a raid destroys
the captured `PRTO` rather than seizing it.
{{< /callout >}}

## Buying technology

A `PRTO` can be bought at a market or trade station, through the
[market order]({{< relref "writing-orders.md" >}}). Like a researched or
transferred prototype, a purchased `PRTO` raises no `TL` on its own; a separate
[upgrade order](#upgrading) applies it, and the buyer holds it under the same
limits as any other prototype.

{{< callout type="warning" >}}
**TODO:** The Trade reference page (markets and trade stations) is not yet
converted. Link the market and trade-station detail here once it exists.
{{< /callout >}}
