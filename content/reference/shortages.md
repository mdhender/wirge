---
title: Shortages
weight: 75
---

When a colony or ship cannot supply everything its production units need in a turn,
the engine resolves the shortfall the same way for mines, farms, and factories: it
works out how many units it can actually run, hands the scarce inputs to them by a
fixed priority, and then applies a consequence that depends on the unit type. This
page describes that shared process and the points where the three types diverge. For
the conceptual picture behind it, see
[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}).

## Active and total units

- **Total units** are all the units assigned to a group.
- **Active units** are the subset that receive *all* of their required inputs this
  turn. Only active units do work; an idle (non-active) unit advances nothing.

A shortage of any single input reduces the active count, and that is the lever
through which every shortage takes effect.

## What a group needs

The inputs differ by type. Factories consume materials and scale their labor with
group size; mines and farms take no materials and use a flat labor ratio.

| Input               | Factory (`FACT`)                         | Mine (`MINE`)   | Farm (`FARM`)   |
| ------------------- | ---------------------------------------- | --------------- | --------------- |
| Materials (METS/NMTS) | 20 × TL MU per unit per year           | none            | none            |
| Professionals (`PRO`) | by group size (see chart below)        | 1 per unit      | 1 per unit      |
| Labor (`USK`/`AUT`) | 3 per `PRO`                              | 3 per unit      | 3 per unit      |
| Fuel                | 0.5 × TL per active unit                 | 0.5 × TL        | per the [FARM table]({{< relref "farming.md#food-output" >}}) |

A factory group's `PRO` requirement falls as the group grows:

| Factory units in group | `PRO` per unit |
| ---------------------- | -------------- |
| 1 – 4                  | 6              |
| 5 – 49                 | 5              |
| 50 – 499               | 4              |
| 500 – 4,999            | 3              |
| 5,000 – 49,999         | 2              |
| 50,000 +               | 1              |

Within a unit, the engine claims inputs in a fixed order — **materials → `PRO` →
`AUT` → `USK` → fuel** — taking automation before unskilled labor. A factory group's
material claim is **persistent**: once claimed, the materials stay reserved for that
group until they are consumed or the group is shut down, so a later labor or fuel
shortage idles units without releasing their materials.

## Allocation priority

When an input is scarce, the engine decides which units get it — and therefore which
stay active — in this order:

1. **Unit type.** Every input is handed out to **all mining groups first, then all
   farm groups, then all factory groups.** This is not a fuel-only rule — managers,
   labor, fuel, and (for factories) materials all follow the same type order — so a
   shortage of any input idles factories before farms, and farms before mines.
2. **Group number.** Within a type, the senior (lower-numbered) group is served
   first: group 1 before group 2, and so on.
3. **WIP completion.** Within a group, the most-complete work is supplied first —
   3/4 before 1/2 before 1/4, and anything already in progress before starting new
   work.
4. **Technological level.** Within the same completion tier, higher-TL units go
   first.

So the last thing a shortage touches is a senior mining group's nearly-finished,
high-TL work; the first to go idle is a junior factory group's not-yet-started,
low-TL units.

## Reducing the active count

Because the `PRO`, labor, and fuel a group needs all depend on how many units are
active, cutting the active count changes the requirement, which can cut it again. The
engine settles this with a stability loop:

1. Reduce the active count to what the scarce input can support.
2. Recompute the group's `PRO`, labor, and fuel needs against the new active count.
3. Repeat. The active count may only **shrink** within a turn — never grow — until it
   stops changing or reaches zero.

If the active count reaches zero, the group does nothing that turn and no work
advances.

## What happens to an idle unit

This is where the three types part ways:

| Type   | An idle unit's work                                                            |
| ------ | ------------------------------------------------------------------------------ |
| `FACT` | **Holds.** Its WIP stays where it is and resumes when inputs return; delivery slips by the number of missed turns. |
| `MINE` | **Holds** — but a mine carries no standing WIP (see below), so an idle mine simply produces nothing that turn. |
| `FARM` | **Resets to 0%.** The in-progress FOOD is lost and the unit starts its year over. |

