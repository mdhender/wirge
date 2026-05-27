# Planet Generation v1

## Overview

The planet generator builds a solar system one layer at a time: first the set of
occupied orbits, then the planet in each, then habitability, then resources.

This document describes the **constraints and algorithms**, not an
implementation. All random draws use the game's RNG; the steps below say *what*
to draw and *how* to combine the results, not how the RNG is wired in.

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
5. Sort the taken orbit numbers ascending.
6. Return them.

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

There are three types: **terrestrial**, **gas giant**, and **asteroid**.

In the rules below, "orbit N is terrestrial" is shorthand for "if orbit N is
occupied, its planet is terrestrial." Empty orbits hold no planet and produce no
entry in the output.

### Special rule

- If exactly one orbit is occupied, that planet is a **gas giant**. The list
  contains only that planet.

### Assignment by orbit

When more than one orbit is occupied, each occupied orbit takes its type from its
position:

- **Orbits 1–3** are always terrestrial.
- **Orbits 4–6:** roll 1d3. On a 1 the planet is a gas giant; otherwise it is
  terrestrial (so gas giants appear about one-third of the time).
- **Orbits 7–10:**
  - If the next inner orbit is empty — orbit 7 peeks at orbit 6, orbit 8 at 7,
    and so on — the planet is an asteroid.
  - Otherwise roll 1d20. On a 1 the planet is terrestrial; otherwise it is a gas
    giant (so terrestrials are rare, about 5%, in the outer orbits).

### Correction: the 4–5–6 asteroid

After the orbit-based assignment, apply one fix-up to the inner trio:

- If orbits 4, 5, and 6 are all occupied, orbits 4 and 5 came out terrestrial,
  and orbit 6 is a gas giant, force orbit 5 to an asteroid.

This runs after the 1d3 rolls for orbits 4–6 are resolved, since it depends on
their outcomes.

Return the list of planets.

## Habitability

Each planet gets a **habitability number (HN)**. The HN is bounded by the
planet's type:

| Type        | HN range |
| ----------- | -------- |
| Terrestrial | 0 – 25   |
| Gas giant   | 0 – 12   |
| Asteroid    | 0        |

### Method

Terrestrials and gas giants both use a two-step method — a **habitable gate**
followed by a **value roll**:

1. **Gate.** Roll 1d1000. The gate passes if the roll is at or below the orbit's
   threshold in the table below; otherwise it fails, the HN is 0, and the planet
   is uninhabitable.
2. **Value.** Roll `b = 3d6 − 3` (range 0–15), then compute

   `HN = floor(b × Hmax / 15)`

   where `Hmax` is the type-and-orbit cap from the tables below.
3. **Floor.** If the gate passed but the value came out 0, set HN to 1 — passing
   the gate always means at least minimally habitable.

Asteroids skip both steps: their HN is always 0.

### Habitable gate

Thresholds are out of 1000 (roll 1d1000, pass if at or below). The terrestrial
gate peaks at orbit 4 (the terrestrial habitable zone); the gas-giant gate peaks
at orbit 7, tracking the gas-giant value peak so that gas giants are both most
likely to be habitable and most habitable in the same orbit.

| Orbit | Terrestrial | Gas giant |
| ----- | ----------- | --------- |
| 1     | 100         | 10        |
| 2     | 200         | 20        |
| 3     | 400         | 25        |
| 4     | 800         | 50        |
| 5     | 400         | 100       |
| 6     | 200         | 200       |
| 7     | 100         | 400       |
| 8     | 50          | 200       |
| 9     | 20          | 100       |
| 10    | 10          | 50        |

### Value cap (Hmax)

Terrestrial `Hmax` peaks at 25 in orbit 4 (the terrestrial habitable zone).
Gas-giant `Hmax` peaks at 12 in orbit 7: gas giants are most habitable farther
out, where their moon systems sit.

