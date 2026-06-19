---
title: The Eleventh Orbit
weight: 60
---

Every solar system in the cluster has one address that points to no planet and
never will. Orbit 11 — written `<star>/11` — is not a world, not a slot a planet
can form in, not even a position the cluster generator fills. It is pure
bookkeeping: a single fixed place the engine keeps so that a ship arriving from
another system has somewhere definite to be. Nearly everything that surprises
players about interstellar travel — why a jump can't aim at a planet, why crossing
between stars costs double, why a just-arrived fleet is briefly hard to touch —
falls out of that one design choice. This page is about why the slot exists and
what its existence implies. The mechanics themselves live in
[11th Orbit]({{< relref "../reference/game-setup.md#11th-orbit" >}}); here we ask
what it really is.

## An address, not a world

[Coordinates and Locations]({{< relref "coordinates-and-locations.md" >}}) describes
how a place is named in three nesting levels — system, star, orbit — each suffix
narrowing the address. Orbit 11 borrows the finest of those, the `/n` orbit
notation, but quietly breaks its meaning. Orbits 1 through 10 are planet slots: a
real position around a star where a world may sit. Orbit 11 is a position only in
the sense that it is a string the engine can write down. No planet is ever
generated there, nothing can be built there, and it never appears on the map as
terrain. It exists the way a post-office box exists — not a building, just an
address that mail can be sent to.

That distinction is the key to everything below. Because orbit 11 is an address
rather than a place, it can do things a planet's orbit cannot: belong to no star in
particular, hold ships but never a world, and be reached by exactly one means.

## Why a jump needs it

A [`jump` between systems]({{< relref "../reference/writing-orders.md#between-systems" >}})
names a **system only** — `4-6-19`, with no star and no orbit. The
[Coordinates]({{< relref "coordinates-and-locations.md" >}}) page explains the
counter-intuitive half of this: the longer journey takes the shorter address. But
that economy creates a problem the engine has to solve. After the jump resolves,
the ship has to be *somewhere*, and the order gave it no star and no orbit to aim
at. The engine cannot simply drop it at a planet — the player never chose one, and
any planet it picked might be empty, occupied, or hostile.

So the engine answers the question the order left open with a place that always
exists and belongs to no planet: orbit 11. Because the order named no star, the
arrival resolves to the system's first star by convention, and the report writes
the address against it — `4-6-19A/11`. The ship is now in the system but *not yet
at* any planet, which is exactly the honest description of what a system-only jump
can promise. The slot exists to make "arrived at the system" a state the engine can
represent.

## One hub for the whole system

Here is the subtlety that the `A` in `4-6-19A/11` hides: `A/11`, `B/11`, and
`C/11` are not three places. They are one. A system has a single orbit 11, shared
by all its stars — conceptually lying *in every star's orbits at once*. The
letter in the written address is a labelling convention, not a location; whichever
star you name, you are pointing at the same hub.

{{< callout type="warning" >}}
**Differs from the rule book.** This shared hub is a deliberate reworking of an
older idea. The 1978 rule book labelled no stars and had no `/11` slot; it told
co-located stars apart by saying each one *occupied the others' eleventh orbit* — a
reciprocal trick, N stars each notionally sitting in the others' books. The modern
engine keeps the eleventh-orbit name but collapses that reciprocity into a single
shared slot per system, reachable only by jump. The lettered-star convention that
replaced the original trick is discussed under
[Identifying a star]({{< relref "../reference/game-setup.md#identifying-a-star" >}})
and [Coordinates and Locations]({{< relref "coordinates-and-locations.md#why-the-star-letter-is-always-required" >}});
orbit 11 is what became of the mechanism those replaced.
{{< /callout >}}

Treating the hub as one shared position rather than one-per-star is not just
tidiness. It is what makes the next consequence — the cost of moving between stars
— come out right.

## Why crossing stars costs double

The hub is best pictured as the seam that stitches a multi-star system's stars
together: a single waypoint sitting one short step — 0.1 light years — from every
star's planetary orbits. Read the
[multi-star system]({{< relref "../reference/game-setup.md#solar-systems" >}})
geometry through that picture and the movement costs explain themselves.

- A [`move`]({{< relref "../reference/exploration.md#interplanetary-movement" >}})
  between two orbits of the **same** star is a single step across that star's
  neighbourhood — 0.1 light years.
- A `move` between planets on **different** stars has to cross the seam: out from
  the first star to the shared hub, then down from the hub to the second star. Two
  steps, and so 0.2 light years.
- A ship that *begins* in orbit 11 is already sitting on the seam, so it reaches
  any star's planet in a single step.

