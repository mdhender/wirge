---
title: The Production Cycle
weight: 20
---

Three kinds of unit turn inputs into output: [mines]({{< relref "../reference/mining.md" >}})
(`MINE`) pull resources from a deposit, [farms]({{< relref "../reference/farming.md" >}})
(`FARM`) grow food, and factories (`FACT`) manufacture everything else. They look
like three separate systems, but the engine runs them on one shared idea: a unit
makes progress only on turns when its inputs are met, and most output arrives once a
year rather than continuously. Understanding that shared cycle explains why a single
bad turn costs a farm so much more than it costs a mine.

## Why we abstract the inputs

A real farm needs seed, soil, water, and a growing season; a real factory needs
tooling, power, and a supply chain. Modeling all of that would bury the game in
bookkeeping, so we wave it away. Every production unit is reduced to a small,
uniform set of inputs:

- **Management** - `PRO` units are required to manage labor each turn.
- **Labor** — `USK` and/or `AUT` provide the labor each turn.
- **Fuel** — consumed each turn the unit runs.
- **Materials** — metallic and non-metallic resources, consumed only by factories.

This is deliberate hand-wavium. It keeps the interesting decisions — how much labor
to train, where to spend fuel, what to build — without simulating agronomy or
industrial logistics.

## A year is four turns of progress

A turn is a quarter; four turns make a game year. Most production is annual, so the
engine tracks each unit's **work in process** (WIP) as a completion percentage.
Every turn a unit has the inputs it needs, it advances one quarter — adds 25% to its
WIP. Four good turns in a row complete one year's worth of output.

What happens when a turn's inputs fall short is where the three systems diverge, and
that difference is the whole point.

## Mines: paid by the turn

A mine is the simple case — it carries no WIP at all. Each turn it produces a
quarter of its annual output and stops. A turn with too little fuel or labor simply
yields proportionally less that turn, and the next turn starts fresh. Nothing is
banked and nothing is lost; a mine can never fall "behind."

## Farms: a year staked on every turn

A farm behaves as though it spends the whole year growing a single crop. Each turn
with sufficient labor and fuel, the farm unit adds 25% to its WIP; after four such
turns it harvests, delivering the full annual yield at once and returning to 0%.

The catch is the failure mode. **A turn without enough inputs resets that farm unit
to 0%.** It does not pause — it loses everything it had grown and starts the year
over. A shortage in the farm's fourth quarter, one turn short of harvest, throws away
nearly a full year of food. This is why a fuel or labor gap is far more punishing for
farms than for mines, and why keeping farms fed is a standing obligation, not a
turn-to-turn optimization.

## Factories: idle until supplied, then patient

A factory adds one more input — materials — and one more state. A factory sits
**idle** until it has materials, labor, and fuel together. The turn an assembly order
is issued, the group is only *formed*: production is calculated earlier in the turn,
so the new group does nothing yet. On the next turn it claims its inputs, consumes the
materials to open the work at 0%, and advances it 25% each turn it stays supplied.
When the work reaches completion it is delivered to cargo and the group starts the
next item. See [Manufacturing]({{< relref "../reference/manufacturing.md" >}}) for
factory-group labor and build costs.

So an order issued on turn 1 delivers on turn 5:

| Turn | What the factory does                                |
| ---- | ---------------------------------------------------- |
| 1    | Assembly order processed; group formed (no work yet) |
| 2    | Claims inputs; opens the work and advances it to 25% |
| 3    | 25% → 50%                                            |
| 4    | 50% → 75%                                            |
| 5    | 75% → complete; delivered to cargo; next item begins |

An `ASSEMBLE LSP-2` issued on turn 1 therefore yields its first life-support unit on
turn 5, the next on turn 9, the next on turn 13, and so on every fourth turn.

Crucially, a factory **does not reset on a shortage the way a farm does.** A turn
without labor or fuel just fails to advance: the WIP holds where it is and the
delivery slips by the missed turns. The factory waits rather than starting over.

## When a shortage splits a group

A group is not a single ledger. Every unit in it carries its own WIP, so a group's
progress is really the sum of many individual clocks. That matters because shortages
rarely land evenly: there may be enough fuel and labor to run some of a group's units
but not all of them. The engine runs as many units as the available inputs cover and
leaves the rest unfed for the turn.

Since the unfed units then react according to their kind — farms reset to 0%,
factories hold where they are — a group that has weathered one or more shortages can
show its units spread across every stage at once. A 1,600-unit farm group might
report 100 units at 75%, 500 at 50%, and 1,000 at 0%, each cohort now harvesting on
its own schedule. What looks like one group is, after a shortage, several
populations of units at different points in the cycle.

Which units receive the scarce inputs is not arbitrary: the engine assigns them by a
fixed priority — by group number, then by how close the work is to finishing, then by
technological level — so the outcome is repeatable rather than random. See
[Shortages]({{< relref "../reference/shortages.md" >}}) for the full allocation rules
and worked examples.

## The three failure modes, side by side

The shared cycle, with three different answers to "what if a turn comes up short,"
is the heart of production planning:

| Unit   | Output rhythm        | A turn with too few inputs                       |
| ------ | -------------------- | ------------------------------------------------ |
| `MINE` | Every turn           | Less output that turn; no lasting effect.        |
| `FACT` | Once every four turns | Pauses; delivery slips by a turn, WIP preserved. |
| `FARM` | Once a year          | **Resets to 0%; up to a year's progress lost.**  |

Every input — managers, labor, fuel, materials — is allocated to mines first, then
farms, then factories, so a shortage of any kind idles the factories first. That is
fortunate, because factories suffer least: they merely pause. Farms suffer most — an
idle farm loses its year — but they sit second in line, ahead of the factories, so
the priority order shields the units with the harshest failure mode. Planning labor
and fuel is about making sure a shortage never cuts deep enough to reach them.
