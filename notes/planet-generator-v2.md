# Planet Generation v2

## Overview

The planet generator builds a solar system one layer at a time: first the set of
occupied orbits, then the planet in each, then habitability, then resources.

This document describes the **constraints and algorithms**, not an
implementation. All random draws use the game's RNG; the steps below say *what*
to draw and *how* to combine the results, not how the RNG is wired in.

> v2 supersedes [planet-generator-v1.md](planet-generator-v1.md). It also
> supersedes the planet/orbit/habitability/deposit sections of
> [cluster-generation.md](cluster-generation.md), which were an earlier
> experiment and disagree with the reference docs.

## Orbit Generation

The first step decides which orbits hold a planet. It returns the list of
occupied orbit numbers, sorted ascending.

### Constraints

- A system has ten orbits, numbered 1 through 10.
- At least one orbit is occupied, and at most all ten.

### Algorithm

1. Form the list of orbit numbers 1 through 10.
2. Shuffle the list.
3. Roll 3d4 − 2 for the count of occupied orbits (range 1–10).
4. Take that many orbit numbers from the front of the shuffled list.
5. **Single-planet override.** If the count is 1, discard the taken orbit and
   use orbit **7** instead. (This pairs with the single-planet → gas-giant rule
   in the next section; gas giants belong in the outer band, so the lone planet
   is seated where a gas giant naturally lives.)
6. Sort the taken orbit numbers ascending.
7. Return them.

Shuffling and then taking from the front yields a uniform random subset of the
ten orbits; sorting at the end gives a stable, ascending result.

`3d4 − 2` lands in 1–10 natively, so no coercion or cap is needed: every system
has at least one planet and never more than ten. The count is a bell curve
centered on 5–6 (mean 5.5), so most systems are mid-sized and both single-planet
and full-ten systems are rare (about 1.6% each).

## Planet Types

Each occupied orbit holds one planet. This step assigns each planet a type. The
input is the list of occupied orbits (1–10); the output is the list of planets,
each carrying its orbit number and type.

