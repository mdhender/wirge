---
title: Planets
weight: 43
---

A **planet** occupies an orbit within a solar system and is the basic site for
colonies, mining, and farming. This page gathers what a planet is — its type,
what its surface and orbit can hold, and the natural resources it carries.
Each planet also has a [habitability number]({{< relref "habitability.md" >}}) (HN)
that sets its surface limits.

## Types

A solar system has from one to ten planets, occupying [orbits]({{< relref
"game-setup.md#orbits" >}}) 1 through 10. There are three types:

| Type            | Description |
| --------------- | ----------- |
| **Terrestrial** | Too small to retain a gas giant's atmosphere, but large enough to be spherical. Not necessarily "earth-like." |
| **Gas giant**   | Natural resources and surface colonies are located only on its moons. |
| **Asteroid**    | Too small to be spherical, so it keeps an irregular shape. Refers to an entire asteroid belt. |

{{< callout type="info" >}}
An **asteroid** and a **gas giant**'s moons are each treated as a single planet.
{{< /callout >}}

## Habitability number

Every planet has a habitability number (HN) from 0 to 25 that sets how much
population and farming its surface supports and whether open colonies are
allowed. See [Habitability]({{< relref "habitability.md" >}}) for the ranges by
type and the surface limits derived from the HN.

## What a planet can hold

A player may establish at most one open colony, one enclosed colony, and one orbiting colony at a single planet, plus any number of ships; see [Colonies and Ships]({{< relref "colonies-and-ships.md" >}}) for this limit across all entity types.
What types of colonies are allowed depends on the planet's type and HN:

| Planet          | Open Colony | Enclosed Colony | Orbiting Colony |
| --------------- | ----------- | --------------- | --------------- |
| **Terrestrial** | if HN > 0   | always          | always          |
| **Gas giant**   | if HN > 0   | always          | always          |
| **Asteroid**    | never       | always          | always          |

A planet with HN of 0 cannot hold an open colony.

A gas giant has no usable surface of its own — its surface colonies and natural resources sit on its moons, which the game treats as part of the one planet.

{{< callout type="warning" >}}
**Differs from the rule book.** The original rules locate open colonies on
terrestrials only, leaving a gas giant with no buildable surface. We allow
surface colonies on a gas giant's moons: without them, a gas giant's natural
resources could never be mined, since mining requires a surface colony and a gas
giant would otherwise have none.
{{< /callout >}}

## Natural resources

Each planet holds a maximum of 40 natural resource deposits. Each deposit
contains from 1,000,000 to 99,000,000 units of a single resource:

| Resource | Use                                      |
| -------- | ---------------------------------------- |
| **GOLD** | Economic exchange.                       |
| **FUEL** | All production and transportation.       |
| **METS** | All metallic substances other than gold. |
| **NMTS** | All non-metallic substances.             |

Each deposit also has a **yield** — a percentage that sets how much of a mining
group's extraction becomes usable product each turn. The yield is fixed when the
planet is generated; see [Mining]({{< relref "mining.md#yield" >}}) for how it
applies.

## Learning about a planet

A player does not automatically know a planet's contents. Two methods reveal
them: a **probe** reads any planet in the same system, while a **survey** reads
the planet a ship or colony is located at. For the full report contents, see
[Probes]({{< relref "exploration.md#probes" >}}) and
[Surveys]({{< relref "exploration.md#surveys" >}}).

## Control

A planet may be controlled by a player who establishes an orbiting or surface
colony — or a trade station — there and declares control. Control may be
contested, granted by diplomacy, or relinquished; see
[Control of Planets]({{< relref "control-of-planets.md" >}}) for the full rules.

## Generation

At game setup, every planet in the cluster is built one layer at a time:
first the orbits it occupies, then the type in each orbit, then habitability,
then resources. The rules below define that procedure — they are the source
of truth for what the cluster looks like on turn 1, and the engine must match
them.

### Occupied orbits

A system has ten orbits, numbered 1 to 10. The procedure picks 1 to 10 of
them to hold a planet:

1. Form the list of orbit numbers 1 through 10.
2. Shuffle the list.
3. Roll `3d4 − 2` for the number of occupied orbits (range 1–10, mean 5.5).
4. Take that many orbit numbers from the front of the shuffled list.
5. **Single-planet override.** If the count is 1, discard the taken orbit and
   use **orbit 7** instead.
