---
title: Writing Orders
weight: 180
---

This page catalogs the orders a nation submits with its turn. Each entry gives an
order's format, fields, and constraints, with one minimal example. For the larger
worked examples — the full set-up block, a complete order file, and multi-order
sequences — see the companion how-to,
[Write a turn's orders]({{< relref "../how-to/writing-orders.md" >}}).

## General rules

Each page of a turn carries a header line: the signature, player name, player ID
No., game No., and game-turn No. The game-turn No. is the number of the last
print-out received.

Zeros are written with a slash through them (0) to distinguish them from the
letter O.

A quantity and its unit need no comma between them.

Orders must be written in the same order as the Sequence of Play; orders written
out of sequence may not execute. See
[Sequence of Turn Execution]({{< relref "sequence-of-turn-execution.md" >}}) for
the canonical stage order. An assembly order written before a dis-assembly order,
for example, may not execute.

Every order is addressed to a ship or colony. The ship or colony ID No. is the
first field of most orders. See
[Colonies and Ships]({{< relref "colonies-and-ships.md" >}}) for entity IDs.

An order is carried out only if the addressed ship or colony holds the units the
order needs; an order is filled partially when fewer units are present than it
calls for.

`//` begins a comment: the `//` and the rest of the line are ignored.

```text
// This is a comment
39, bombard, 121, 75%. // This is a comment
```
