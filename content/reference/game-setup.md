---
title: Game Setup
weight: 40
---

What a player receives when entering a game of Epimethean Challenge, and the
properties of the cluster, solar systems, and planets that make up the game
board. This page describes the starting state; ongoing play is covered
elsewhere.

## Star lists

Each player receives two lists. The first shows the co-ordinates of every star
in the cluster. The second shows the distances between the player's home system
and all stars within maximum jump range of it. When a player explores a new
solar system, they receive a list of the stars within jump range of that system.

### Co-ordinates

A solar system is designated solely by its co-ordinates, written as three
two-digit numbers ranging from `00` to `30` — for example, `28-02-18`. Stars
that share the same co-ordinates are part of the same solar system:

- Two stars in one system form a **binary** system.
- Three stars form a **trinary** system, and so on.

## Solar systems

### Orbits

Each star has ten orbits, numbered 1 to 10. Orbit 1 is closest to the star and
orbit 10 is farthest from it. Any orbit may be occupied by a planet.

{{< callout type="warning" >}}
**Differs from the rule book.** The original rules gave each star an eleventh
orbit, used only to record the other star(s) of a multi-star system — each star
was said to occupy the others' eleventh orbit. That orbit was a bookkeeping entry
for the original game engine. Our engine keeps a referential link between the
stars in a system instead, so it has no eleventh orbit.
{{< /callout >}}

### Home system

Each player receives a description of their home system, listing the number of
planets it contains, their type, and their orbit positions.

## Planets

Each occupied orbit contains a planet, of one of three types, with a
[habitability number]({{< relref "habitability.md" >}}) and a set of natural
resources. See [Planets]({{< relref "planets.md" >}}) for the full description.

## Time scale

One turn equals one quarter of a Galactic standard year.

## Initial turn report

When a player enters a game, they receive an initial turn report — emailed or
downloaded — describing their nation's starting position.