6. Sort the result ascending.

`3d4 − 2` is a bell curve centred on 5–6; single-planet and full-ten systems
are each about 1.6%. The single-planet override pairs with the type rule
below — a lone planet is always a gas giant, and orbit 7 is where gas giants
belong.

### Planet types

Each occupied orbit takes its type from its position. Resolve every orbit
against the *original* occupancy map; never read your own output.

- **Single occupied orbit.** The planet is a **gas giant**. (Orbit
  generation has already placed it in orbit 7.)
- **Orbits 1–3.** Always **terrestrial**.
- **Orbits 4–6.** Roll 1d3. On a 1 the planet is a **gas giant**; otherwise
  it is **terrestrial**.
- **Orbits 7–8.** Roll 1d20. On a 1 the planet is **terrestrial**; otherwise
  it is a **gas giant**.
- **Orbit 9.** Roll 1d20. On a 1 the planet is **terrestrial**; on a 2 it is
  a **gas giant**; otherwise it is an **asteroid** (≈90% asteroid).
- **Orbit 10.** Always an **asteroid**. The outer edge of the system holds
  only rocky debris.

Then apply two fix-ups in order:

**Lone outer asteroid.** Walk the occupied orbits from 8 down to 7. The first
one whose next inner orbit is empty (orbit 8 peeks at 7; orbit 7 at 6)
becomes an **asteroid**, overwriting the 1d20 result. Stops after one
conversion; if neither orbit qualifies, the step does nothing. The peek uses
the *original* occupancy.

**The 4-5-6 asteroid.** If orbits 4, 5, and 6 are all occupied, orbits 4 and
5 came out terrestrial, and orbit 6 is a gas giant, force orbit 5 to an
**asteroid**.

### Habitability number

Each terrestrial or gas giant rolls one die and reads one row:

1. Roll `r = 2d15` (range 2–30, mean 16).
2. Look up `penalty` and `div` for the planet's type and orbit (tables below).
3. `HN = clamp(floor((r − penalty) / div), 0, typeMax)`.

`typeMax` is the ceiling from [Habitability]({{< relref "habitability.md" >}}):
25 for terrestrials, 12 for gas giants. Asteroids skip the roll; their HN is
always 0.

There is no separate "habitable gate." A planet is uninhabitable (HN = 0)
precisely when the roll fails to overcome its orbit's penalty. The `div` of 2
on fringe orbits compresses successful rolls into a smaller HN — a hot,
irradiated world that may briefly be habitable but is never lush.

**Terrestrial penalties.** Peak at orbit 4. Orbit 1 is both hard to make
habitable and capped low when it works (div 2). Orbit 10 never holds a
terrestrial.

| Orbit | Penalty | Div | Habitable chance |
| ----- | ------- | --- | ---------------- |
| 1     | 17      | 2   | ~40%             |
| 2     | 9       | 1   | ~84%             |
| 3     | 4       | 1   | ~97%             |
| 4     | 2       | 1   | ~99.6%           |
| 5     | 4       | 1   | ~97%             |
| 6     | 10      | 1   | ~80%             |
| 7     | 18      | 1   | ~32%             |
| 8     | 24      | 1   | ~7%              |
| 9     | 28      | 1   | ~1%              |

**Gas-giant penalties.** Same shape as the terrestrial curve, shifted right
by three orbits — peak at orbit 7, with the tail wrapping back through the
inner orbits. The divisor is always 2: a gas giant is at most half as
habitable as a terrestrial in the same favorable orbit.

| Orbit | Source (terr. orbit) | Penalty | Div | Habitable chance |
| ----- | -------------------- | ------- | --- | ---------------- |
| 1     | 7                    | 18      | 2   | ~32%             |
| 2     | 8                    | 24      | 2   | ~7%              |
| 3     | 9                    | 28      | 2   | ~1%              |
| 4     | 1                    | 17      | 2   | ~40%             |
| 5     | 2                    | 9       | 2   | ~84%             |
| 6     | 3                    | 4       | 2   | ~97%             |
| **7** | **4**                | **2**   | 2   | ~99.6%           |
| 8     | 5                    | 4       | 2   | ~97%             |
| 9     | 6                    | 10      | 2   | ~80%             |

