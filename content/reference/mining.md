---
title: Mining
weight: 58
---

**Mining** extracts natural resources from a planet's
[deposits]({{< relref "planets.md#natural-resources" >}}) — FUEL, GOLD, METS, and
NMTS. A player assigns [mine units]({{< relref "units.md#production" >}}) (`MINE`)
to a deposit, which both grants control of that deposit and produces resources from
it each turn.

Mining can be done only by a **surface colony**. Ships and orbiting colonies cannot
mine.

## Deposits

A deposit is a body of a single resource on a planet's surface. Deposits are
located on the surfaces of terrestrial planets, on asteroids, or on the moons of
gas giants — never in orbit. A player learns a planet's deposits, their type, and
their size from a [probe or survey]({{< relref "planets.md#learning-about-a-planet" >}}).

## Mine groups

A **mine group** is a set of `MINE` units assigned to a single deposit. A group may
contain mine units of **different technological levels** — for example, 200 `MINE-1`
and 50 `MINE-2` working the same deposit.

There is a **one-to-one** relationship between mine groups and deposits: each
deposit may have at most one mine group, and each mine group works exactly one
deposit. A *mining change order* assigns mine units to a deposit (and so claims
control of it); assembly orders may add further mine units to an existing group.

Each mine group has:

| Field          | Description                                            |
| -------------- | ------------------------------------------------------ |
| `group_number` | Identifies the group within the colony.                |
| `deposit`      | The deposit being mined.                               |
| `units`        | The `MINE` units in the group, by technological level. |
| `quantity`     | The number of `MINE` units in the group, by technological level. |

{{< callout type="info" >}}
**Group number** is never reused.
{{< /callout >}}

## Extraction

A MINE unit **extracts** ore in proportion to its technological level. Annual
extraction is **100 × TL** mass units; because mines work every turn, the
extraction per turn is one quarter of that, **25 × TL** mass units. The resource
is whatever the assigned deposit holds.

| Tech level | Annual extraction (MU) | Extraction per turn (MU) | Fuel per turn |
| ---------- | ---------------------- | ------------------------ | ------------- |
| MINE-1     | 100                    | 25                       | 0.5           |
| MINE-2     | 200                    | 50                       | 1.0           |
| MINE-3     | 300                    | 75                       | 1.5           |
| MINE-4     | 400                    | 100                      | 2.0           |
| MINE-5     | 500                    | 125                      | 2.5           |
| MINE-6     | 600                    | 150                      | 3.0           |
| MINE-7     | 700                    | 175                      | 3.5           |
| MINE-8     | 800                    | 200                      | 4.0           |
| MINE-9     | 900                    | 225                      | 4.5           |
| MINE-10    | 1,000                  | 250                      | 5.0           |

These figures are the **gross** amount a group pulls from the deposit. How much
of it becomes usable product depends on the deposit's yield.

## Yield

Every deposit has a **yield** — a percentage fixed when the planet is generated
(see [natural resources]({{< relref "planets.md#natural-resources" >}})). The
amount a group **produces** in a turn, and delivers to cargo, is its extraction
multiplied by the deposit's yield:

> produced = extracted × yield

The deposit's remaining quantity then drops by the amount **produced**, not the
amount extracted. For example, a group that extracts 1,000 MU from a deposit with
a 10% yield produces **100 MU**, and the deposit's quantity falls by 100. A
low-yield deposit therefore both produces less each turn and lasts far longer
before it is exhausted — which is why an asteroid (large quantity, low yield) is a
slow but durable mine.

A mine begins producing the turn after it is assembled into a group. It carries no
multi-turn pipeline: each turn the engine delivers that turn's product straight to
cargo (see [Shortages]({{< relref "shortages.md#mines-the-quarterly-wink" >}})).

## Inputs

### Labor

Each MINE unit requires, regardless of group size:

- 3 unskilled worker units (`USK`), or the equivalent in
  [automation units]({{< relref "ship-systems.md#automation" >}}) (`AUT`), and
- 1 professional unit (`PRO`).

### Fuel

Each MINE unit consumes **0.5 × TL** fuel units per turn (see the table above). Fuel —
like every production input — is allocated to MINE and FARM units **before** FACT
units, so a shortage starves the FACT units first. See
[Shortages]({{< relref "shortages.md#allocation-priority" >}}) for the full rules.

{{< callout type="info" >}}
MINE units always require fuel. The solar-power exemption that lets some FARM and
FACT units run without fuel applies only to *orbiting* colonies within the fifth
orbit — and mining is surface-only, so MINE units can never qualify.
{{< /callout >}}

## Shortages

A shortage of fuel or labor reduces the number of mine units that run that turn,
dropping the lowest-priority units first; extraction — and so product — falls with
the active count, but only for that turn. There is no reset penalty — a mine carries no work between turns,
so production returns to full rate as soon as its inputs are restored.

This is gentler than the other production units: a short turn forfeits a FARM group's
crop (its idle units reset to 0%) and slips a FACT group's delivery, while a MINE
group simply produces less that turn. See [Shortages]({{< relref "shortages.md" >}})
for the shared allocation rules.
