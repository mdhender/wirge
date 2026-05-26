---
title: Planets
weight: 180
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

A player may establish at most one open colony, one enclosed colony, and one orbiting colony at a single planet, plus any number of ships.
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
contains from 1,000,000 to 99,999,999 units of a single resource:

| Resource | Use                                      |
| -------- | ---------------------------------------- |
| **GOLD** | Economic exchange.                       |
| **FUEL** | All production and transportation.       |
| **METS** | All metallic substances other than gold. |
| **NMTS** | All non-metallic substances.             |

## Learning about a planet

A player does not automatically know a planet's contents. Two methods reveal
them:

- A **probe** reports any planet in the same system: the ships and colonies there
  (orbiting and on the surface), their mass and ID numbers, the planet's natural
  resource deposits with their type and approximate quantity, and its habitability
  number.
- A **survey** is conducted by a ship/colony at the planet itself. It reports
  the number of natural resource deposits, where they are located, their type, and
  the exact number of resource units in each. A survey takes one TPT unit and
  one PRO unit and completes in one turn.

## Control

A planet may be controlled by a player who establishes an orbiting or surface
colony — or a trade station — there and declares control. Control may be
contested, granted by diplomacy, or relinquished; see Control of Planets for the
full rules.

{{< callout type="warning" >}}
**TODO:** Wire up the "Control of Planets" link above with a `relref` once that
reference page exists.
{{< /callout >}}