The divisor is always taken from the gas-giant row. The shift only borrows
the *penalty* from the source terrestrial row, never its divisor — otherwise
gas-giant orbit 4 would compound to div 4.

### Resource deposits

Resources are generated *after* habitability, because a planet's deposit count
depends on its HN. The generator rolls each attribute **per deposit**, so a
planet's deposits vary among themselves. See [Natural resources](#natural-resources)
above for what each resource is used for, and [Mining]({{< relref "mining.md#yield" >}})
for how yield turns extraction into product.

#### Count

| Case                                    | Deposit count                                |
| --------------------------------------- | -------------------------------------------- |
| Asteroid                                | `15 + 1d25` (16–40, mean 28)                 |
| Terrestrial / gas giant, **HN = 0**     | `clamp((orbit)d6, 1, 40)`                    |
| Terrestrial / gas giant, **HN ≥ 1**     | `clamp((orbit)d6 − floor(HN / 2), 3, 6)`     |

`(orbit)d6` means one d6 per orbit number — a planet in orbit 9 rolls `9d6`.
A habitable terrestrial or gas giant carries **3 to 6 deposits** no matter
how lucky the roll: the small farm-side mine, not an industrial site. The
`− floor(HN/2)` term biases the result toward the low end as HN climbs — a
barely-habitable HN-1 world rolls near 6, a lush HN-25 paradise rolls 3 every
time. Uninhabited terrestrials and gas giants, and all asteroids, are the
cluster's true mining grounds.

#### Resource type

Each deposit rolls 1d100 for its resource. Inner terrestrials are metal-rich
(differentiated cores), outer terrestrials carry ices and volatiles (NMTS),
gas giants are fuel-heavy, and asteroids are balanced.

Terrestrials — three orbit bands:

| 1d100 | Inner (orbits 1–2) | Mid (orbits 3–4) | Outer (orbits 5–6) |
| ----- | ------------------ | ---------------- | ------------------ |
| GOLD  | 01–02 (2%)         | 01–02 (2%)       | 01–02 (2%)         |
| FUEL  | 03–32 (30%)        | 03–42 (40%)      | 03–32 (30%)        |
| METS  | 33–87 (55%)        | 43–71 (29%)      | 33–50 (18%)        |
| NMTS  | 88–100 (13%)       | 72–100 (29%)     | 51–100 (50%)       |

Gas giants — fuel-dominant, single mix:

| 1d100 | Gas giant    |
| ----- | ------------ |
| GOLD  | 01 (1%)      |
| FUEL  | 02–71 (70%)  |
| METS  | 72–79 (8%)   |
| NMTS  | 80–100 (21%) |

Asteroids — balanced, single mix:

| 1d100 | Asteroid     |
| ----- | ------------ |
| GOLD  | 34 (1%)      |
| FUEL  | 01–33 (33%)  |
| METS  | 35–67 (33%)  |
| NMTS  | 68–100 (33%) |

#### Quantity

| Type                    | Quantity                                       |
| ----------------------- | ---------------------------------------------- |
| Terrestrial / Gas giant | `4d20 × 1,000,000` (4M–80M)                    |
| Asteroid                | uniform integer in `[33,000,000, 99,000,000]`  |

Both ranges stay within the 1,000,000–99,000,000 band required of every
deposit.

#### Yield

| Type                    | Yield (percent)                       |
| ----------------------- | ------------------------------------- |
| Terrestrial / Gas giant | `clamp(1d15 − floor(HN / 3), 1, 15)`  |
| Asteroid                | `1d6` (1–6%)                          |

The per-deposit yield penalty of `floor(HN / 3)` reflects pristine farmland:
the more habitable the world, the less of its surface can be stripped for
ore. Asteroids carry the largest deposits but the poorest yields — lots of
ore, slowly extracted.

#### Gold penalty

After a deposit's resource, quantity, and yield are rolled, two rules apply
to any `GOLD` deposit, regardless of type or orbit:

- **Yield** is reduced to a third: `max(1, floor(yield / 3))`.
- **Quantity** is reduced to a tenth: `max(1,000,000, floor(quantity / 10))`.

Gold is both scarce (rarely rolled) and lean (penalised when found), keeping
it a premium resource.
