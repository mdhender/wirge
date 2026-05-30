---
title: Coordinates and Locations
weight: 50
---

Almost every order that reaches past a single ship or colony has to say *where*:
where to move, where to take control, where to grant permission to colonize. The
game answers with one addressing scheme — coordinates — that names a place at one
of three levels of precision: a whole system, a single star within it, or one
orbit around that star. Seeing how those levels nest, and which level a given
order expects, clears up most of the confusion around writing locations.

## Three levels of precision

A location is built up in layers, each adding detail to the one before.

- A **system** is three two-digit numbers joined by hyphens, such as `12-13-14`.
  It names a point on the map and nothing finer; a system may hold one, two, or
  three stars. See
  [Cluster]({{< relref "../reference/game-setup.md#cluster" >}}).
- A **star** appends a letter: `12-13-14A` is the first star, `12-13-14B` the
  second, and so on. See
  [Identifying a star]({{< relref "../reference/game-setup.md#identifying-a-star" >}}).
- An **orbit** appends a slash and a number from 1 to 10: `12-13-14A/5` is the
  fifth orbit of star A — the slot a planet sits in. See
  [Stars and Orbits]({{< relref "../reference/game-setup.md#stars-and-orbits" >}}).

Read left to right, each suffix narrows the address: system, then star, then
orbit. Drop a suffix and you have named something larger. So `12-13-14A/5` carries
its whole context in one string — which system, which star, which orbit. The
glossary's [Co-ordinates]({{< relref "../reference/glossary.md" >}}) entry is the
one-line statement of this format; this page is the reasoning around it.

## Why the star letter is always required

The most common surprise is that the star letter is mandatory *even when a system
has only one star*. `12-13-14` and `12-13-14A` are not interchangeable: the first
is the system, the second is its only star. Requiring the letter keeps those two
ideas from blurring, so an order never leaves the engine guessing whether you
meant the system or the star in it.

It is also a deliberate departure from the oldest rule book, which labelled no
stars at all and leaned on an eleventh-orbit trick to tell co-located stars apart.
We adopt the later lettered-suffix convention and make it universal — see the note
under [Identifying a star]({{< relref "../reference/game-setup.md#identifying-a-star" >}}).

## What each movement order expects

Locations get most confusing in movement, because the two kinds of movement want
*different* levels of precision — for a reason rooted in how the engine tracks an
arriving ship. The two even take different order keywords: `move` within a system,
`jump` between systems, so the distinction is visible in the order itself.

A **`jump` between systems** names a **system only**: `4-6-19`, never `4-6-19A` or
`4-6-19A/2`. You cannot choose the star or orbit you arrive at, because you do not
choose it — the engine sets the ship down in a holding slot it calls the
[eleventh orbit]({{< relref "../reference/game-setup.md#11th-orbit" >}}), a
bookkeeping position that exists only to give a just-arrived ship a fixed address.
A ship there is not yet *at* any planet. See
[Interstellar movement]({{< relref "../reference/exploration.md#interstellar-movement" >}}).

A **`move` within a system** names a **star and an orbit**: the ship is already in
the system, so the only open questions are which star and which of its orbits to
head for — which is also why a ship sitting in the eleventh orbit must make such a
move before it can act at any planet.

The rule of thumb is the mirror image of intuition: the *longer* journey (between
systems) takes the *shorter* address (system only), and the *shorter* journey
(within a system) takes the *more specific* one (star and orbit).

## A notation detail worth knowing

An in-system `move` names just the star and orbit in the usual slash form — `A/2` —
and leaves off the leading system coordinates, because the ship is already in that
system. It is the same `star/orbit` pattern as the tail of a fully-qualified
address like `12-13-14A/2`, shortened to what the order still needs to know. See
[Movement orders]({{< relref "../reference/writing-orders.md#movement-orders" >}}).

## Where this shows up

Movement is the headline case, but any order that names a place uses the same
scheme. Declaring
[control]({{< relref "../reference/writing-orders.md#control-orders" >}}) of a
planet, granting
[permission to colonize]({{< relref "../reference/writing-orders.md#colonization-orders" >}}),
naming a planet, or posting
[news]({{< relref "../reference/writing-orders.md#news-release-orders" >}}) to a
market planet all take a star-and-orbit location, written the way an orbit address
always is. The
[General rules]({{< relref "../reference/writing-orders.md#general-rules" >}}) of
the order catalog point back to the
[Co-ordinates]({{< relref "../reference/glossary.md" >}}) entry so the format lives
in one place; this page is the longer answer to *why it looks the way it does*.
