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

Orders must be written in the same order as the Sequence of Play; orders written
out of sequence may not execute. See
[Sequence of Turn Execution]({{< relref "sequence-of-turn-execution.md" >}}) for
the canonical stage order. An assembly order written before a dis-assembly order,
for example, may not execute.

Every order is addressed to a ship or colony. The ship or colony ID No. is the
first field of most orders. See
[Colonies and Ships]({{< relref "colonies-and-ships.md" >}}) for entity IDs.

Some orders name a location — a system, star, or orbit. See
[Co-ordinates]({{< relref "glossary.md" >}}) for how a location is written, and
[Coordinates and Locations]({{< relref "../explanation/coordinates-and-locations.md" >}})
for the nuances of specifying them in orders.

An order is carried out only if the addressed ship or colony holds the units the
order needs; an order is filled partially when fewer units are present than it
calls for.

`//` begins a comment: the `//` and the rest of the line are ignored.

```text
// This is a comment
39, bombard, 121, 75%. // This is a comment
```

## Combat orders

The percent committed is an integer and the `%` sign is required; `10%` is barely
committed and `100%` is totally committed. See
[Percentage of commitment]({{< relref "combat.md#percentage-of-commitment" >}}).

**Bombard.**

```text
S/C ID. , bombard , Defender S/C ID. , Percent committed .
```

```text
39, bombard, 121, 75%.
```

**Invade.**

```text
S/C ID. , invade , Defender S/C ID. , Percent committed .
```

```text
22, invade, 342, 55%.
```

**Raid.** The material raided follows the percent committed.

```text
S/C ID. , raid , Defender S/C ID. , Percent committed , Unit raided .
```

```text
98, raid, 644, 28%, GOLD.
```

**Support (attacker).** The supported attacker's ID No. precedes the defender's;
the example below has No. 20 support No. 342 in its attack on No. 45.

```text
S/C ID. , support , Attacker S/C ID. , Defender S/C ID. , Percent committed .
```

```text
20, support, 342, 45, 35%.
```

**Support (defender).** The example below has No. 20 support No. 342 in its
defense.

```text
S/C ID. , support , Defender S/C ID. , Percent committed .
```

```text
20, support, 342, 40%.
```

See [Bombardment]({{< relref "combat.md#bombardment" >}}),
[Attack orders]({{< relref "combat.md#attack-orders" >}}), and
[Defense support]({{< relref "combat.md#defense-support" >}}) for combat
resolution.

## Set up orders

A set-up order establishes a new ship or colony and transfers units into it. The
order may span several lines, and `.` terminates the block.

Set up colony:

```text
S/C ID. , set up , colony , transfer , Unit , Quantity, ... .
```

```text
29, set up, colony, transfer,
STU-1, 50,000,
SDRV-1, 1,
LSP-1, 5,
SEN-1, 1.
```

Set up ship:

```text
S/C ID. , set up , ship , transfer , Unit, Quantity, ... .
```

```text
29, set up, ship, transfer,
STU-2, 50,000,
SDRV-1, 5,
HDRV-1, 10,
LSP-1, 5,
SEN-1, 1.
```

