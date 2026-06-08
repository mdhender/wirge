# World Generation — Engine Hand-off

Hand-off note for the engine agent working in the **`pyre`** repo. All paths
below are in the **`wirge`** docs repo (<https://github.com/mdhender/wirge>),
which is the authoritative specification — when code and docs disagree, the docs
win and the engine gets fixed to match.

## Where the world-generation rules live

The full pipeline is published in the reference docs, split across **two
cross-linked sections**, walkable top-down. Generation is deterministic from the
game seed.

### Top half — cluster, systems, stars

**`content/reference/game-setup.md`, `## Generation` section.**

1. **Coordinate space** — coordinates are `XX-YY-ZZ`, each component `00`–`30`,
   giving `31³ = 29,791` possible coordinates. Every system gets a distinct one.
2. **Systems** — exactly **100** systems. Star counts are **fixed, not rolled**:
   5 trinary (3 stars), 10 binary (2 stars), 85 single (1 star). Placed
   **most-constrained-first** (trinary → binary → single). Placement uses a
   **squared-distance spacing rule**: two systems must be at least
   `max(starCountA, starCountB)` apart (compared as squared Euclidean distance
   against the squared separation — 9 / 4 / 1). Algorithm: shuffle all 29,791
   coordinates, then for each system pop candidates until one satisfies the rule;
   rejected candidates are discarded, never reused (guarantees termination).
3. **Stars** — each star shares the system's coordinates, gets a sequence letter
   `A`/`B`/`C` in order, and has ten orbits (1–10). Orbit 11 is **not generated**
   — it's a fixed jump-arrival bookkeeping slot (see `game-setup.md`,
   `### 11th Orbit`).

That section **hands off to the bottom half, run once per star.**

### Bottom half — orbits, planet types, habitability, deposits

**`content/reference/planets.md`, `## Generation` section.**

4. **Occupied orbits** (`### Occupied orbits`) — shuffle orbits 1–10, roll
   `3d4 − 2` (1–10) for the count, take that many. Single-planet override: a
   count of 1 becomes orbit **7**.
5. **Planet types** (`### Planet types`) — assigned by orbit position (1–3
   terrestrial; 4–6 roll 1d3; 7–8 roll 1d20; 9 roll 1d20; 10 always asteroid),
   then two fix-ups in order: **lone outer asteroid** and the **4-5-6 asteroid**.
   Resolve against the *original* occupancy map. The **lone-outer-asteroid**
   fix-up applies only to systems with **two or more occupied orbits** — it never
   touches the single-planet override's lone gas giant in orbit 7.
6. **Habitability** (`### Habitability number`) —
   `HN = clamp(floor((2d15 − penalty) / div), 0, typeMax)`, with per-orbit
   penalty/div tables for terrestrials and gas giants (gas-giant curve is the
   terrestrial curve shifted +3 orbits, div always 2). Asteroids are always HN 0.
   `typeMax` = 25 terrestrial, 12 gas giant.
7. **Resource deposits** (`### Resource deposits`) — generated **after**
   habitability (count depends on HN). Sub-sections: **Count**, **Resource
   type**, **Quantity**, **Yield**, **Gold penalty**. Each attribute rolled per
   deposit; max 40 deposits, quantities in the 1M–99M band.

Supporting attribute definitions the generator references: HN ranges and surface
limits in **`content/reference/habitability.md`**; how starting yield is later
applied in **`content/reference/mining.md`, `## Yield`**.

## Two notes for the engine agent

- **Per-star, not per-system.** The `planets.md` procedure runs once for **each
  star**, not once per system — a binary/trinary system generates planets
  independently for each of its stars.
- **Retired sources.** The old `notes/planet-generator-v0/v1/v2.md` and
  `notes/cluster-generation.md` are obsolete. Don't implement against them — they
  conflict with the published rules. Only `game-setup.md#generation` +
  `planets.md#generation` are authoritative.
