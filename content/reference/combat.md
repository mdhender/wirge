---
title: Combat
weight: 120
---

## Description

Combat occurs when a nation orders an attack by its ships or colonies against
another nation's ships or colonies. The attacking and target
[ships or colonies]({{< relref "colonies-and-ships.md" >}}) must be at the same
orbit within the same system.

Combat runs in rounds. The number of rounds is indefinite: it is bounded by the
time taken to complete the mission or by the exhaustion of the attack's troops,
`FUEL`, missiles, and `MTSP`. A raid is the exception — it lasts one round.

{{< callout type="warning" >}}
TODO: Document the rounding rules for combat results. The formulas on this page
(combat factors, casualties, missile hits, and damage) can produce fractional
values, and how each result is rounded to whole units is not yet specified.
{{< /callout >}}

## Military supplies

`MTSP` is the ammunition, supplies, and other consumables expended during
combat. One `MTSP` is consumed per `SLD` unit per combat round. For the unit
stat, see [Weapons]({{< relref "weapons.md#military-supplies" >}}).

## Percentage of commitment

Every combat order carries a percentage of commitment — the share of a unit a
nation commits to the attack. For invasion and raid orders, the commitment
applies to `SLD` and `MRBT`. For bombard orders, it applies to `FUEL` (for
`EWP`) and to missiles. Units not committed remain with the ship or colony for
its defense.

## Attack

All combat orders are executed simultaneously. A ship or colony may be given
only one combat order per turn. The order syntax is covered in
[Writing Orders]({{< relref "writing-orders.md" >}}).

### Attack orders

There are four types of attack order:

- **Raid** — a ship or colony steals one type of unit from another ship or
  colony. Any type of unit may be stolen, including population units.
- **Invasion** — a ship or colony invades another ship or colony to capture it.
- **Bombard** — a ship or colony uses `MSS` and `EWP` against another ship or
  colony to destroy it.
