---
title: Game Setup
weight: 40
---

Defines the initial game state for a new player, including cluster data, solar systems, stars, planets, and turn timing.

## Cluster

The cluster is the complete game map.

The cluster contains 100 solar systems distributed across three-dimensional space.

Solar system coordinates use the following format:

```text
XX-YY-ZZ
```

Each coordinate component:

- Uses two decimal digits
- Ranges from `00` to `30` inclusive
- Is separated by a hyphen (`-`)

Example coordinates:

```text
00-00-00
15-22-07
30-30-30
```

## Solar Systems

A solar system contains one or more stars sharing the same coordinates.

Classification by star count:

- 1 star: single-star system
- 2 stars: binary system
- 3 stars: trinary system

### Identifying a star

A system is named by its coordinates alone (`12-13-14`). Each star within a
system is named by appending a letter suffix, assigned in order: `A`, `B`, `C`,
and so on.

- `12-13-14A` — the first (or only) star
- `12-13-14B` — the second star (binary system)
- `12-13-14C` — the third star (trinary system)

The suffix is **required**, even in a single-star system: `12-13-14A` is the
star, while `12-13-14` is the system it belongs to. Requiring the suffix lets an
order name a star unambiguously and keeps it distinct from the bare system
coordinates.

{{< callout type="warning" >}}
**Differs from the rule book.** The 1978 rule book identifies a system only by
its coordinates and never labels individual stars — it distinguished them
through an eleventh-orbit mechanism in which each star was said to occupy the
others' eleventh orbit. The lettered star suffix comes from the 1980 rule book;
we adopt it and additionally **require** it on every system, including
single-star systems, so that orders can name a star precisely.
{{< /callout >}}

## Star Lists

A player-visible star list contains:

- Solar system coordinates
- Jump distances from a reference system

### Initial Visibility

A new player is provided with:

- A complete list of solar system coordinates in the cluster
- Jump distances from the player’s home system to all systems within jump range

### Exploration Visibility

Exploration of a solar system reveals all solar systems within jump range of that system.

## Stars and Orbits

Each star has exactly ten planetary orbits, numbered `1` to `10` inclusive.

Orbits may be occupied or empty.

Each occupied orbit contains exactly one planet.

An orbit is addressed by appending `/` and the orbit number to the star. For
example, `12-13-14A/5` is the fifth orbit of star `12-13-14A`.

Additional information about planets and habitability is defined in the following references:

- [Planets]({{< relref "planets.md" >}})
- [Habitability]({{< relref "habitability.md" >}})

### 11th Orbit

A `JUMP` order names a [solar system]({{< relref "#solar-systems" >}}) only — it
cannot name a star or an orbit. The engine still needs a fixed address for an
arriving ship, so it places the ship in **orbit 11** of the arrival star. The
turn report writes the address as `<star>/11`, for example `00-00-00A/11`.

Orbit 11 is a bookkeeping slot, not a planetary orbit:

- It never holds a planet; planetary orbits run 1 through 10.
- It holds only ships that have arrived by an interstellar jump.
- A ship in orbit 11 must move to one of orbits 1 through 10 before it can act
  at any planet in the system.

## Turn Length

One turn equals one quarter of a Galactic standard year.

Four turns equal one Galactic standard year.

## Constraints

- The cluster contains exactly 100 solar systems.
- Solar system coordinates range from `00-00-00` to `30-30-30`.
- A solar system contains one or more stars.
- Multiple stars within a solar system share identical coordinates.
- Each star contains exactly 10 planetary orbits, numbered `1` through `10`, plus orbit `11` as a non-planetary arrival slot.
- Each occupied planetary orbit contains exactly one planet.
- Each star is identified by its system coordinates plus a letter suffix (`A`, `B`, `C`, …); the suffix is required even for single-star systems.
- An orbit is addressed as `<star>/<orbit>`, for example `12-13-14A/5`.
