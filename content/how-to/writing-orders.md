---
title: Write a turn's orders
weight: 10
---

This guide shows you how to assemble the orders for one turn — the set-up block, a
complete order file, and several orders working together. It assumes you already
know what you want your nation to do this turn; it does not teach strategy.

For each order's format, fields, and constraints, see the
[Writing Orders]({{< relref "../reference/writing-orders.md" >}}) reference. For
the order in which your orders must appear, see
[Sequence of Turn Execution]({{< relref "../reference/sequence-of-turn-execution.md" >}}).

Write your orders in the same order as the Sequence of Play. An order written out
of sequence may not execute — the parser works through your orders stage by stage,
and an order that arrives after its stage has passed is skipped. This guide is
organized around that rule.

## Set up a new ship or colony

A set-up order establishes a new ship or colony from an existing one and transfers
units into it. Because a set-up order lists every unit to transfer, it is usually
too long for one line — so you write it across several, one transfer per line, and
close it with a period:

```text
29, set up, ship, transfer,
STU-2, 50,000,
SDRV-1, 5,
LSP-1, 5,
FOOD, 5,
PRO, 5,
SEN-1, 1,
FUEL, 10,000,
HDRV-1, 61.
```

Start with the establishing ship or colony's ID No., then `set up`, the type
(`ship` or `colony`), and `transfer`. List each unit to transfer as a
`Unit, Quantity` pair on its own line, and end the last line with a period. The
order continues across line breaks until that period, so it is required — it tells
the parser the list is complete. Without it, later orders would be read as more
transfer lines.

Each item is a unit code and a quantity; the `-1` in `SDRV-1` is the unit's TL.

For the bare format, see
[Set up orders]({{< relref "../reference/writing-orders.md#set-up-orders" >}}); for
what a set-up order does, see
[Establishment]({{< relref "../reference/colonies-and-ships.md#establishment" >}}).

## A complete order file

A turn's orders are a plain-text file. Put the header line at the top of each page,
then list your orders in Sequence-of-Play order. Use `//` to leave notes for
yourself; the parser ignores the `//` and the rest of that line.

```text
// Player: Tras-yo of Blenora   Player ID No.: 408   Game No.: 3   Game-turn No.: 17
// Signature: ______________________

// --- Mining and manufacturing ---
83, assemble, MINE-2, 25,680, 148.      // work deposit 148
91, build change, 8, EWP-4.             // build EWP-4 in factory group 8

// --- Logistics ---
22, transfer, 29, SPY, 10.              // hand spies to the scout

// --- Movement ---
29, jump, 4-6-19.                       // jump the scout out of the system

16, ration, 50%.                        // half rations this turn
```

Write the header values — player name, player ID No., game No., game-turn No., and
your signature — on every page, and slash your zeros (0) so they are not read as
the letter O. The game-turn No. is the number of the last print-out you received.

Keep the orders grouped in the order the turn executes them; the next section
covers why that grouping matters. For the header rules and the `//` comment
convention, see
[General rules]({{< relref "../reference/writing-orders.md#general-rules" >}}).

### A full sample order file

The file below is a complete sample exercising most of the order types. It is
grouped by activity, in roughly the order the turn executes; the `//` comments
explain representative lines. Slash your zeros (0) and keep the header on every
page.