- **Support** — assists another nation in an invasion and serves in defense (see
  [Defense support](#defense-support)). The supporting and supported nations do
  not attack each other and fight as one unit.

{{< callout type="info" >}}
An invasion of a ship can be considered a boarding party.
{{< /callout >}}

### Raids and invasions

In round one of a raid or invasion, the committed troops are armed and sent into
battle. Committed troops are assigned first to `ASC`. Troops that overflow the
available `ASC` are placed in `TPT` and armed with `ASW`. Troops left with
neither `ASC` nor `TPT` remain with the uncommitted `SLD`. Uncommitted troops
stay with the ship or colony for its defense.

#### Assault craft

`ASC` transport `SLD`. Each `ASC` requires one `SLD` to operate it, and one
`SLD` is the maximum it holds. For the unit stat, see
[Weapons]({{< relref "weapons.md#assault-craft" >}}).

#### Assault weapons

Each `ASW` requires one `SLD` to operate it. An `ASW` is destroyed when the
`SLD` operating it is destroyed. For the unit stat, see
[Weapons]({{< relref "weapons.md#assault-weapons" >}}).

#### Transports

`TPT` carry `SLD` to battle. In combat, a `TPT` consumes `0.01 x TL²` `FUEL`
per round trip, and its carrying capacity is `3 x TL` mass units per combat
round. These combat figures differ from the transfer figures, which are given in
[Ship Systems]({{< relref "ship-systems.md#transports" >}}).

#### Military robots

`MRBT` replace `SLD`, functioning as soldiers in all ways except that they are
quicker, stronger, and harder to kill. Each `MRBT` replaces `TL x 2` `SLD`. The
percentage of commitment applies to `MRBT`. For the unit stat, see
[Weapons]({{< relref "weapons.md#military-robots" >}}).

### Bombardment

#### Bombardment by colonies

Colonies bombard ships or other colonies with `MSS` or `EWP`, with one
exception: because `EWP` operate on direct line-of-sight, a surface colony
cannot use `EWP` against another surface colony.

The distance factor (`DF`), used by colonies only, is:

| Attacker | Defender | Distance factor (`DF`) |
| -------- | -------- | ---------------------- |
| Surface colony | Surface colony | 1 |
| Surface colony | Orbiting colony | 2 |
| Orbiting colony | Orbiting colony | 3 |

`DF` stands in for the ship distance `D` used in the damage formulas under
[Damage](#damage).

#### Bombardment by ships

A ship's distance from the planet it orbits, the orbiting colony, or the target
ship is a random number from `1` to `100`, in increments of 10,000 miles. A ship
cannot fire `MSS` or `EWP` until it is within range `10` (100,000 miles) of the
target.

## Defense

A ship or colony automatically defends itself against raids, invasions, and
bombardments.

### Defense against soldier units

The defending ship or colony's `EWP` and `ANM` fire on the `ASC` and `TPT`
carrying the attacking soldiers. After the attackers reach the surface, the
attacking `ASC` are met by the defender's `ASC`, and the troops carried in `TPT`
are met by the defender's uncommitted `SLD`. The defender fires `MSS` and `EWP`
at the attacking ship or colony.

{{< callout type="info" >}}
A surface colony cannot fire `EWP` at another surface colony. If an attack is
made by two or more nations, only one nation's ships or colonies are fired upon.
{{< /callout >}}

### Defense against bombardment

A defending ship or colony fires `ANM` at incoming `MSS`, raises `ESH` to
deflect the attacker's `EWP` beams, and fires `EWP` and `MSS` back at the
attacking ship or colony.

{{< callout type="info" >}}
If an attack is made by two or more nations, only one nation's ships or colonies
are fired upon.
{{< /callout >}}

### Defense while invading

If a ship or colony is itself attacked while in the process of invading, its
`SLD` return home — unless the invasion has already succeeded, in which case
only half return and the original order is aborted.

### Defense against raids

Defense against a raid is the same as defense against soldier units, except that
a raid lasts one round.

### Defense support

A support order may assist another nation in the defense of its ship or colony
(see [Attack orders](#attack-orders)). If a supporting ship or colony is itself
invaded, its `SLD` return home. The order syntax is covered in
[Writing Orders]({{< relref "writing-orders.md" >}}).

## Combat factor

Combat factors determine the casualties in raids and invasions. Each unit used
in a raid or invasion is assigned a combat factor:

| Unit | Combat factor |
| ---- | ------------- |
| `ASC` | `10 x TL` |
| `ASW` | `2 x TL` |
| `SLD` | 1 |
| `MRBT` | `2 x TL` |

A force's combat factor is the sum of each soldier's basic factor and its
weapon's factor. For example, a force of 5,000 `SLD` armed with `TL1` `ASW` and
5,000 `SLD` armed with `TL1` `ASC` has a total combat factor of 70,000.

## Casualties

### Invasion casualties

Combat losses for an invasion are:

```text
((A / D) x R₁) x D = DL
((D / A) x R₂) x A = AL
```

| Variable | Value |
| -------- | ----- |
| `A` | the attacker's combat factors |
| `D` | the defender's combat factors |
| `DL` | the defender's losses |
| `AL` | the attacker's losses |
| `R₁` | a random number from 0.1 to 0.5 (the element of chance) |
| `R₂` | a random number from 0.1 to 0.5 (the element of chance) |

For example, with an attacker combat factor of 500 and a defender combat factor
of 100: `((500 / 100) x 0.3) x 100 = 150` combat factors lost by the defender,
and `((100 / 500) x 0.5) x 500 = 50` combat factors lost by the attacker.

The percentage of `SLD` and weapon units lost equals the percentage of combat
factors lost. In the example, the attacker loses 10% of its `SLD`, `ASC`, and
`ASW`; the defender loses all of its units.

Of all casualties, 70% are killed in action and removed from play; the remaining
30% are wounded and added to the ship or colony's `UEM`. For the `UEM` class,
see [Population]({{< relref "population.md#population-classes" >}}) and
[Units]({{< relref "units.md#population-units" >}}).

### Troop transport casualties

This applies to `SLD` in `TPT` and `ASC` while moving to the target ship or
colony. An `ASC` or `TPT` hit by an energy beam or `ANM` is destroyed with all
aboard.

### Bombardment casualties

75% of the hits on a ship or colony strike `EWP`, `MSL`, and `SDRV`; the other
25% strike other parts and may include population units. The computer randomly
selects which units are hit.

### Raiding casualties

Raiding casualties, for both attacker and defender, are the invasion casualty
formula result multiplied by 0.01.

## Damage

Damage is the mass-unit destruction done by `EWP`, `MSS`, and `ANM` to ships and
colonies and to the small craft that carry attacking troops.

### Energy weapons

An `EWP` fires once per round at a ship or colony, and fires at `MSS`, `TPT`, and
`ASC` whenever they attack. Each beam delivers `10 x TL` energy units, and each
energy unit that strikes destroys one mass unit. For the unit stat, see
[Weapons]({{< relref "weapons.md#energy-weapons" >}}).

Damage against a ship or colony is:

```text
((F / D) x E) - SH = DA
```

| Variable | Value |
| -------- | ----- |
| `F` | the number of energy weapons fired |
| `D` | the distance |
| `E` | the energy delivered by each weapon |
| `SH` | the shields' ability to deflect energy beams |
| `DA` | the damage in mass units |

For example, a ship fires 10,000 `TL1` `EWP` at a colony 5 distance units away,
and the colony has 1,000 `TL1` `ESH`: `((10,000 / 5) x 10) - 10,000 = 10,000`
mass units of damage. Of that damage, 75% is applied to `MSL`, `EWP`, and `SDRV`
(a colony has no `SDRV`); the balance affects other parts of the target,
including population units.

{{< callout type="warning" >}}
**Differs from the rule book.** The original rule book prints this term as
`(F + D)`, but its own worked example divides — `((10,000 / 5) x 10) - 10,000` —
so the printed sum is a typo. We use the division form `(F / D)`, which the
example confirms and which correctly attenuates a beam over distance (a more
distant target, larger `D`, takes less damage). This is the formula the engine
implements.
{{< /callout >}}

Against transports and assault craft, the share of `EWP` that fire and the share
of beams that hit depend on the target:

| Target raided or invaded | `EWP` that fire | Beams that hit |
| ------------------------ | --------------- | -------------- |
| Surface colony | 50% | 10% |
| Orbiting colony | 75% | 20% |
| Ship | 100% | 40% |

An `ASC` or `TPT` hit by an energy beam is destroyed with all aboard.

Against missiles, all `EWP` fire, and `25% + (5% x TL)` of the beams hit. A `MSS`
hit by a beam is destroyed.

**Energy shields.** An `ESH` deflects `10 x TL` energy units per round — the `SH`
term in the damage formula. For the unit stat, see
[Weapons]({{< relref "weapons.md#energy-shields" >}}).

### Missiles

`MSS` are launched by `MSL`, one `MSS` per `MSL` per round, and only at ships and
colonies. The possible hits are:

```text
M / D² = H
```

| Variable | Value |
| -------- | ----- |
| `M` | the number of missiles fired |
| `D` | the distance |
| `H` | maximum possible hits |

For example, 1,000 `MSS` fired at a target 2 distance factors away:
`H = 1,000 / 2² = 1,000 / 4 = 250` hits. The number of hits is reduced by the
`MSS` destroyed by `EWP` and `ANM`.

Each hit does `100 x TL` mass units of damage. Of that damage, 75% is applied to
`SDRV`, `MSL`, and `EWP`; the other 25% affects other units, including
population units.

The TL of a `MSL` affects the accuracy of the `MSS` it fires: subtract the
average `MSL` TL of the firing ship or colony from `D²` in the formula above. If
this would make `D²` less than 1, `D²` remains 1. `MSL` TL has no effect on
`ANM`. For the unit stats, see
[Weapons]({{< relref "weapons.md#missiles" >}}) and
[Missile Launchers]({{< relref "weapons.md#missile-launchers" >}}).

### Anti-missiles

`ANM` destroy small, fast-moving targets: `MSS`, `TPT`, and `ASC`. They are
launched by `MSL`, one `ANM` per `MSL` per attack. Launching `ANM` does not
inhibit the launching of `MSS`. For the unit stat, see
[Weapons]({{< relref "weapons.md#anti-missiles" >}}).

Against missiles, `50 + (TL x 5)`% of `ANM` hit, and each hit destroys a `MSS`.
For example, of 300 `TL2` `ANM`, 60% — or 180 — destroy missiles.

Against transports and assault craft, the number hit is found from the missile
hit formula above, divided by 2 for `TPT` and divided by 4 for `ASC`. `ASC`
absorb hits first; once they are all destroyed, the remaining hits are applied to
`TPT`. An `ASC` or `TPT` hit by an `ANM` is destroyed with all aboard.

## Ship movement during combat

A ship moves during combat only under a bombard order. Movement happens each
round after all weapons have fired and casualties and damage have been resolved.
The distance moved per round is set by the ship's speed (see
[Ship Systems]({{< relref "ship-systems.md#space-drives" >}})). A bombarding ship
is moved toward its target; a non-bombarding ship under attack is moved away from
its attacker.

## End of round

Combat continues for another round if the attackers have not yet captured or
destroyed their assigned targets and still have committed `SLD`, `FUEL`, `MTSP`,
and `MSS` remaining. Combat stops once the mission is fulfilled or the committed
`SLD`, `FUEL`, `MTSP`, or `MSS` are exhausted.

## Surrender

When invading or defending `SLD` face odds of six to one, they surrender
automatically and become `UEM` in the colony where they surrendered. `MRBT` fight
until killed.

## Captured colonies

When the defending soldiers of a ship or colony have been destroyed or have
surrendered, the ship or colony becomes the property of the attacking nation,
provided the attacker still has troops there.

{{< callout type="warning" >}}
TODO: Capture leads to *control of a planet*, covered in the Control of Planets
section, which has not yet been converted.
{{< /callout >}}

### Captured population units

On transfer to the new owner, 50% of the loyal population units become rebels,
50% of all rebels convert to loyal population, and any remaining soldiers are
disbanded and become `UEM`. Population of a different race from the new owner's
becomes rebels at double the normal rate. These loyalty rules are owned by
[Rebellion]({{< relref "rebellion.md#loyalty-on-capture" >}}).

## Combat and ship or colony TL

A captured ship or colony drops one `TL`, unless it is already at `TL1`. A colony
that is not captured but loses 20% or more of its population to bombardment or
rebellion also drops one `TL`, unless it is already at `TL1`. For what a `TL` is,
see [Technological Advancement]({{< relref "technological-advancement.md" >}});
the rebellion-driven 20% loss is also stated under
[Rebellion]({{< relref "rebellion.md#when-rebellion-occurs" >}}).
