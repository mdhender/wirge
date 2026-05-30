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
close it with `end`:

```text
set up, ship, 29,
transfer, 50,000 STU,
5 SDRV-1,
5 LSP-1,
5 FOOD,
5 PRO,
1 SEN-1,
10,000 FUEL,
61 HDRV-1,
end.
```

Start the order with `set up`, the type (`ship` or `colony`), and the establishing
ship or colony's ID No. Follow it with `transfer` and then each item on its own
line. The order continues across line breaks until `end`, so `end` is required —
it tells the parser the list is complete. Without it, later orders would be read as
more transfer lines.

Each item is a quantity and a unit code; the `-1` in `SDRV-1` is the unit's TL.

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
83, assemble, 25,680 MINE-2, 148.       // work deposit 148
91, build change, 8, EWP-4.             // retool factory group 8

// --- Logistics ---
22, transfer, 10 SPY, 29.               // hand spies to the scout

// --- Movement ---
29, move, 4-6-19.                       // jump the scout out

16, ration, 50%.                        // half rations this turn
```

Write the header values — player name, player ID No., game No., game-turn No., and
your signature — on every page, and slash your zeros (0) so they are not read as
the letter O. The game-turn No. is the number of the last print-out you received.

Keep the orders grouped in the order the turn executes them; the next section
covers why that grouping matters. For the header rules and the `//` comment
convention, see
[General rules]({{< relref "../reference/writing-orders.md#general-rules" >}}).

{{< callout type="warning" >}}
**TODO:** When the manual's Appendix C (sample Orders File) is converted, link it
here as the canonical model.
{{< /callout >}}

## Order several actions in sequence

<!-- Task 18: multi-order sequences in Sequence-of-Play order -->
