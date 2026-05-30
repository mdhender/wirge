---
title: Exploration
weight: 100
---

Exploration covers how ships move between orbits and systems, and how a nation
learns a planet's contents through a probe or a survey.

## Ship movement

A ship moves between locations by jumping. Each jump is interplanetary (within a
system) or interstellar (between systems); both kinds are made by
[hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}}) (`HDRV`), which set
jump range, fuel use, and the rule that a jump cannot end in deep space. Holding
position in orbit and maneuvering in combat are functions of
[space drives]({{< relref "ship-systems.md#space-drives" >}}) (`SDRV`), not
hyperdrives.

{{< callout type="warning" >}}
**TODO:** Ship movement during combat is a separate, tactical case owned by the
Combat reference page, which is not yet converted. Link it here once it exists.
{{< /callout >}}

### Interplanetary movement

A jump within a system is always treated as **0.1 light years** in distance. A
ship may jump from one orbit to another within the system. For jump range, fuel,
and the deep-space rule, see
[Hyperdrives]({{< relref "ship-systems.md#hyperdrives" >}}).

### Interstellar movement

An interstellar jump may start from **any orbit** and ends automatically in the
[11th orbit]({{< relref "game-setup.md#11th-orbit" >}}) of the target system. The
distances for interstellar jumps come from the
[Star List]({{< relref "game-setup.md#star-lists" >}}).

{{< callout type="info" >}}
**Movement between stars of one system.** A jump between two stars of the same
[multi-star system]({{< relref "game-setup.md#solar-systems" >}}) (a binary or
trinary, whose stars share one set of coordinates) is written as an interstellar
jump but is treated as **0.2 light years** in distance. The order specifies the
orbit in the destination star, which must be an occupied orbit; the ship does not
arrive in the 11th orbit.
{{< /callout >}}

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
