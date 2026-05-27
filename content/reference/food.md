---
title: Food
weight: 65
---

## Rations

A **full ration** (`Rf`) of FOOD is 0.25 units per population unit per turn.
This is the default ration for every new ship or colony.

Players may set the **actual ration** (`Ra`) for a ship or colony by issuing a
`RATION` order.

Rations are divided equally amongst the population. A player may not issue a
ration order targeting a specific population type. For example, `SLD` may not
receive 100% rations while `UEM` receive 50%.

Population units receiving less than a full ration are subject to:

- Morale decline
- Starvation

## Shortages

A ship or colony suffers an **unplanned shortage** when insufficient FOOD is
available to satisfy the current ration.

During an unplanned shortage, the actual ration (`Ra`) is recalculated for that
turn as:

```text
Ra = Fa / Fr
```

where:

- `Ra` is the actual ration served that turn,
- `Fa` is the FOOD available, and
- `Fr` is the FOOD required to satisfy a full ration.

**Example.** A ship or colony has `Ra` set to 100% and requires 500 FOOD for a full ration, but
only 200 FOOD is available:

```text
Ra = Fa / Fr
   = 200 / 500
   = 0.40
```

The actual ration for that turn becomes 40%.

The recalculated `Ra` applies only for the current turn. On the following turn,
the ration returns to the value established by the most recent `RATION` order.

Both Morale and Starvation calculations use the recalculated `Ra`.

An unplanned shortage also increases the survival ration used for Starvation
calculations. See [Starvation](#starvation).

## Morale

Morale declines whenever `Ra` is less than 100%.

{{< callout type="warning" >}}
TODO: Document how SOL (Standard of Living) is impacted by changes to morale.
{{< /callout >}}

{{< callout type="warning" >}}
TODO: Morale declines every time rations are reduced and increases only when
rations are restored to 100%. The increase does not offset the decrease.
{{< /callout >}}

{{< callout type="warning" >}}
TODO: Document whether rations above 100% can increase morale.
{{< /callout >}}

## Starvation

Every population unit requires a **survival ration** (`Rs`) of 25% per turn to
avoid starvation.

```text
Rs = 0.25
```

If `Ra` is greater than or equal to `Rs`, no population units starve.

If `Ra` is less than `Rs`, part of the population starves. The percentage of the
population lost is calculated as:

```text
P = max(Rs − Ra, 0) / Rs
```

where:

- `P` is the percentage of the population that starves,
- `Rs` is the survival ration, and
- `Ra` is the actual ration served.

{{< callout type="info" >}}
Percentages enter formulas as decimal values. For example:

- 25% = 0.25
- 20% = 0.20
- 100% = 1.00
{{< /callout >}}

The larger the gap between `Ra` and `Rs`, the greater the percentage of the
population that starves. If `Ra = 0`, the entire population starves (`P = 1`).

**Example.** A ship or colony sets `Ra = 20%`:

```text
P = max(Rs − Ra, 0) / Rs
  = max(0.25 − 0.20, 0) / 0.25
  = 0.05 / 0.25
  = 0.20
```

20% of the population starves that turn.

### Unplanned shortages

During an unplanned shortage, the survival ration increases from 25% to 35% for
that turn only.

```text
Rs = 0.35
```

This modifier applies only to Starvation calculations. Morale calculations use
the recalculated `Ra` unchanged.

If a ration reduction is issued through a `RATION` order before the shortage
occurs, the shortage is considered **planned**. Planned shortages do not modify
`Rs`; the survival ration remains 25%.

**Example.** A shortage recalculates `Ra` to 40% while `Rs` is raised to 35%:

```text
P = max(Rs − Ra, 0) / Rs
  = max(0.35 − 0.40, 0) / 0.35
  = 0 / 0.35
  = 0
```

No population units starve.

**Example.** A deeper shortage recalculates `Ra` to 30% while `Rs = 35%`:

```text
P = max(Rs − Ra, 0) / Rs
  = max(0.35 − 0.30, 0) / 0.35
  = 0.05 / 0.35
  ≈ 0.143
```

Approximately 14.3% of the population starves.

## Rounding

When calculating the number of population units lost to starvation, fractional
results are always rounded upward.

Examples:

- 20% of 500 `POP` = 100 `POP`
- 20% of 6 `POP` = 2 `POP`