Because the allocation priority feeds the most-complete work first, a farm shortage
tends to starve the *youngest* WIP — so the crop closest to harvest is the last to be
sacrificed, and a group that has weathered a shortage can hold cohorts of units
scattered across several completion tiers, each on its own schedule.

## Work in process and timing

All three unit types accrue **work in process** (WIP) at 25% per turn while active —
four active turns complete one year's output. The turn order matters: production is
calculated near the start of a turn (mining first, farming second, manufacturing last),
while assembly orders are processed much later in the same turn. So on the turn an
order is issued the group is only *formed* — it holds no inputs and does no work. The
first 25% lands the **next** turn, and the first delivery comes four turns after that.

A factory building 1,000 `LSP-2` with 50,000 active `FACT-1`, with no shortage:

| Turn | WIP 1/4 | WIP 1/2 | WIP 3/4 | Cargo  | What happened              |
| ---- | ------- | ------- | ------- | ------ | -------------------------- |
| 1    | 0       | 0       | 0       | 0      | Assembly order; group formed |
| 2    | 1,000   | 0       | 0       | 0      | 1st production turn        |
| 3    | 0       | 1,000   | 0       | 0      | 2nd                        |
| 4    | 0       | 0       | 1,000   | 0      | 3rd                        |
| 5    | 0       | 0       | 0       | 1,000  | 4th — delivered            |
| 6    | 1,000   | 0       | 0       | 0      | next batch begins          |
| 9    | 0       | 0       | 0       | 2,000  | second batch delivered     |

The group does **not** finish 250 units a turn. The whole batch of 1,000 moves
together, a quarter of the way each turn, and the full 1,000 lands in cargo on the
fourth production turn — then again every fourth turn after.

Now the same order, but a fuel shortage on turn 3 drops the active count to 25,000
(half), resolved on turn 4:

| Turn | WIP 1/4 | WIP 1/2 | WIP 3/4 | Cargo  | What happened                       |
| ---- | ------- | ------- | ------- | ------ | ----------------------------------- |
| 1    | 0       | 0       | 0       | 0      | Assembly order; group formed        |
| 2    | 1,000   | 0       | 0       | 0      | 1st production turn                  |
| 3    | 0       | 1,000   | 0       | 0      | fuel shortage (25,000 active)        |
| 4    | 0       | 500     | 500     | 0      | shortage resolved                    |
| 5    | 0       | 0       | 500     | 500    | half the batch delivered            |
| 6    | 0       | 0       | 0       | 1,000  | remainder delivered                 |

The shortage splits the batch: half slips a turn and the 1,000 units arrive across
turns 5 and 6 instead of all on turn 5. Note that the holding factory loses no work —
the delivery is only delayed.

## Mines: the quarterly wink

A mine accrues WIP like everything else, but because mining is meant to pay out every
turn rather than once a year, the engine never lets a mine's WIP accumulate. During
the next turn's production stage it "winks" the 25%-complete resource straight to
cargo as a finished resource. A mine group therefore produces **every turn** and never
carries WIP between turns. Each active mine unit delivers a quarter of its annual
output — **25 × TL MU** — per turn. Equivalently, a mine group puts out a quarter of
its combined annual output each turn: a group whose units would yield 5,000 MU a year
delivers 1,250 MU per turn.

Because a mine holds no standing WIP, the WIP-completion step of the allocation
priority has nothing to sort: a mine group is ranked by group number and TL alone.
And since an idle mine has no WIP to lose, "holds" simply means it produces nothing
that turn and resumes at full rate the moment its inputs return.

## Farms: a reset, not a delay

A farm is the harsh case. Each active farm unit advances its FOOD 25% toward harvest,
but a unit that goes idle for even one turn **resets to 0%** and forfeits everything
it had grown — up to a full year's progress if it was nearly ripe. Combined with the
allocation priority, a farm shortage sheds its lowest-progress units first, so a
group that survives a lean turn keeps its near-harvest cohort and loses the youngest.
This is far more punishing than a mine's lost turn or a factory's slipped delivery,
and it is why keeping farms supplied is a standing obligation rather than a
turn-to-turn optimization.
