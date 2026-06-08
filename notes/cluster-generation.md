# Cluster Generation

> WARNING: THIS IS EXPERIMENTAL!

The original *Empyrean Challenge* manual never specified how a cluster is generated, so the rules
here are **invented**. This document is therefore authoritative design for cluster generation:
where it specifies a rule, [`REFERENCE.md`](../REFERENCE.md) cites it rather than the other way
around.

A system is identified by three two-digit coordinate fields, e.g. `28-02-18`. Each field is an
integer in the range `00`–`30`, inclusive ([REFERENCE §2.1](../REFERENCE.md#21-coordinates-and-systems)),
giving `31 × 31 × 31 = 29,791` possible coordinates — far more than the 100 systems we place.

All randomness draws from the per-game RNG seeded by `Game.seed` (see `DATA-MODEL.md`), so a given
seed always produces the same cluster.

## Systems

A cluster has exactly 100 systems. Each system has 1, 2, or 3 stars (single, binary, trinary). We
deliberately spread the multi-star systems away from each other and from the single systems: the
larger of any two systems' star counts sets how far apart they must be.

Build the candidate coordinate pool:

```
possibleCoords := every (x, y, z) with x, y, z in 0..30   // 29,791 coordinates
shuffle possibleCoords using the Game.seed RNG
```

Generate the systems. We assign each system its number of stars by generation order, placing the
most-constrained (trinary) systems first so they find room before the cluster fills:

```
systems := empty list
for i := 1 to 100:
    system := new System
    if i <= 5:
        system.stars := 3        // trinary
    else if i <= 15:
        system.stars := 2        // binary
    else:
        system.stars := 1        // single

    // Find coordinates that respect the spacing rule against every placed system.
    loop:
        assert(possibleCoords is not empty)
        candidate := pop next coordinates from possibleCoords   // discarded if rejected
        acceptable := true
        for each other in systems:
            minDist := max(system.stars, other.stars)           // 1, 2, or 3
            if squaredDistance(candidate, other.coords) < minDist * minDist:
                acceptable := false                             // too close — reject
                break
        if acceptable:
            system.coords := candidate
            break

    append system to systems
```

`squaredDistance` is the squared Euclidean distance `dx² + dy² + dz²`; comparing it against
`minDist * minDist` keeps the test in integers and avoids a square root. The required separation is:

| Larger of the two star counts | Minimum separation |
|------------------------------|--------------------|
| 3 (a trinary is involved)    | 3 (squared: 9)     |
| 2 (a binary, no trinary)     | 2 (squared: 4)     |
| 1 (both single)              | 1 (squared: 1)     |

Two single systems only need distinct coordinates, which a shuffled-unique pool guarantees, so that
case never rejects. Squaring the star count (rather than, say, doubling it) leaves headroom for a
possible future four-star system, which would require a separation of 4.

A rejected candidate is **discarded**, never requeued. This guarantees the loop terminates: the pool
shrinks by one every iteration, so each system is either placed or the `assert` fires when the pool
empties. With 29,791 coordinates and only 100 systems the pool never runs dry in practice.

## Stars

Each system now holds a *count* of stars (1, 2, or 3) from the Systems pass. Here we replace that
count with the actual `Star` objects ([DATA-MODEL](../DATA-MODEL.md): `System.stars` is the list of
stars). All stars in a system share the system's coordinates. Each star is given a
`sequence_letter` (`A`, `B`, …) to disambiguate it within a multi-star system, and 10 orbits.

Every star has at least 5 occupied orbits. We roll the count as `numberOfOccupiedOrbits := 4 +
roll(1, 6)`, where `roll(1, 6)` is a random integer in `1..6` drawn from the `Game.seed` RNG —
yielding 5 to 10 occupied orbits. The Planets section uses this count to decide which of the 10
orbits receive a planet.

```
for each system in systems:
    starCount := system.stars            // the count chosen in the Systems pass
    system.stars := empty list           // now holds the actual Star objects

    for j := 1 to starCount:
        star := new Star
        star.sequence_letter := letter(j)    // 1 → 'A', 2 → 'B', 3 → 'C'
        star.orbits := empty list

        // Every star has orbits 1..10; at least 5 of them are occupied by a planet.
        numberOfOccupiedOrbits := 4 + roll(1, 6)   // 4 + a 1..6 roll ⇒ 5..10

        for orbit_no := 1 to 10:
            isOccupied := orbit_no <= numberOfOccupiedOrbits
            orbit := createOrbit(orbit_no, isOccupied)   // see the Orbits section
            append orbit to star.orbits

        append star to system.stars
```

Each orbit starts empty; the Planets section fills `orbit.planet` for occupied orbits.

## Orbits

We model only the **10 real orbits** (1–10) that can hold a planet. Orbit 11 is a **fictitious
orbit for player convenience**: it is player-facing notation that reminds players they may jump
between the stars of a multi-star system. It is *not* a stored entity — the engine never creates an
orbit-11 record, so generation does nothing with it. (This refines
[REFERENCE §2.2](../REFERENCE.md#22-stars-and-orbits), which describes orbit 11 as a companion-star
"slot"; here it is purely notation.)

Because orbit 11 is fictitious, we do **not** store companion-star references anywhere. A star's
companions are found by following the star back to its parent `System` and reading that system's
list of stars (every star in the list other than this one is a companion). This keeps companions
derived from the system structure rather than duplicated into an orbit slot.

An orbit holds a reference to the `Planet` in it, or `null` when the orbit is empty. The caller
passes `isOccupied` to say whether this orbit should receive a planet (the lowest
`numberOfOccupiedOrbits` orbits are occupied). `createOrbit` records that intent; the Planets
section fills `orbit.planet` for occupied orbits and leaves the rest `null`.

```
function createOrbit(orbit_no, isOccupied):
    orbit := new Orbit
    orbit.number := orbit_no       // 1..10
    orbit.isOccupied := isOccupied // true ⇒ the Planets section will give it a planet
    orbit.planet := null           // empty until the Planets section fills it
    return orbit
```

## Planets

With orbits in place, we give every **occupied** orbit a planet and leave empty orbits `null`. The
planet's type is fixed by its orbit number — the inner orbits favor terrestrials, the middle orbits
are gas giants, and asteroid belts sit at the edges of each band:

| Orbit | Planet type   |
|-------|---------------|
| 1–4   | terrestrial   |
| 5     | asteroid      |
| 6–8   | gas giant     |
| 9     | terrestrial   |
| 10    | asteroid      |

```
function planetTypeFor(orbit_no):
    case orbit_no:
        1, 2, 3, 4: return TERRESTRIAL
        5:          return ASTEROID
        6, 7, 8:    return GAS_GIANT
        9:          return TERRESTRIAL
        10:         return ASTEROID

for each system in systems:
    for each star in system.stars:
        for each orbit in star.orbits:
            if not orbit.isOccupied:
                continue                              // empty orbit — leave orbit.planet null

            planet := new Planet
            planet.orbit_no := orbit.number
            planet.type := planetTypeFor(orbit.number)
            planet.habitability := habitabilityFor(planet, orbit.number)   // see Habitability below
            planet.habitable := planet.habitability > 0
            planet.deposits := depositsFor(planet, orbit.number)           // see Deposits below
            orbit.planet := planet
```

`TERRESTRIAL`, `ASTEROID`, and `GAS_GIANT` are the values of `PlanetType`
([DATA-MODEL](../DATA-MODEL.md): `gas_giant | terrestrial | asteroid`). The Habitability and Deposits
sections below define the remaining attributes — both driven by orbit number.

### Habitability

Habitability is an integer `0`–`25` ([REFERENCE §2.4](../REFERENCE.md#24-habitability)). **Asteroids
are never habitable** (always 0). For terrestrials and gas giants it is derived from the orbit
number in two steps: an orbit-dependent *chance* that the planet is habitable at all, and — when it
is — a habitability value rolled within an orbit-dependent *range*. Both peak at **orbit 4** (the
habitable zone) and fall off toward the innermost orbit and the outer orbits — a planet is most
likely to be habitable, and most habitable when it is, around orbit 4.

```
function habitabilityFor(planet, orbit_no):
    if planet.type == ASTEROID:
        return 0                                  // asteroids are never habitable (orbits 5, 10)

    // Terrestrials and gas giants. chance(p) is true with probability p%.
    case orbit_no:
        1, 8, 9: return chance(5)  ? roll(1, 3)  : 0
        2, 7:    return chance(10) ? roll(2, 5)  : 0
        3, 6:    return chance(35) ? roll(3, 10) : 0
        4:       return chance(65) ? roll(8, 25) : 0
```

| Orbit(s) | Chance habitable | Habitability if habitable |
|----------|------------------|---------------------------|
| 1, 8, 9  | 5%               | `roll(1, 3)`  → 1–3       |
| 2, 7     | 10%              | `roll(2, 5)`  → 2–5       |
| 3, 6     | 35%              | `roll(3, 10)` → 3–10      |
| 4        | 65%              | `roll(8, 25)` → 8–25      |
| 5, 10    | —                | 0 (asteroid)              |

Helpers, both drawing from the `Game.seed` RNG: `roll(min, max)` returns a random integer in
`min..max` inclusive; `chance(percent)` returns true with the given percent probability. Orbit 4 is
the sweet spot — most likely to be habitable and reaching the full habitability range; orbits 5 and
10 are always asteroids and so always 0.

Habitability gates open (surface) colonies, and it is **not** restricted to terrestrials: a gas
giant (orbits 6–8) with habitability > 0 is habitable and may host open colonies, since colonies are
tied to orbits, not to a planet's "color." `planet.habitable` is simply `habitability > 0`.

### Deposits

Each planet has at most **40** resource deposits ([REFERENCE §2.5](../REFERENCE.md#25-resource-deposits)).
A deposit has a `resource` (`GOLD | FUEL | METS | NMTS`), a `quantity` (1M–99M units), and a
`yield_pct` (the mining yield reported to players). Deposit **count**, **yield**, and **quantity**
are all driven by the orbit number. Two resource-dependent rules apply everywhere,
regardless of orbit or planet type: a **`GOLD`** deposit's **yield** is reduced to a third (min 1%)
and its **quantity** to a tenth (min 1,000,000). `depositsFor` builds the list:

```
function depositsFor(planet, orbit_no):
    deposits := empty list
    count := depositCountFor(planet, orbit_no)
    for d := 1 to count:
        deposit := new Deposit
        deposit.number    := d
        deposit.yield_pct := yieldFor(orbit_no)        // percent
        deposit.resource  := resourceFor(planet, orbit_no)
        deposit.quantity  := quantityFor(orbit_no)     // units (MU)
        if deposit.resource == GOLD:                   // global gold penalties, all orbits/types
            deposit.yield_pct := max(1, floor(deposit.yield_pct / 3))      // a third (min 1%)
            deposit.quantity  := max(1000000, floor(deposit.quantity / 10)) // a tenth (min 1M)
        append deposit to deposits
    return deposits
```

#### Asteroids (orbits 5 and 10)

Asteroids carry the **largest deposits but the lowest yields**, and may hold any of the four
resources (`FUEL`, `GOLD`, `METS`, `NMTS`). Count and yield differ between the two asteroid orbits;
each deposit rolls its own yield within the orbit's range:

| Orbit | Deposit count      | Range  | Yield per deposit | Range  |
|-------|--------------------|--------|-------------------|--------|
| 5     | `10 + roll(1, 30)` | 11–40  | `roll(1, 12)` %   | 1–12%  |
| 10    | `25 + roll(1, 15)` | 26–40  | `roll(1, 3)` %    | 1–3%   |

```
function depositCountFor(planet, orbit_no):
    case orbit_no:
        5:  return 10 + roll(1, 30)    // 11..40  (asteroid belt)
        10: return 25 + roll(1, 15)    // 26..40  (asteroid belt)
        else:                          // terrestrials & gas giants (orbits 1–4, 6–9)
            count := rollDice(orbit_no, 6) - planet.habitability
            return clamp(count, 1, 40) // at least 1; capped at 40

function yieldFor(orbit_no):
    case orbit_no:
        5:  return roll(1, 12)   // 1..12 %  (asteroid belt)
        10: return roll(1, 3)    // 1..3 %   (asteroid belt)
        else: return roll(1, 15) // 1..15 %  (terrestrials & gas giants, orbits 1–4, 6–9)

function quantityFor(orbit_no):
    case orbit_no:
        5, 10: return roll(33000000, 99000000)   // asteroids — the largest deposits
        else:  return rollDice(4, 20) * 1000000  // 4d20 × 1M → 4M..80M (orbits 1–4, 6–9)
```

Both formulas cap at the 40-deposit maximum (`10 + 30` and `25 + 15`). Orbit 10's belts are denser
(at least 26 deposits) but poorer (≤3% yield) than orbit 5's. Asteroid deposits are the largest in
the cluster: each holds `roll(33000000, 99000000)` units (33M–99M) before any gold penalty.

Each asteroid deposit picks its resource independently with a `roll(1, 100)`: gold is rare, the
other three roughly equal.

| Roll (1d100) | Resource | Chance |
|--------------|----------|--------|
| 1–33         | `FUEL`   | 33%    |
| 34           | `GOLD`   | 1%     |
| 35–67        | `METS`   | 33%    |
| 68–100       | `NMTS`   | 33%    |

```
function resourceFor(planet, orbit_no):
    if planet.type == ASTEROID:
        case roll(1, 100):
            1..33:   return FUEL
            34:      return GOLD
            35..67:  return METS
            68..100: return NMTS
    else:                       // terrestrials & gas giants (orbits 1–4, 6–9)
        case roll(1, 100):
            1..40:   return FUEL
            41..42:  return GOLD
            43..71:  return METS
            72..100: return NMTS
```

#### Terrestrials and gas giants (orbits 1–4, 6–9)

These orbits may also hold any of the four resources (`FUEL`, `GOLD`, `METS`, `NMTS`). The deposit
**count** is the orbit number's worth of d6 dice, reduced by the planet's habitability, then clamped
to `1..40`:

```
count := rollDice(orbit_no, 6) - planet.habitability    // clamped to 1..40
```

`rollDice(n, 6)` sums `n` separate `roll(1, 6)` dice (drawing from the `Game.seed` RNG). Subtracting
habitability means the more habitable a world is, the fewer deposits it carries — habitable worlds
trade mineral wealth for living space. Examples:

| Orbit | Habitability | Roll        | Result (clamped 1–40)        |
|-------|--------------|-------------|------------------------------|
| 9     | 1            | `9d6 − 1`   | 8–53 → **8–40**              |
| 4     | 8            | `4d6 − 8`   | −4–16 → **1–16**             |
| 1     | 0            | `1d6 − 0`   | **1–6**                      |

The subtraction can drive the raw value to zero or below (a small, highly habitable world), so the
count is floored at 1 as well as capped at 40 — every planet has at least one deposit.

Each deposit rolls its own **base yield** of `roll(1, 15)` (1–15%) — higher than either asteroid
band. The global gold penalty still applies afterward (a `GOLD` deposit's yield drops to a third,
min 1%).

Resource is picked per deposit with a `roll(1, 100)` — fuel-heavy, gold scarce:

| Roll (1d100) | Resource | Chance |
|--------------|----------|--------|
| 1–40         | `FUEL`   | 40%    |
| 41–42        | `GOLD`   | 2%     |
| 43–71        | `METS`   | 29%    |
| 72–100       | `NMTS`   | 29%    |

**Quantity** is `4d20 × 1,000,000` — i.e. `rollDice(4, 20) * 1000000`, ranging 4M–80M units before
any gold penalty (a `GOLD` deposit's quantity then drops to a tenth, min 1,000,000). These are smaller
than the asteroid belts' 33M–99M.

### A note on planet types

Beyond what `planetTypeFor` sets, the three types need no separate generation logic. In game terms
`TERRESTRIAL` and `GAS_GIANT` are essentially "color" — every generated attribute (habitability,
deposit count, yield, resource mix, quantity) is driven by the **orbit number**, defined under
Habitability and Deposits above. The only type-dependent rule is that an `ASTEROID` (orbits 5 and 10)
is never habitable (habitability 0) and uses the asteroid deposit band. An asteroid is an entire belt
treated as a single planet ([REFERENCE §2.3](../REFERENCE.md#23-planets)).