The doubled cost of a cross-star hop, and the matching jump in
[fuel]({{< relref "../reference/ship-systems.md#hyperdrives" >}}) that goes with the
greater distance, is therefore not an arbitrary surcharge for leaving a star. It is
the shape of a shared hub showing up in the distance travelled: you pay for two
legs because the only path between two stars runs through the one point they have
in common. (The exact distances and the single fuel rule that turns them into a
fuel bill belong to the reference pages; the point here is *why* the numbers take
the shape they do.)

## A one-way membrane

You can enter orbit 11 by exactly one means — a `jump` from another system. A
[`move`]({{< relref "../reference/exploration.md#interplanetary-movement" >}}) can
never target it, because a move names a planetary orbit from 1 to 10 and the hub is
none of those. This makes the slot a one-way membrane. Interstellar arrivals flow
*in* through it and then down to planets; nothing inside the system flows back up.

The implication catches people out: once a ship has moved down from the hub to a
planet, it cannot stroll back to orbit 11. The only route back to the hub is to
leave the system entirely and jump in again. Orbit 11 is an entrance, not a
corridor — a door that opens inward from interstellar space and cannot be reopened
from within.

## Arrival, not forced transit

The reference notes that a ship in orbit 11 *must* move to one of orbits 1 through
10 before it can act at a planet, which is easy to misread as a rule that the ship
must move at all. It isn't. The requirement attaches to *acting at a planet* — a
surface or colony action — not to occupying the slot. A ship with no planetary
business this turn is free to stay in the hub indefinitely.

That permission is what turns orbit 11 from a turnstile into a usable position. The
slot is not a transit lounge you are hurried through; it is somewhere a ship can
choose to remain. The two sections that follow are about what remaining there buys
you.

## Scouting from the hub

Not every action needs a planet underfoot. The two reconnaissance actions —
[survey]({{< relref "../reference/exploration.md#surveys" >}}) and
[probe]({{< relref "../reference/exploration.md#probes" >}}) — are remote sensing:
they read a system rather than touch it, and so they run from orbit 11 just as well
as from a planetary orbit. Surface and colony actions, which need the ship actually
*at* a world, do not. So the hub is a natural reconnaissance perch: a ship can jump
in, read what the system holds, and decide what to do before committing to any
planet. Because surveys and probes resolve earlier in the turn than ship movement
(see [Sequence of Turn Execution]({{< relref "../reference/sequence-of-turn-execution.md" >}})),
a ship can scout from the hub on the same turn it intends to move onward.

{{< callout type="warning" >}}
**TODO — reference gap.** The reference pages do not yet state plainly that survey
and probe may be performed *from* orbit 11. The
[Probes]({{< relref "../reference/exploration.md#probes" >}}) description ("any
planet in the same system") is already consistent with it, but
[Surveys]({{< relref "../reference/exploration.md#surveys" >}}) is framed as
surveying "the planet it is located at," which predates this clarification and does
not obviously admit a ship sitting in a slot that holds no planet. The
orbit-11 vantage should be reconciled in those reference pages; this note flags the
gap rather than resolving it here.
{{< /callout >}}

## A perch, not a fortress

The most interesting consequence of the membrane is tactical. A ship parked in
orbit 11 cannot be reached by the system's own ships, because they would have to
`move` onto the hub and nothing can move onto the hub. An attacker who wants to
reach it has no in-system route at all: it must leave the system and jump back to
land in orbit 11 alongside its target.

Two facts about timing then work in the perched ship's favour.
[Combat resolves early in the turn and movement late]({{< relref "../reference/sequence-of-turn-execution.md" >}}) —
combat is the third stage, ship movement the fourteenth — so a ship that jumps in
arrives only at the end of the turn and cannot fight until the *following* turn's
combat. The perched ship therefore gets a full turn's notice: it can jump away or
drop to a planet before the newcomer is able to act.

But the hub is shared, and that is the catch. Two ships that both jump into the
same system land at the same address, and because
[combat happens between ships at the same orbit]({{< relref "../reference/combat.md#description" >}}),
co-arrived jumpers can engage each other. Orbit 11 is safe from everything already
in the system and exposed to everything that follows you in. It is a relatively
safe perch, not a fortress — which is precisely the character a shared, jump-only
arrival slot ought to have.

## The hinge it all turns on

Step back and the eleventh orbit resolves into a single design decision with a long
shadow: *one non-planetary slot per system, shared across its stars, reachable only
by jump.* From that one choice follow the jump-arrival rule (a system-only order
needs a fixed address), the doubled cost of crossing between stars (the only path
runs through the shared seam), the survey-and-probe-but-don't-act distinction
(remote sensing needs the system, action needs the planet), and the perch's odd
safety (unreachable from within, exposed from without). The eleventh orbit is less
a place than a hinge the whole movement system turns on — which is why it repays
understanding well out of proportion to the single line of reference that defines
it.