There are three types: **terrestrial**, **gas giant**, and **asteroid**. An
asteroid is a single planet representing an entire belt; see
[planets.md#types](../content/reference/planets.md).

Note: this document addresses only orbits that are occupied. "orbit N is terrestrial"
is shorthand for "if orbit N is occupied, its planet is terrestrial." Empty orbits
hold no planet and produce no entry in the output.

### Special rule

- If exactly one orbit is occupied, that planet is a **gas giant**. (Orbit
  generation has already moved it to orbit 7.) The list contains only that
  planet.

### Assignment by orbit

When more than one orbit is occupied, each occupied orbit takes its type from
its position. The outer rule needs the original occupancy map, so resolve outer
orbits **before** the inner ones — or, equivalently, resolve all orbits against
the original occupancy and never read your own output.

- **Orbits 1–3** are always terrestrial.
- **Orbits 4–6:** roll 1d3. On a 1 the planet is a gas giant; otherwise it is
  terrestrial (so gas giants appear about one-third of the time).
- **Orbits 7–8:** roll 1d20. On a 1 the planet is terrestrial; otherwise it is
  a gas giant (so terrestrials are rare, about 5%, in the outer orbits).
- **Orbit 9:** roll 1d20. On a 1 the planet is terrestrial; on a 2 it is a gas
  giant; otherwise it is an asteroid. Orbit 9 is the edge of the planet-bearing
  zone: terrestrials and gas giants are both possible there but vanishingly
  rare (5% each).
- **Orbit 10:** always an asteroid. No roll. Orbit 10 is the outer edge of the
  system and only holds rocky debris.

### Correction: the lone outer asteroid

Apply this correction only if multiple orbits are occupied in the system.

Asteroids in the outer band can also be introduced by a single fix-up applied
after the per-orbit rolls:

1. Walk the occupied orbits from **8 down to 7**.
2. The first one whose **next inner orbit is empty** (orbit 8 peeks at 7,
   7 at 6) becomes an **asteroid**, overwriting whatever the 1d20 produced.
3. Stop after that single conversion. At most one asteroid is created this way
   per system; if neither orbit 7 nor orbit 8 has an empty inner neighbor, the
   step does nothing.

The peek uses the **original** occupancy from Orbit Generation, not the
type-assignment output. The walk runs from outer to inner so the *outermost*
isolated orbit becomes the asteroid — the lonelier rock at the edge — rather
than cascading inward. Orbits 9 and 10 are excluded from the walk because they
already favor asteroids by their own rules.

### Correction: the 4–5–6 asteroid

After the orbit-based assignment, apply one more fix-up to the inner trio:

- If orbits 4, 5, and 6 are all occupied, orbits 4 and 5 came out terrestrial,
  and orbit 6 is a gas giant, force orbit 5 to an asteroid.

This runs after the 1d3 rolls for orbits 4–6 are resolved, since it depends on
their outcomes. It is deliberately narrow — only this exact pattern fires it.
The original designer wanted it that way; the rationale was not written down,
and we preserve the rule unchanged because we are sheep.

Return the list of planets.

## Habitability

Each planet gets a **habitability number (HN)**. The HN is bounded by the
planet's type:

| Type        | HN range | Type cap |
| ----------- | -------- | -------- |
| Terrestrial | 0 – 25   | 25       |
| Gas giant   | 0 – 12   | 12       |
| Asteroid    | 0        | 0        |

These ranges match [habitability.md](../content/reference/habitability.md).
Asteroids are always 0 and skip the rest of this section.

### Method

A terrestrial or gas giant rolls **one** die and reads **one** row:

1. Roll `r = 2d15` (range 2–30, bell-shaped, mean 16).
2. Look up `penalty` and `div` for the planet's type and orbit (tables below).
3. `HN = clamp(floor((r − penalty) / div), 0, typeMax)`.

That's the whole step. There is no separate "habitable gate" — a planet is
uninhabitable (HN = 0) precisely when the roll fails to overcome its orbit's
penalty. High rolls clear the penalty by more, and become the planet's
habitability.

`div` is a per-orbit divisor that compresses the result for fringe orbits:
where it is `1` the roll passes through directly, where it is `2` even a
successful roll yields a small HN.

### Terrestrial

The terrestrial curve peaks at orbit 4 and falls off symmetrically. Orbit 1 is
both *hard to make habitable* (high penalty) and *capped low when it works*
(div 2), reflecting a hot, irradiated world that — even at its best — is no
prize. Orbits 8 and 9 are nearly impossible; orbit 10 is excluded (it is always
an asteroid).

| Orbit | Penalty | Div | Habitable chance | Mean HN | Max HN reachable |
| ----- | ------- | --- | ---------------- | ------- | ---------------- |
| 1     | 17      | 2   | ~40%             | ~1      | 6                |
| 2     | 9       | 1   | ~84%             | ~7      | 21               |
| 3     | 4       | 1   | ~97%             | ~12     | 25               |
| 4     | 2       | 1   | ~99.6%           | ~14     | 25               |
| 5     | 4       | 1   | ~97%             | ~12     | 25               |
| 6     | 10      | 1   | ~80%             | ~6      | 20               |
| 7     | 18      | 1   | ~32%             | ~2      | 12               |
| 8     | 24      | 1   | ~7%              | ~0      | 6                |
| 9     | 28      | 1   | ~1%              | ~0      | 2                |

### Gas giant

The gas-giant curve has the same shape as the terrestrial one, **shifted right
by three orbits**: the gas-giant peak is at orbit 7, and the curve's tail wraps
back through the inner orbits (gas-giant orbit 1 borrows the terrestrial
orbit-7 penalty, and so on). The divisor is `2` for every gas-giant orbit,
which keeps the HN at about half a terrestrial's — capping at 12 only at the
sweet-spot peak.

| Orbit | Source (terr orbit) | Penalty | Div | Habitable chance | Mean HN | Max HN reachable |
| ----- | ------------------- | ------- | --- | ---------------- | ------- | ---------------- |
| 1     | 7                   | 18      | 2   | ~32%             | ~1      | 6                |
| 2     | 8                   | 24      | 2   | ~7%              | ~0      | 3                |
| 3     | 9                   | 28      | 2   | ~1%              | ~0      | 1                |
| 4     | 1                   | 17      | 2   | ~40%             | ~1      | 6                |
| 5     | 2                   | 9       | 2   | ~84%             | ~3      | 10               |
| 6     | 3                   | 4       | 2   | ~97%             | ~6      | 12               |
| **7** | **4**               | **2**   | 2   | ~99.6%           | **~7**  | **12**           |
| 8     | 5                   | 4       | 2   | ~97%             | ~6      | 12               |
| 9     | 6                   | 10      | 2   | ~80%             | ~3      | 10               |

The divisor is always taken from the **gas-giant** row (`2`), never inherited
from the borrowed terrestrial row — otherwise gas-giant orbit 4 would compound
to div 4. The shift only borrows the penalty value.

The orbit-3 entry (HN max 1) is reachable in principle but essentially never
seen; it is listed for completeness, the same way the terrestrial table lists
orbits 8–9.

## Resources

Each planet carries up to **40** resource deposits. A deposit has three
attributes:

- **resource** — one of `GOLD`, `FUEL`, `METS`, `NMTS`.
- **quantity** — units (mass units) in the deposit, never below 1,000,000.
- **yield** — the mining yield, as a percent, reported to players.

Resources are generated **after habitability**, because a planet's deposit count
depends on its HN. Each attribute is rolled **per deposit**, so a planet's
deposits vary among themselves.

### Deposit count

The count splits into three discrete cases. Asteroids and uninhabited
terrestrials/gas giants are the cluster's mining grounds; a habitable
terrestrial or gas giant carries only a small farm-side mine, no more than six
deposits no matter how lucky the roll.

| Case                                  | Deposit count                                       |
| ------------------------------------- | --------------------------------------------------- |
| Asteroid                              | `15 + 1d25` (16–40, mean 28)                        |
| Terrestrial / gas giant, **HN = 0**   | `clamp((orbit)d6, 1, 40)`                           |
| Terrestrial / gas giant, **HN ≥ 1**   | `clamp((orbit)d6 − floor(HN / 2), 3, 6)`            |

Notes:

- `(orbit)d6` means one d6 per orbit number — e.g. a planet in orbit 9 rolls
  `9d6`. The clamp floor of 1 (uninhabited case) guarantees every planet has at
  least one deposit; the 40 cap is the published maximum.
- The habitable case is a **hard band of 3–6**. The `− floor(HN/2)` term biases
  the result toward the low end as HN climbs: a barely-habitable HN-1 world
  rolls near 6, a lush HN-25 paradise rolls 3 every time. Either way, a player
  founding an open colony knows they will get 3 to 6 mines and no more.
- The habitable case fires the moment HN reaches 1, matching
  [habitability.md](../content/reference/habitability.md): HN ≥ 1 is the
  threshold for open colonies, and is also the threshold where the surface
  starts trading mineral wealth for farmland.
- Asteroid count is independent of orbit. The orbit-5 inner belt and the
  orbit-10 outer belt draw from the same `15 + 1d25`; they differ in resource
  mix, not in count.

### Resource type

Each deposit rolls 1d100 for its resource. Terrestrials shift along the orbit
axis: inner worlds are metal-rich (differentiated cores), outer worlds carry
ices and volatiles (NMTS), and the middle band is balanced. Gas giants are
strongly fuel-rich with an NMTS tilt in the residual. Asteroids are balanced
across the three bulk resources.

#### Terrestrials — three orbit bands

| Roll (1d100) | Inner (orbits 1–2) | Mid (orbits 3–4) | Outer (orbits 5–6) |
| ------------ | ------------------ | ---------------- | ------------------ |
| GOLD         | 01–02 (2%)         | 01–02 (2%)       | 01–02 (2%)         |
| FUEL         | 03–32 (30%)        | 03–42 (40%)      | 03–32 (30%)        |
| METS         | 33–87 (55%)        | 43–71 (29%)      | 33–50 (18%)        |
| NMTS         | 88–100 (13%)       | 72–100 (29%)     | 51–100 (50%)       |

Orbit 4 sits at the balanced mid-point, which is also where most habitable
terrestrials end up — so a paradise gets the widest variety of mining choices,
just very few deposits to choose from.

#### Gas giants — single mix, fuel-dominant

| Roll (1d100) | Gas giant   |
| ------------ | ----------- |
| GOLD         | 01 (1%)     |
| FUEL         | 02–71 (70%) |
| METS         | 72–79 (8%)  |
| NMTS         | 80–100 (21%)|

Gas giants are first and foremost fuel stores; the residual leans NMTS to
reflect their icy moon systems.

#### Asteroids — single mix, balanced

| Roll (1d100) | Asteroid    |
| ------------ | ----------- |
| GOLD         | 34 (1%)     |
| FUEL         | 01–33 (33%) |
| METS         | 35–67 (33%) |
| NMTS         | 68–100 (33%)|

We keep one mix for all asteroid orbits to avoid an extra table; the
inner-band metallic / outer-band icy distinction lives in the terrestrial
table instead.

### Quantity

| Type                    | Quantity                                          |
| ----------------------- | ------------------------------------------------- |
| Terrestrial / Gas giant | `4d20 × 1,000,000` (4M–80M)                       |
| Asteroid                | uniform integer in `[33,000,000, 99,000,000]`     |

Asteroid deposits are the largest in the cluster; terrestrial and gas-giant
deposits are smaller. Both stay within the 1,000,000–99,000,000 band required
of every deposit (see [planets.md](../content/reference/planets.md#natural-resources)).

### Yield

| Type                    | Yield (percent)                                  |
| ----------------------- | ------------------------------------------------ |
| Terrestrial / Gas giant | `clamp(1d15 − floor(HN / 3), 1, 15)`             |
| Asteroid                | `1d6` (1–6%)                                     |

For terrestrials and gas giants the base roll is `1d15` (mean 8), but a per-
deposit penalty equal to `floor(HN / 3)` is subtracted. The narrative is
pristine farmland: the more habitable the world, the less of its surface can be
stripped for ore. Resulting mean yields:

| HN  | Mean yield (terr / gas) |
| --- | ----------------------- |
| 0   | 8                       |
| 5   | 7                       |
| 10  | 5                       |
| 14  | 4                       |
| 20  | 2                       |
| 25  | 1                       |

Asteroids carry the largest deposits but the poorest yields — lots of ore,
slowly extracted. The generator only sets the starting yield; for how yield
turns extraction into product and how a deposit depletes, see
[mining.md#yield](../content/reference/mining.md#yield).

### Gold penalty

After a deposit's resource, quantity, and yield are rolled, one rule applies to
**any** `GOLD` deposit, regardless of type or orbit:

- **Yield** is reduced to a third: `max(1, floor(yield / 3))` (never below 1%).
- **Quantity** is reduced to a tenth: `max(1,000,000, floor(quantity / 10))`
  (never below 1,000,000).

Gold is both scarce (rarely rolled) and lean (penalized when found), keeping it
a premium resource.

### Richness, at a glance

Per-planet richness is roughly `count × mean quantity × mean yield`. After the
rules above:

| World                              | Count | Qty (M) | Yield | Richness | Role |
| ---------------------------------- | ----- | ------- | ----- | -------- | ---- |
| Orbit-4 terrestrial, HN 14         | ~3    | 42      | 4     | ~500     | paradise — small farm-side mine |
| Orbit-3 terrestrial, HN 12         | ~4    | 42      | 4     | ~670     | habitable, modest |
| Orbit-9 gas giant, HN 0            | ~32   | 42      | 8     | ~10,700  | the cluster's mineral kingdom |
| Asteroid (any orbit)               | ~28   | 66      | 3.5   | ~6,500   | rich but slow |

Habitable worlds are roughly an order of magnitude poorer than asteroids and
two orders poorer than barren outer planets, which is the trade we want: pick
your world for farms or pick it for ore, but rarely both.
