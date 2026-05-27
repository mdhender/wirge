---
title: Food
---

## Rations

A **full ration** (`Rf`) of FOOD is 0.25 units per population unit per turn. This is the default value for every new ship/colony.

Players can set the **actual ration** (`Ra`) for a ship/colony by issuing a `RATION` order.

Rations are always divided equally amongst the population.
A player is not allowed to issue an order targeting a specific population type (e.g., `SLD` cannot be set to 100% rations while `UEM` receive 50%).

Population units that don't receive their full ration of FOOD may suffer two effects:

- Morale decline
- Starvation

## Shortages

A ship/colony suffers an **unplanned shortage** when it does not have enough FOOD on hand to serve its current ration. When that happens, `Ra` is recalculated for that turn as the FOOD available divided by the FOOD required:

```
Ra = FOOD available / FOOD required
```

**Example.** A ship/colony has `Ra` set to 100% and needs 500 FOOD, but only 200 FOOD is available. Its `Ra` falls to 40% (200 / 500) for that turn.

The recalculated `Ra` lasts for that turn only; the next turn returns to the ration set by the most recent `RATION` order. Both Morale and Starvation use this recalculated `Ra`. An unplanned shortage also raises the survival ration — see [Starvation](#starvation).

## Morale

Morale declines when `Ra` is less than 100%.

{{< callout type="warning" >}}
TODO: Document how SOL (Standard of Living) is impacted by changes to morale.
{{< /callout >}}

{{< callout type="warning" >}}
TODO: Morale declines **every time** rations are reduced and increases only when rations are restored to 100%. The increase **does not** offset the decrease. It's possible, in theory, to bribe the population by increasing rations to over 100%.
{{< /callout >}}

## Starvation

Every population unit needs a **survival ration** (`Rs`) of 25% per turn — one-quarter of a full ration — to avoid starvation.

If `Ra` is at least `Rs`, no one starves, even on reduced rations.

If `Ra` falls below `Rs`, a percentage of the population starves to death. The percentage lost equals the size of the shortfall measured against the survival ration:

```
P = max(Rs − Ra, 0) / Rs
```

{{< callout type="info" >}}
Percentages enter the formulas as their decimal equivalents: 25% is 0.25, 20% is 0.20, and so on.
{{< /callout >}}

where:

- **P** is the percentage of the population that starves,
- **Rs** is the survival ration, and
- **Ra** is the actual ration per population unit.

The wider the gap between the actual ration and the survival ration, the larger the share of the population that dies. At `Ra` = 0, the entire population starves (`P` = 1).

**Example.** A player sets the ration to 20% (`Ra` = 20%), which is below `Rs`:

```
P = max(Rs − Ra, 0) / Rs
  = (0.25 − 0.20) / 0.25
  = 0.05 / 0.25
  = 0.20
```

20% of the population starves that turn.

During an unplanned shortage (see [Shortages](#shortages)), the survival ration rises from 25% to 35% for that turn. Distributing emergency stockpiles without coordination wastes some of the available FOOD, so each population unit needs more FOOD to survive than usual. This bump applies only to Starvation; Morale uses the recalculated `Ra` unchanged.

A player who anticipates the shortage and lowers the ration ahead of time with a `RATION` order makes the cut **planned**: the survival ration stays at 25%, so fewer population units are lost than if the same `Ra` had been forced by an unplanned shortage.

**Example.** Continuing the shortage above, `Ra` is recalculated to 40% while `Rs` is raised to 35%. Because `Ra` still clears the raised survival ration, no one starves:

```
P = max(Rs − Ra, 0) / Rs
  = max(0.35 − 0.40, 0) / 0.35
  = 0 / 0.35
  = 0
```

Had the shortage been deeper — only 150 FOOD available, giving `Ra` = 30% — the raised survival ration would put part of the population at risk:

```
P = max(Rs − Ra, 0) / Rs
  = max(0.35 − 0.30, 0) / 0.35
  = 0.05 / 0.35
  ≈ 0.143
```

When calculating the number of population units lost to starvation, round the results up. For example, 20% of 500 POP would be 100 `POP`. 20% of 6 `POP` would be 2 `POP`.
