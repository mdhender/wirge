# Planet Generation v0

## Overview

The planet generator accepts a fixed set of ten orbital slots.

```go
func GeneratePlanets(occupied [10]bool, planetRNG RNG) []Planet
```

Where:

- occupied[i] == true means orbit i+1 contains a planet.
- occupied[i] == false means orbit i+1 is empty.

Generation order:

1. Assign planet types.
2. Generate habitability.
3. Generate resource deposits.
4. Apply deposit conversion rules.

## Planet Types

Types:

- rocky
- gas-giant
- asteroid-belt

### Special Rules

- If exactly one orbit is occupied, that planet is a gas-giant.
- If orbit 10 is occupied and orbit 9 is empty, orbit 10 is an asteroid-belt.

### General Assignment

Orbits 1-3:

- Always rocky.

Orbits 4-6:

- Roll 1d3.
- 1-2 = rocky
- 3 = gas-giant

Orbits 7-10:

- Normally gas-giant.
- If the next inner orbit is empty, use asteroid-belt instead.

## Habitability

Habitability ranges from 0..25.

### Rocky Planets

#### Habitable Gate

| Orbit | Chance |
| ----- | ------ |
| 1     | 10%    |
| 2     | 20%    |
| 3     | 40%    |
| 4     | 80%    |
| 5     | 40%    |
| 6     | 20%    |
| 7     | 10%    |
| 8     | 5%     |
| 9     | 2%     |
| 10    | 1%     |

Failed gate => habitability = 0.

#### Value

Hmax table:

| Orbit | Hmax |
| ----- | ---- |
| 1     | 8    |
| 2     | 16   |
| 3     | 22   |
| 4     | 25   |
| 5     | 22   |
| 6     | 16   |
| 7     | 8    |
| 8     | 4    |
| 9     | 2    |
| 10    | 1    |

Roll:

b = 3d6 - 3

Compute:

habitability = floor(b \* Hmax / 15)

If habitability == 0 after passing the gate, set it to 1.

### Gas Giants

Gate chance is half the rocky chance.

Value:

h = 2d4 - orbit

If orbit >= 5:

h += 1d4

Clamp to 0.

If the gate passed and h == 0, set h = 1.

### Asteroid Belts

Habitability = 0.

## Resources

Resource types:

- METALLICS
- NON_METALLICS
- FUEL
- GOLD

### Deposit Counts

Rocky:

- 1d12 + 2

Gas Giant:

- 1d18 + 6

Asteroid Belt:

- 1d10 + 6

### Deposit Type Selection

Rocky:

- 01 GOLD
- 02-16 FUEL
- 17-61 METALLICS
- 62-100 NON_METALLICS

Gas Giant:

- 01 GOLD
- 02-66 FUEL
- 67-83 METALLICS
- 84-100 NON_METALLICS

Asteroid Belt:

- 01-02 GOLD
- 03-12 FUEL
- 13-77 METALLICS
- 78-100 NON_METALLICS

### Quantity

METALLICS, NON_METALLICS, FUEL:

- 99d1,000,000

GOLD:

- 9d1,000,000

### Yield

METALLICS:

- 1d10

NON_METALLICS:

- 1d10

FUEL:

- 1d6

GOLD:

- 1d3

### Resource Modifiers

Asteroid Belt GOLD:

- Quantity +25% to +75%
- Yield = 1

Gas Giant FUEL:

- Quantity +1% to +25%

### Yield Modifiers

Asteroid Belt:

- yield = ceil(yield / 3)

Gas Giant:

- yield = floor(yield \* 1.25)

### GOLD Deposit Limit

Maximum 4 GOLD deposits.

Convert excess deposits starting with the smallest quantity \* yield.

Yield 1 => FUEL
Yield 2 => METALLICS
Yield 3 => NON_METALLICS

quantity \*= 10

### FUEL Deposit Limit

Maximum 12 FUEL deposits.

Convert excess deposits starting with the smallest quantity \* yield.

Yield 1,3,5 => METALLICS
Yield 2,4,6 => NON_METALLICS

## Specification compliance (v0 review, 2026-05-26)

Reviewed this design against the authoritative reference docs
(`content/reference/planets.md`, `habitability.md`, `mining.md`). The docs win
when they disagree with the engine; the items below are changes the **pyre**
generator must make to comply, plus a couple of spec ambiguities to resolve
first.

### Engine must change

1. **Gas-giant habitability must be able to reach 12.**
   `habitability.md` sets the gas-giant HN range at 0–12, but the current
   formula (`h = 2d4 − orbit`, plus `1d4` when orbit ≥ 5, clamp to 0) peaks at
   **7** — at its best orbit (5). Per-orbit maxima today: orbit 4 → 4,
   orbit 5 → 7, 6 → 6, 7 → 5, 8 → 4, 9 → 3, 10 → 2; the singleton-gas-giant case
   (orbits 1–3) also tops out at 7. The formula needs revising so a gas giant
   can produce an HN up to 12. (New formula TBD by the designer.)

2. **Every deposit must hold at least 1,000,000 units.**
   `planets.md` / the manual require each deposit to contain 1,000,000–99,000,000
   units. The current rolls violate the floor:
   - METS/NMTS/FUEL `99d1,000,000` can land well below 1,000,000.
   - GOLD `9d1,000,000` can land below 1,000,000 *and* caps at ~9,000,000,
     short of the spec maximum.
   Re-scale these so all deposits fall inside the stated band.

### Documentation gap (track separately, not an engine fix)

3. **Deposit yield is generated but undocumented in mining.**
   This design assigns each deposit a yield (METS/NMTS `1d10`, FUEL `1d6`,
   GOLD `1d3`, with asteroid/gas-giant modifiers), matching the "Yield" column
   in the manual's Appendix I sample sheet. But `mining.md` derives output
   solely from mine tech level (`25 × TL` MU/turn) and never references deposit
   yield. `mining.md` must eventually document how yield factors into output
   before the generator's yield values mean anything.

### Spec ambiguities to resolve first

4. **Deposit maximum quantity disagrees across our own docs.**
   `planets.md` says 99,999,999; the manual says 99,000,000. Pick one before
   fixing item 2 above.

5. **`99d1,000,000` / `9d1,000,000` notation is ambiguous** — 99 dice of
   1..1,000,000, or a single roll up to 99,000,000? Clarify before re-scaling.

### Non-issues (no change needed)

- **40-deposit ceiling is satisfied.** Realized maxima (rocky 14, gas giant 24,
  asteroid 16) stay under the 40 cap. Compliant, though the realized spread is
  far narrower than "up to 40" implies — confirm that's the intended feel.
- **Unreachable rocky table rows.** The rocky habitable-gate and Hmax tables
  list orbits 7–10, but rocky planets are only assigned in orbits 1–6 (7–10 are
  gas-giant or asteroid). Those rows are dead; trim them or leave as-is.
- **Terminology.** Generator uses `rocky`/`gas-giant`/`asteroid-belt`; docs use
  Terrestrial/Gas giant/Asteroid. Internal-only mapping.
