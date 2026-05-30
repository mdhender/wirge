---
title: Rebellion
weight: 110
---

Rebellion is the process by which a discontented population seizes a ship or
colony from its owner. Rebels accumulate as the standard of living falls; when
enough of them are willing to fight, the ship or colony revolts and becomes
independent.

For the standard-of-living factors that drive discontent — pay, rationing, and
starvation — see [Food]({{< relref "food.md" >}}). For the `RBL` cadre and how
rebels are tracked alongside the population classes, see
[Population]({{< relref "population.md" >}}).

## Rebels

A rebel (`RBL`) is a citizen within an existing population class who is willing
to rebel. Rebels are a **tally**, not a separate population class:

- Rebel counts are drawn from the existing population classes (`USK`, `PRO`,
  `SLD`, `UEM`); those people remain counted in their own classes.
- Rebels have no pay rate and no death rate of their own.
- Total population in census reports excludes cadres, including `RBL`, because
  those people are already counted within the population classes.
- Unlike `TRN`, `SPY`, and `CNW`, `RBL` is not detailed in the separate cadre
  turn-report chart.

{{< callout type="info" >}}
Rebel counts are never reported directly. A player learns the number of rebels —
and their population type — only by assigning a `SPY` to the ship or colony. See
[Learning rebel counts](#learning-rebel-counts).
{{< /callout >}}

## Rebel increase

`RBL` increases when the standard of living decreases — most commonly when the
general population is underpaid or underfed, and especially when starvation
occurs. A captured ship or colony also gains rebels at the moment of transfer
(see [Loyalty on capture](#loyalty-on-capture)).

## When rebellion occurs

| Factor | Rule |
| ------ | ---- |
| Rebel militia | 10% of all rebels are **rebel militia** — the share of rebels that will actively take up arms. |
| Revolt threshold | Rebellion occurs when loyal soldier units number no more than twice the rebel militia units (a ratio of 2:1 or less). Soldier units that are themselves rebels do not count toward the loyal total. |
| Outcome | A successful rebellion makes the ship or colony **independent** (see [Independent ships and colonies](#independent-ships-and-colonies)). |
| Technology loss | A colony that loses 20% or more of its population to rebellion drops one technological level, unless it is already at TL1. |

## Learning rebel counts

Because rebel counts are never reported directly, a player must station a `SPY`
to gather the information. The spy functions that bear on rebellion:

| Function | Effect |
| -------- | ------ |
| Rebel quantity and type | Reports the number of rebels on the player's own ship/colony and their population type. One spy unit is required per ship/colony. |
| Convert rebels | Converts the player's own rebels back to loyal population. Each spy unit converts one unit of rebels. |
| Incite rebellion | Converts loyal population in a foreign colony into rebels. Each spy unit converts one loyal population unit per turn. |

A `SPY` cadre is allocated from 1 `PRO` and 1 `SLD`; see
[Population]({{< relref "population.md#population-cadres" >}}).

## Loyalty on capture

When a captured ship or colony is transferred to its new owner (see
[Captured colonies]({{< relref "combat.md#captured-colonies" >}})):

- 50% of the loyal population units become rebels.
- 50% of all existing rebels convert to loyal population.
- Any remaining soldier units are disbanded and become `UEM`.

If the captured population is of a different race from the new owner's, it tends
to become rebels at **double** the normal rate.

## Independent ships and colonies

A ship or colony lost to rebellion becomes independent: it is no longer owned by
any player and runs under the same rules as player-controlled ships and
colonies.

- An independent **ship** supports itself by plundering ships, raiding colonies,
  or hiring out as a mercenary combat ship. It may establish an independent
  colony, but only on an uninhabited planet.
- An independent **colony** is based mainly on producing consumer goods and is
  generally — though not always — non-aggressive. If it accumulates excess
  population, it builds independent ships to remove them.

## Turn sequence

Within a turn, rebellion is resolved before new rebels accumulate: rebellion
occurs first, then rebel increases are calculated. Pay and ration orders take
effect just before this step, so the current turn's standard of living governs
both whether a revolt happens and how many new rebels appear.
