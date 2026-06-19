---
title: Exploration
weight: 100
---

Exploration covers how ships move between orbits and systems, and how a nation
learns a planet's contents through a probe or a survey.

## Ship movement

A ship moves between locations by making a **hyperdrive hop**. Each hop is
interplanetary (within a system) or interstellar (between systems); both kinds are
made by [hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}}) (`HDRV`), which
set hop range, fuel use, and the rule that a hop cannot end in deep space. Holding
position in orbit and maneuvering in combat are functions of
[space drives]({{< relref "ship-systems.md#space-drives" >}}) (`SDRV`), not
hyperdrives.

{{< callout type="warning" >}}
**TODO:** Ship movement during combat is a separate, tactical case owned by the
Combat reference page, which is not yet converted. Link it here once it exists.
{{< /callout >}}

### Interplanetary movement

A [`move` order]({{< relref "writing-orders.md#in-system" >}}) stays within a
single system, and its distance depends on the geometry. A hop between orbits of
the same star is treated as **0.1 light years**; a hop between two stars of a
multi-star system (see the note below) is treated as **0.2 light years**. There is
one fuel rule for both — a hyperdrive burns fuel in proportion to the distance
flown — so the longer hop simply costs more. For that rule, range, and the
deep-space rule, see
[Hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}}).

{{< callout type="info" >}}
**Movement between stars of one system.** The stars of a
[multi-star system]({{< relref "game-setup.md#solar-systems" >}}) (a binary or
trinary, whose stars share one set of coordinates) belong to a single system, so
a ship travels from one star to another with a `move` order, naming the
destination star and orbit — **not** a `jump`, which targets a different system by
ID and cannot name an orbit. The destination orbit must be an occupied orbit, and
the ship does not arrive in the 11th orbit. The hop covers more ground than a move
within one star's orbits, so it is treated as **0.2 light years** rather than 0.1,
and the [hyperdrive fuel rule]({{< relref "ship-systems.md#hyperdrives" >}})
charges for that greater distance.
{{< /callout >}}

### Interstellar movement

An interstellar [`jump` order]({{< relref "writing-orders.md#between-systems" >}})
may start from **any orbit** and ends automatically in the
[11th orbit]({{< relref "game-setup.md#11th-orbit" >}}) of the target system. The
distances for interstellar jumps come from the
[Star List]({{< relref "game-setup.md#star-lists" >}}). For why arrival lands in
that slot and what its design implies, see
[The Eleventh Orbit]({{< relref "../explanation/the-eleventh-orbit.md" >}}).

## Probes

A probe is executed by [sensors]({{< relref "ship-systems.md#sensors" >}})
(`SEN`) on a ship or colony; see Sensors for the probe rate and sensor mechanics.
A probe reports on **any planet in the same system**:

- orbiting ships — count, approximate mass, and ID numbers;
- orbiting colonies — count, approximate mass, and ID numbers;
- surface colonies — count, mass, and ID numbers;
- natural-resource [deposits]({{< relref "planets.md#natural-resources" >}}) —
  type and **approximate** quantity of each;
- the planet's [habitability number]({{< relref "habitability.md" >}}) (HN).

A probe's quantities are approximate, in contrast to the exact figures a survey
returns.

### Approximation

Probe and sensor reports give certain values not exactly but as the **log base
10** of the actual number:

| Actual mass / quantity | Reported approximation |
| ---------------------- | ---------------------- |
| 0 – 9                  | 0                      |
| 10 – 99                | 1                      |
| 100 – 999              | 2                      |
| 1,000 – 9,999          | 3                      |
| 10,000 – 99,999        | 4                      |
| 100,000 – 999,999      | 5                      |
| 1,000,000 – 9,999,999  | 6                      |

The pattern continues for larger magnitudes — each further row is one more power
of ten. This is the convention behind the approximate quantities a probe reports,
in contrast to the exact figures a [survey](#surveys) returns.

## Surveys

Any ship or colony may survey the **planet it is located at**. A survey reports
the number of natural-resource [deposits]({{< relref "planets.md#natural-resources" >}}),
where they are located, their type, and the **exact** number of resource units in
each deposit. A survey requires one
[transport]({{< relref "ship-systems.md#transports" >}}) (`TPT`) and one
professional unit ([`PRO`]({{< relref "units.md#population-units" >}})), and
completes in one turn.