See [Establishment]({{< relref "colonies-and-ships.md#establishment" >}}) for what
a set-up order does. For the full set-up block in context, see
[Write a turn's orders]({{< relref "../how-to/writing-orders.md" >}}).

## Assembly orders

An assembly order has three variants. Factories and mines are assembled into
groups automatically.

**Factory.** The units the factory group will make follow the quantity of factory
units.

```text
S/C ID. , assemble , FACT Unit, Quantity , Unit the factory will make .
```

```text
91, assemble, FACT-6, 54,000, CNGD.
```

**Mine.** The deposit No. the mine group will work follows the quantity of mine
units.

```text
S/C ID. , assemble , Mine Unit , Quantity , Deposit No. .
```

```text
83, assemble, MINE-2, 25,680, 148.
```

**Other.**

```text
S/C ID. , assemble , Unit , Quantity .
```

```text
58, assemble, MSL-1, 6,000.
```

See [Assembling]({{< relref "manufacturing.md#assembling" >}}).

## Dis-assembly orders

```text
S/C ID. , disassemble , Unit , Quantity .
```

```text
58, disassemble, MSL-1, 6,000.
```

See [Dis-assembling]({{< relref "manufacturing.md#dis-assembling" >}}).

## Build change orders

A build change order sets a factory group to start a new product, or `retool`.

Start building:

```text
S/C ID. , build change , Factory Group No. , Unit to start building .
```

Retool:

```text
S/C ID. , retool , Factory Group No. , Unit to start building .
```

```text
16, build change, 8, EWP-4.
16, retool, 8, EWP-4.
```

See [Retooling]({{< relref "manufacturing.md#retooling" >}}).

{{< callout type="warning" >}}
TODO: Considering collapsing build change and retool into a single order.
{{< /callout >}}

## Transfer orders

A transfer order moves one unit type from one ship or colony to another. One order
moves a single unit type; multi-item transfer is a future feature.

```text
S/C ID. , transfer , Receiving S/C ID. , Unit , Quantity .
```

```text
22, transfer, 29, SPY, 10.
```

See [Colonies and Ships]({{< relref "colonies-and-ships.md" >}}).

## Mining change orders

A mining change order reassigns a mining group to a new deposit.

```text
S/C ID. , mining , Mining Group No. , New Deposit No. .
```

```text
348, mining, 18, 92.
```

See [Mining]({{< relref "mining.md" >}}).

## Market orders

A market order buys or sells units.

**Buy units.**

```text
S/C ID. , buy , Unit , Quantity , Price each (in GOLD) .
```

```text
555, buy, STU-2, 25,600, 0.01.
53, buy, PRTO-6, 1, 1,000,000.
```

**Sell units.**

```text
S/C ID. , sell , Unit , Quantity , Price each (in GOLD) .
```

```text
721, sell, STU-2, 4, 0.5.
721, sell, PRTO-4, 1, 800,000.
```

See [Home planet markets]({{< relref "trade.md#home-planet-markets" >}}).

## Survey orders

```text
S/C ID. , survey .
```

```text
23, survey.
```

See [Surveys]({{< relref "exploration.md#surveys" >}}).

## Probe orders

A probe order takes one or more orbit IDs, separated by commas.

```text
S/C ID. , probe , Orbit ID , ... .
```

```text
28, probe, A/6.
31, probe, A/2, C/4, B/5.
```

{{< callout type="info" >}}
The order may specify orbits for multiple stars only when the ship is located in the 11th orbit.
{{< /callout >}}


See [Probes]({{< relref "exploration.md#probes" >}}).

## Spy orders

A spy order names a quantity of spies and a function. Three functions —
**incite rebels**, **attack spies**, and **information** — also take a defender
ship or colony ID No.

```text
S/C ID. , check rebels , quantity of SPY .
S/C ID. , check for spies , quantity of SPY .
S/C ID. , convert rebels , quantity of SPY .
S/C ID. , attack spies , quantity of SPY , Defender S/C ID. .
S/C ID. , incite rebels , quantity of SPY , Defender S/C ID. .
S/C ID. , information , quantity of SPY , Defender S/C ID. .
```

```text
38, check rebels, 1.
38, check for spies, 1.
38, convert rebels, 119.
38, attack spies, 102, 54.
38, incite rebels, 998, 54.
38, information, 12, 54.
```

See [Spy functions]({{< relref "espionage.md#spy-functions" >}}),
[Convert rebels]({{< relref "espionage.md#convert-rebels" >}}), and
[Incite rebellion]({{< relref "espionage.md#incite-rebellion" >}}).

## News release orders

A news release posts a message to a market planet or a trade station. The message
text is enclosed in double quotes; an optional signature, if present, is also
quoted. Odd characters in the message may cause the order to be rejected.

**Market planet.**

```text
Market Planet Location , news , Quoted message text , Quoted signature .
```

```text
02-29-64A/3, news, "SDRV-3 on the market next turn.", "Tras-yo of Blenora".
```

{{< callout type="warning" >}}
The message text and signature must always be quoted.
Odd characters in the text may cause the order to be rejected (TODO: document which characters cause rejection).
{{< /callout >}}

**Trade station.**

```text
Trade Station Colony No. , news , Quoted message text , Quoted signature .
```

```text
632, news, "SDRV-3 on the market next turn.", "".
```

{{< callout type="warning" >}}
The message text and signature must always be quoted.
Odd characters in the text may cause the order to be rejected (TODO: document which characters cause rejection).
{{< /callout >}}

See [News service]({{< relref "communication.md#news-service" >}}).

## Movement orders

A movement order is `move` within a system and `jump` between systems.

### In-system

The destination is the target star's sequence letter and the orbit number,
separated by a slash (`A/2`, `C/4`, etc.). The star letter is required even in a
single-star system.

```text
Ship No. , move , Destination Orbit ID .
```

```text
77, move, A/2.
88, move, C/4.
```

See
[Interplanetary movement]({{< relref "exploration.md#interplanetary-movement" >}}).

### Between systems

The destination is the system ID alone; a between-systems jump cannot specify a
star or an orbit.

```text
Ship No. , jump , Destination System ID .
```

```text
79, jump, 4-6-19.
```

See
[Interstellar movement]({{< relref "exploration.md#interstellar-movement" >}}).

## Draft orders

```text
S/C ID. , draft , Population Unit , Quantity .
```

```text
13, draft, SLD, 3,600.
78, draft, TRN, 16,880.
99, draft, CNW, 5,000.
```

See [Population orders]({{< relref "population.md#orders" >}}).

## Disband orders

```text
S/C ID. , disband , Unit, Quantity .
```

```text
13, disband, SLD, 3,600.
```

See [Population changes]({{< relref "population.md#population-changes" >}}).

## Pay orders

```text
S/C ID. , pay , Population Unit, Wages (in CNGD) .
```

```text
38, pay, USK, 0.7.
38, pay, PRO, 1.6.
38, pay, SLD, 1.2.
```

See [Population]({{< relref "population.md" >}}).

## Ration orders

```text
S/C ID. , ration , Ration percentage % .
```

```text
16, ration, 50%.
```

{{< callout type="info" >}}
The ration is an integer and the `%` sign is required: `50%` is half a full ration
and `100%` is a full ration. Starvation sets in at `25%` of a full ration. All
population units on the ship or colony are assigned the same ration.
{{< /callout >}}

See [Rations]({{< relref "food.md#rations" >}}) and
[Starvation]({{< relref "food.md#starvation" >}}).

## Control orders

A control order takes control for the acting nation. It is addressed to a ship or
colony the nation has transferred population to.

```text
S/C ID. , control .
```

```text
28, control.
```

{{< callout type="info" >}}
The ship or colony ID is a proxy: the engine looks up the nation that controls it
and applies the order to that nation.
{{< /callout >}}

{{< callout type="warning" >}}
TODO: Reconsider whether a Location ID is needed.
{{< /callout >}}

See [Taking control]({{< relref "control-of-planets.md#taking-control" >}}).

## Un-control orders

An un-control order relinquishes control. It is the control order with
`un-control` replacing `control`.

```text
S/C ID. , un-control .
```

```text
28, un-control.
```

{{< callout type="info" >}}
The ship or colony ID is a proxy: the engine looks up the nation that controls it
and applies the order to that nation.
{{< /callout >}}

{{< callout type="warning" >}}
TODO: Reconsider whether a Location ID is needed.
{{< /callout >}}

See
[Relinquishing planets]({{< relref "control-of-planets.md#relinquishing-planets" >}}).

## Naming orders

A name may be at most 24 characters, including blanks, and is enclosed in double
quotes. Odd characters in the text may cause the order to be rejected (TODO: document which characters cause rejection).

### Naming planets

```text
Location ID , name , Quoted text .
```

```text
5-12-38A/2, name, "Goldball Prime".
```

### Naming ships and colonies

```text
S/C ID. , name , Quoted text .
```

```text
39, name, "Dragonfire".
```

## Trade station orders

A trade station order grants or denies a receiving ship or colony permission to
use the station.

```text
Trade Station S/C ID. , permission , Receiving S/C ID. , granted .
Trade Station S/C ID. , permission , Receiving S/C ID. , denied .
```

```text
138, permission, 200, granted.
162, permission, 100, denied.
```

{{< callout type="info" >}}
The receiving ship or colony is a proxy: granting or denying permission to it acts
on the nation that controls it.
{{< /callout >}}

See [Trade stations]({{< relref "trade.md#trade-stations" >}}).

## Colonization orders

A colonization order grants a receiving ship or colony permission to colonize a
location. The location must include the star letter and orbit number.

```text
Receiving S/C ID. , permission to colonize , Location .
```

```text
129, permission to colonize, 99-12-26A/3.
```

{{< callout type="warning" >}}
The receiving ship or colony is a proxy: granting permission to it acts on the
nation that controls it. Permission to colonize cannot be revoked once granted.
{{< /callout >}}

See [Control of planets]({{< relref "control-of-planets.md" >}}).