| Orbit | Terrestrial | Gas giant |
| ----- | ----------- | --------- |
| 1     | 8           | 2         |
| 2     | 16          | 3         |
| 3     | 22          | 4         |
| 4     | 25          | 6         |
| 5     | 22          | 8         |
| 6     | 16          | 10        |
| 7     | 8           | 12        |
| 8     | 4           | 10        |
| 9     | 2           | 7         |
| 10    | 1           | 4         |

With these caps a terrestrial reaches 25 only in orbit 4 (`b = 15` → `floor(15 ×
25 / 15) = 25`), and a gas giant reaches 12 only in orbit 7 — the maximums set by
the HN ranges at the top of this section.

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

The count depends on type. For terrestrials and gas giants it is `(orbit)d6`
reduced by the planet's HN, then clamped to 1–40 — so the more habitable a world
is, the fewer deposits it carries (mineral wealth traded for living space).
Asteroids use a single dense band, independent of orbit.

| Type        | Deposit count                         |
| ----------- | ------------------------------------- |
| Terrestrial | `(orbit)d6 − HN`, clamped to 1–40     |
| Gas giant   | `(orbit)d6 − HN`, clamped to 1–40     |
| Asteroid    | `10 + 1d30` (11–40)                   |

The clamp floors the count at 1 (every planet has at least one deposit) and caps
it at the 40-deposit maximum. `(orbit)d6` means one d6 per orbit number — e.g. a
planet in orbit 9 rolls `9d6`.

### Resource type

Each deposit rolls 1d100 for its resource. The mix depends on type: terrestrials
are fuel-leaning with scarce gold, gas giants are strongly fuel-rich (their
hydrogen atmospheres), and asteroids are balanced across the three bulk
resources with gold rarest of all.

| Roll (1d100) | Terrestrial | Gas giant   | Asteroid    |
| ------------ | ----------- | ----------- | ----------- |
| GOLD         | 41–42 (2%)  | 01 (1%)     | 34 (1%)     |
| FUEL         | 01–40 (40%) | 02–66 (65%) | 01–33 (33%) |
| METS         | 43–71 (29%) | 67–83 (17%) | 35–67 (33%) |
| NMTS         | 72–100 (29%)| 84–100 (17%)| 68–100 (33%)|

### Quantity

| Type                  | Quantity                              |
| --------------------- | ------------------------------------- |
| Terrestrial / Gas giant | `4d20 × 1,000,000` (4M–80M)         |
| Asteroid              | `33,000,000 – 99,000,000` (largest)   |

Asteroid deposits are the largest in the cluster; terrestrial and gas-giant
deposits are smaller. Both stay within the 1,000,000–99,000,000 band required of
every deposit.

### Yield

| Type                  | Yield (percent) |
| --------------------- | --------------- |
| Terrestrial / Gas giant | `1d15` (1–15%) |
| Asteroid              | `1d6` (1–6%)    |

Asteroids carry the largest deposits but the poorest yields — lots of ore,
slowly extracted.

**What yield does.** Yield is the fraction of a mining group's extraction that
becomes product, and it also sets how fast the deposit depletes. If a group
extracts 1,000 units from a deposit with a 10% yield, it produces 100 units (10%
of 1,000); the deposit's quantity then falls by 100 — by the amount *produced*,
not the 1,000 extracted. So a low-yield deposit both produces less per turn and
lasts far longer: an asteroid (large quantity, low yield) is a slow, durable
mine. This generator only sets the starting yield; the full extraction rules
belong in the mining reference.

### Gold penalty

After a deposit's resource, quantity, and yield are rolled, one rule applies to
**any** `GOLD` deposit, regardless of type or orbit:

- **Yield** is reduced to a third: `max(1, floor(yield / 3))` (never below 1%).
- **Quantity** is reduced to a tenth: `max(1,000,000, floor(quantity / 10))`
  (never below 1,000,000).

Gold is both scarce (rarely rolled) and lean (penalized when found), keeping it a
premium resource.
