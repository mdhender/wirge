---
title: Food Strategy
weight: 30
---

Feeding a population is a standing obligation, not a one-time purchase. Every
turn, each ship and colony owes its people a [ration]({{< relref "../reference/food.md" >}})
of food, and the [`RATION` order]({{< relref "../reference/food.md" >}}) is the
only lever a player has over that cost. Cutting the ration saves food, but it
buys that food with two kinds of damage — falling morale and outright
starvation. The interesting decisions in food management are all about *when* and
*how deliberately* a player chooses to take that damage.

## The shortage you see coming is cheaper

The single most important thing to understand about food is that the game
distinguishes between a shortage a player *plans for* and one that simply
*happens*. The mechanics are laid out under
[Starvation]({{< relref "../reference/food.md" >}}); the strategic consequence is
that the same empty larder costs very different numbers of lives depending on
whether the player saw it coming.

When food runs out on its own, the colony is caught feeding everyone a full
ration right up until the stores are gone. The engine then splits whatever food
remains across the whole population, and — because no one organized the
rationing in advance — some of that food is wasted in the scramble. This is an
**unplanned shortage**, and it raises the survival ration from 25% to 35% for
the turn. More food is needed per person to avoid death precisely when there is
least to go around.

A player who anticipates the shortfall and issues a `RATION` order *before* the
stores run dry suffers no such waste. The cut is **planned**: the survival
ration stays at 25%, and the distribution is orderly. The food delivered may be
identical — the difference is entirely in the coordination.

## The arithmetic of acting early

Consider two colonies that each end up feeding their people only a fifth of a
full ration. The first coasted at 100% until the food ran out, and the engine
forced its effective ration down to 20%. The second foresaw the shortage and
ordered `RATION 20%` ahead of time. Both deliver the same food; the outcomes are
not the same.

The planned colony starves against the normal survival ration:

```
P = (0.25 − 0.20) / 0.25 = 0.20
```

The unplanned colony starves against the raised survival ration:

```
P = (0.35 − 0.20) / 0.35 ≈ 0.43
```

Twenty percent lost versus forty-three percent — more than double, for the same
amount of food in the storehouse. The only thing the second colony did wrong was
fail to give the order in time. Anticipation is not a marginal optimization
here; it is the difference between a hard turn and a catastrophe.

## Spending lives to buy time

Once a player accepts that some starvation is unavoidable — a failed harvest, a
long voyage, a blockade — the question stops being *whether* to lose population
and becomes *how to lose the fewest over the whole crisis*. A deliberately deep
cut, taken early, is often the most humane choice available.

Coasting at a full ration until the stores empty spends the food fastest,
reaches the larder's bottom soonest, and then pays the unplanned-shortage
penalty on every turn that the famine continues. Cutting early does the
opposite: it stretches the remaining food across more turns, keeps every
starving turn on the cheaper 25% survival ration, and lets the player choose a
sustainable level rather than have one forced on them. The population lost to a
single controlled cut is smaller than the population bled away turn after turn by
an uncontrolled one.

This is the grim logic behind a famine ration: accept a smaller, deliberate loss
now so that the rest of the population survives until the farms recover —
sacrificing some of the tribe to carry the rest through to spring. The game does
not let a player aim that loss at any particular group; rations are always
[divided equally]({{< relref "../reference/food.md" >}}) and starvation takes its
percentage across the board. What the player controls is the *size* of the loss
and *when* it falls, not who bears it.

## Why thrashing the ration has its own cost

Starvation is the sharper of the two penalties, but morale is the more
persistent one. Underfeeding a population lowers its morale, and — unlike
starvation, which is paid once — that decline lingers and recovers only slowly
and incompletely when the ration is restored. A player who yo-yos the ration up
and down each turn pays the morale cost repeatedly while never holding a level
long enough to benefit from it.

The lesson reinforces the one above: pick a ration the colony can sustain
through the lean turns and hold it, rather than reacting turn by turn. A single,
planned, sustained cut is gentler on both morale and population than a series of
panicked adjustments.

## Famines rarely arrive alone

A food crisis is often the visible symptom of a deeper production problem. Farms
are the harshest unit in the [production cycle]({{< relref "production-cycle.md" >}}):
a single turn without enough fuel or labor resets a farm to zero and throws away
up to a year's harvest. The fuel or labor gap that idles a colony's farms is
therefore likely to *cause* the food shortage in the first place — and to keep
causing it, turn after turn, until the underlying shortage is resolved.

This is why food planning cannot be separated from production planning. Keeping
farms fed with fuel and labor is the real defense against famine; the `RATION`
order is only the tool for surviving the famine that slips through. The player
who watches the farm inputs, and who cuts rations early when the harvest does
fail, will weather a bad year that ruins a less attentive neighbor.
