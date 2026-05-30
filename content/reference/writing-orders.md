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

## Combat orders

The percent committed is an integer and the `%` sign is required; `10%` is barely
committed and `100%` is totally committed. See
[Percentage of commitment]({{< relref "combat.md#percentage-of-commitment" >}}).

**Bombard.**

```text
Ship/Colony No. , bombard , Defender Ship/Colony No. , percent committed .
```

```text
39, bombard, 121, 75%.
```

**Invade.**

```text
Ship/Colony No. , invade , Defender Ship/Colony No. , percent committed .
```

```text
22, invade, 342, 55%.
```

**Raid.** The material raided follows the percent committed.

```text
Ship/Colony No. , raid , Defender Ship/Colony No. , percent committed , material raided .
```

```text
98, raid, 644, 28%, GOLD.
```

**Support (attacker).** The supported attacker's ID No. precedes the defender's;
the example below has No. 20 support No. 342 in its attack on No. 45.

```text
Ship/Colony No. , support , attacker Ship/Colony No. , Defender Ship/Colony No. , percent committed .
```

```text
20, support, 342, 45, 35%.
```

**Support (defender).** The example below has No. 20 support No. 342 in its
defense.

```text
Ship/Colony No. , support , Defender Ship/Colony No. , percent committed .
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
order may span several lines, and `end` terminates the block.

```text
set up , type (ship or colony) , Establishing Ship/Colony No. , transfer , quantity and item , ... , end .
```

```text
set up, ship, 29,
transfer, 50,000 STU,
5 SDRV-1,
5 LSP-1,
1 SEN-1,
end.
```

The `-1` in `SDRV-1` is the unit's TL.

See [Establishment]({{< relref "colonies-and-ships.md#establishment" >}}) for what
a set-up order does. For the full set-up block in context, see
[Write a turn's orders]({{< relref "../how-to/writing-orders.md" >}}).

## Assembly orders

An assembly order has three variants. Factories and mines are assembled into
groups automatically.

**Factory.** The units the factory group will make follow the quantity of factory
units.

```text
Ship/Colony No. , assemble , quantity of FACT , units the factory will make .
```

```text
91, assemble, 54,000 FACT-6, CNGD.
```

**Mine.** The deposit No. the mine group will work follows the quantity of mine
units.

```text
Ship/Colony No. , assemble , quantity of MINE , Deposit No. .
```

```text
83, assemble, 25,680 MINE-2, 148.
```

**Other.**

```text
Ship/Colony No. , assemble , quantity of units .
```

```text
58, assemble, 6,000 MSL-1.
```

See [Assembling]({{< relref "manufacturing.md#assembling" >}}).

## Dis-assembly orders

Format and examples match the assembly orders, with `disassemble` replacing
`assemble`.

```text
58, disassemble, 6,000 MSL-1.
```

See [Dis-assembling]({{< relref "manufacturing.md#dis-assembling" >}}).

## Build change orders

A build change order sets a factory group to start a new product, or `retool`.

```text
Ship/Colony No. , build change , Factory Group No. , item to start building (or retool) .
```

```text
16, build change, 8, EWP-4.
16, build change, 10, retool.
```

See [Retooling]({{< relref "manufacturing.md#retooling" >}}).

## Transfer orders

A transfer order moves one unit type from one ship or colony to another. One order
moves a single unit type; multi-item transfer is a future feature.

```text
Ship/Colony No. , transfer , quantity and unit type , Receiving Ship/Colony No. .
```

```text
22, transfer, 10 SPY, 29.
```

See [Colonies and Ships]({{< relref "colonies-and-ships.md" >}}).

## Mining change orders

A mining change order reassigns a mining group to a new deposit.

```text
Ship/Colony No. , mining , Mining Group No. , new Deposit No. .
```

```text
348, mining, 18, 92.
```

See [Mining]({{< relref "mining.md" >}}).

## Market orders

A market order buys or sells units or technology levels. The quantity is omitted
when buying or selling a technology level.

**Buy units.**

```text
Ship/Colony No. , buy , quantity , unit type , price in GOLD each .
```

```text
555, buy, 25,600, STU, 0.01.
```

**Buy TL.** The quantity is omitted.

```text
Ship/Colony No. , buy , technology level , price in GOLD each .
```

```text
53, buy, TL-6, 1,000,000.
```

**Sell units.**

```text
Ship/Colony No. , sell , quantity , unit type , price in GOLD each .
```

```text
721, sell, STU, 0.5.
```

**Sell TL.** The quantity is omitted.

```text
Ship/Colony No. , sell , technology level , price in GOLD each .
```

```text
721, sell, TL-4, 800,000.
```

See [Home planet markets]({{< relref "trade.md#home-planet-markets" >}}).

## Survey orders

```text
Ship/Colony No. , survey .
```

```text
23, survey.
```

See [Surveys]({{< relref "exploration.md#surveys" >}}).

## Probe orders

A probe order takes one or more orbit numbers, separated by commas.

```text
Ship/Colony No. , probe , Orbit No. , ... .
```

```text
28, probe, 6.
31, probe, 2, 4, 5.
```

See [Probes]({{< relref "exploration.md#probes" >}}).

## Spy orders

A spy order names a quantity of spies and a function. Three functions —
**incite rebels**, **attack spies**, and **information** — also take a defender
ship or colony ID No.

```text
Ship/Colony No. , quantity of SPY , check rebels .
Ship/Colony No. , quantity of SPY , convert rebels .
Ship/Colony No. , quantity of SPY , incite rebels , Defender Ship/Colony No. .
Ship/Colony No. , quantity of SPY , check for spies .
Ship/Colony No. , quantity of SPY , attack spies , Defender Ship/Colony No. .
Ship/Colony No. , quantity of SPY , information , Defender Ship/Colony No. .
```

```text
38, 1, check rebels.
38, 119, convert rebels.
38, 998, incite rebels, 54.
38, 1, check for spies.
38, 102, attack spies, 54.
38, 12, information, 54.
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
news , Market Planet Location , message text , signature .
```

```text
news, 02-29-64/3, "SDRV-3 on the market next turn.", "Tras-yo of Blenora".
```

**Trade station.**

```text
news , Trade Station Colony No. , message text , signature .
```

```text
news, 632, "SDRV-3 on the market next turn.".
```

See [News service]({{< relref "communication.md#news-service" >}}).

## Jump orders

**In-system.** From the 11th orbit, the destination orbit is prefixed with the
target star's sequence letter and a dash (`C-4`).

```text
Ship No. , move , Orbit No. .
```

```text
77, move, 6.
88, move, C-4.
```

See
[Interplanetary movement]({{< relref "exploration.md#interplanetary-movement" >}}).

**System jump.**

```text
Ship No. , move , Destination Location .
```

```text
79, move, 4-6-19.
```

See
[Interstellar movement]({{< relref "exploration.md#interstellar-movement" >}}).

## Draft orders

The unit-type words are rendered here as codes (`SLD` for soldier, `TRN` for
trainee) for consistency with the rest of these docs.

```text
Ship/Colony No. , draft , quantity and type of unit .
```

```text
13, draft, 3,600 SLD.
78, draft, 16,880 TRN.
99, draft, 5,000 CNW.
```

See [Population orders]({{< relref "population.md#orders" >}}).

## Disband orders

```text
Ship/Colony No. , disband , quantity and type of unit .
```

```text
13, disband, 3,600 SLD.
```

See [Population changes]({{< relref "population.md#population-changes" >}}).

## Pay orders

The pay-type words are rendered as codes (`USK` for unskilled, `PRO` for
professional, `SLD` for soldier).

```text
Ship/Colony No. , pay , wages , type .
```

```text
38, pay, 0.7, USK.
38, pay, 1.6, PRO.
38, pay, 1.2, SLD.
```

See [Population]({{< relref "population.md" >}}).

## Ration orders

```text
Ship/Colony No. , ration , ration percentage % .
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