```text
// Player: Tras-yo of Blenora   Player ID No.: 408   Game No.: 3   Game-turn No.: 17
// Signature: ______________________

// --- Set up a new ship (transfer block closed by a period) ---
29, set up, ship, transfer,
STU-1, 60,
SDRV-1, 5,
LSP-1, 5,
FOOD, 5,
PRO, 5,
SEN-1, 1,
FUEL, 16,800,
HDRV-1, 61.

// --- Assembly ---
58, assemble, MSL-1, 6,000.            // assemble 6,000 missile launchers
83, assemble, MINE-2, 25,680, 148.     // new mine group working deposit 148
91, assemble, FACT-6, 54,000, CNGD.    // new factory group building CNGD

// --- Build changes ---
16, build change, 8, EWP-4.            // factory group 8 builds EWP-4 (use retool to change an existing product)
17, build change, 1, RSCH.             // switch factory group 1 to research

// --- Mining change ---
348, mining, 18, 92.                   // move mine group 18 to deposit 92

// --- Population, pay, and rations ---
13, draft, SLD, 3,600.                 // raise 3,600 soldiers
78, draft, TRN, 16,880.                // train 16,880 unskilled toward professional
99, disband, SLD, 5,000.               // return 5,000 soldiers to unskilled
38, pay, USK, 0.7.                     // wages are in CNGD
38, pay, PRO, 1.6.
38, pay, SLD, 1.2.
16, ration, 50%.                       // half rations this turn

// --- Logistics ---
22, transfer, 29, SPY, 10.             // hand 10 spy units to ship 29

// --- Market ---
53, buy, PRTO-6, 1, 1,000,000.         // buy one TL-6 prototype
555, buy, STU-1, 25,600, 0.01.         // buy structural units at 0.01 GOLD each
44, sell, SDRV-3, 4, 0.2.              // sell 4 space drives at 0.2 GOLD each
721, sell, PRTO-4, 1, 800,000.         // sell one TL-4 prototype

// --- Survey and probe ---
23, survey.                            // survey the planet this S/C is at
28, probe, A/6.                        // probe orbit 6 of star A
31, probe, A/2, A/4, A/5.              // probe several orbits

// --- Espionage ---
38, check rebels, 1.
38, check for spies, 1.
38, convert rebels, 119.
38, attack spies, 102, 54.             // attack nation 54's spies
38, incite rebels, 998, 54.
38, information, 12, 54.

// --- Combat ---
20, support, 342, 40%.                 // support 342 in its defense
20, support, 342, 45, 35%.             // support 342's attack on 45
22, invade, 342, 55%.
39, bombard, 121, 75%.
98, raid, 644, 28%, GOLD.              // raid 644 for gold

// --- Movement ---
77, move, A/6.                         // in-system move to orbit 6 of star A
79, jump, 4-6-19.                      // jump to system 4-6-19

// --- Control ---
28, control.                           // declare control through proxy S/C 28
28, un-control.                        // or relinquish it

// --- Naming ---
39, name, "Dragonfire".                // name a ship
5-12-38A/2, name, "Goldball".          // name a planet (location needs star letter and orbit)

// --- News and permissions ---
02-29-64A/3, news, "SDRV-3 on the market next turn.", "Tras-yo of Blenora".
129, permission to colonize, 99-12-26A/3.
138, permission, 200, granted.
162, permission, 100, denied.
```

This sample only illustrates each order's shape. For the exact format, fields,
and constraints of every order, follow the reference: each of these orders is
cataloged in
[Writing Orders]({{< relref "../reference/writing-orders.md" >}}) — for instance
[set up]({{< relref "../reference/writing-orders.md#set-up-orders" >}}),
[assemble and dis-assemble]({{< relref "../reference/writing-orders.md#assembly-orders" >}}),
[build change]({{< relref "../reference/writing-orders.md#build-change-orders" >}}),
[transfer]({{< relref "../reference/writing-orders.md#transfer-orders" >}}),
[market buy/sell]({{< relref "../reference/writing-orders.md#market-orders" >}}),
[combat]({{< relref "../reference/writing-orders.md#combat-orders" >}}),
[spy]({{< relref "../reference/writing-orders.md#spy-orders" >}}),
[movement]({{< relref "../reference/writing-orders.md#movement-orders" >}}),
[draft]({{< relref "../reference/writing-orders.md#draft-orders" >}}),
[pay]({{< relref "../reference/writing-orders.md#pay-orders" >}}),
[ration]({{< relref "../reference/writing-orders.md#ration-orders" >}}),
[control]({{< relref "../reference/writing-orders.md#control-orders" >}}), and
[naming]({{< relref "../reference/writing-orders.md#naming-orders" >}}).

To interpret the report this file produces, see
[Read a turn report]({{< relref "read-a-turn-report.md" >}}).

## Order several actions in sequence

The parser works through your orders in the order the turn executes, stage by
stage. When it reaches a stage, it acts on the matching orders and moves on; an
order for a stage that has already passed is skipped. So when one action must
happen before another, write the orders in that same order.

The manual's own example is dis-assembly and assembly. Dis-assembly runs before
assembly in the Sequence of Play, so write your dis-assembly order first:

```text
58, disassemble, MSL-1, 6,000.         // free the units first
58, assemble, FACT-6, 6,000, CNGD.     // then assemble with them
```

If you wrote the assembly order first, the parser would reach the assembly stage
before the units were freed, decide there was no assembly order to fill, and skip
it.

The same applies when one order feeds another — transfer units into a ship before
the order that uses them, and move a ship after the orders that load it. Arrange
the whole file to match
[Sequence of Turn Execution]({{< relref "../reference/sequence-of-turn-execution.md" >}}).
For each order's format, see
[Assembly orders]({{< relref "../reference/writing-orders.md#assembly-orders" >}}),
[Dis-assembly orders]({{< relref "../reference/writing-orders.md#dis-assembly-orders" >}}),
and the rest of the
[Writing Orders]({{< relref "../reference/writing-orders.md" >}}) reference.
