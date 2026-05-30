---
title: Espionage
weight: 130
---

A spy unit is the `SPY` cadre — one soldier unit (`SLD`) plus one professional
unit (`PRO`); for how the cadre is allocated, paid, and lost, see
[Population]({{< relref "population.md#population-cadres" >}}). A spy unit
performs one function per turn. To act on a ship or colony, the spy unit must be
**at** that ship or colony. Once ordered to perform a function, a spy unit
continues to perform it until ordered otherwise. For how spy functions are
ordered, see [Writing Orders]({{< relref "writing-orders.md" >}}).

Espionage results round all fractions **down**.

## Spy functions

A spy unit can perform one of six functions:

| Code | Action |
| ---- | ------ |
| `A` | Rebel Quantity and Type |
| `B` | Convert Rebels |
| `C` | Uncover Foreign Spy |
| `D` | Suppress Foreign Spy |
| `E` | Incite Rebellion |
| `F` | Obtain Secrets |

## Rebel quantity and type

Function `A` reports, to the spy unit's own nation, the number of rebels on its
ships and colonies and their population type. One spy unit is required per ship
or colony. For what a rebel is, see
[Rebellion]({{< relref "rebellion.md#rebels" >}}); for the rebellion-side view of
this and the other rebel-related functions, see
[Learning rebel counts]({{< relref "rebellion.md#learning-rebel-counts" >}}).

## Convert rebels

Function `B` converts the nation's own rebels to loyal population. Each spy unit
converts one unit of rebels. See
[Rebellion]({{< relref "rebellion.md#rebels" >}}).

## Uncover foreign spy

Function `C` discovers foreign spy operations on the nation's ships and colonies.
It reports the number of foreign spies and the name of the ship or colony from
which they originated. One spy unit is required per ship or colony.

## Suppress foreign spy

Function `D` suppresses foreign spy operations through assassination. For
attacking spies and the foreign spies they target:

- Attacking spies destroy a number of foreign spies equal to **3× the
  attackers' number**.
- The attackers lose **1/6 of the defenders' number**.

For example, 21 spies attacking 12 foreign spies lose 2 attacking spies and
destroy 7 foreign spies. Because espionage results round fractions down, a
partial loss is truncated to a whole spy unit.

{{< callout type="info" >}}
These quantities vary by as much as ±50% to account for the element of chance.
{{< /callout >}}

## Incite rebellion

Function `E` incites rebellion in a foreign colony. Each spy unit converts one
loyal population unit into a rebel unit per turn. For what rebellion does, see
[Rebellion]({{< relref "rebellion.md#when-rebellion-occurs" >}}).

## Obtain secrets

Function `F` obtains all or part of another nation's ship or colony report. One
line of the report is obtained per turn per spy unit.
