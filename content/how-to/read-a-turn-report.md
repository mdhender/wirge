---
title: Read a turn report
weight: 20
---

This guide walks through the turn report your nation receives each turn and shows
what each section reports and where the rule behind it lives. It does not teach
strategy and does not restate the rules — for the rule behind any field, follow
the link to its reference page.

The report below is a sample for one open-air colony, translated to engine codes.

```text
Game # 5               Turn # 1                          Nation # 13              Date 02/20/84

Open Colony      Not Named ( 13 ) on                     Orbit # 2 in System  0 / 0 / 0

Ship or Colony Activity Report

Vital Statistics ******************
1.0000 TL         0.4881 S.O.L.    0.0625% Deaths      0.0000% Births
0.1250 USK Pay    0.3750 PRO Pay   0.2500 SLD Pay    100.0000% Rations

Other Statistics ******************
400,000 TPT Capacity     15,920,040 Total POP          89,494,472 Total MASS
4,952,743 Space Avail.        65,000 FUEL used/FARM       150,000 FUEL used/MINE      500,000 FUEL mined
425,000 FUEL used/FACT     3,980,010 FOOD consumed      3,250,000 FOOD produced     2,750,000 METS mined
1,395,833 METS used/FACT    1,354,167 NMTS used/FACT     1,942,513 CNGD paid       2,083,333 CNGD produced
2,990,000 employed USKs     1,430,000 employed PROs       400,000 unused TPT cap

Census Report *********************
5,900,000 UEM     6,000,000 USK     1,500,000 PRO     2,500,000 SLD      10,000 CNW

Storage / Non-Assembly Items ********
2,400,000 ASW-1       150,000 ANM-1       150,000 MSS-1        20,000 TPT-1
5,354,167 METS      2,645,833 NMTS      1,360,000 FUEL         20,000 GOLD    4,269,990 FOOD     940,821 CNGD

Storage / Unassembled Items *********
93,750 AUT-1        37,500 EWP-1        31,250 MINE-1           20 SEN-1   14,500,000 STU-1

Assembled Items *******************
130,000 FARM-1        50,000 MSL-1            20 SEN-1   60,000,000 STU-1


Mine #  Units____  TL  Dep. #  Deposit Qty.  Type  Yield     Mine #  Units____  TL  Dep. #  Deposit Qty.  Type  Yield
01      100,000     1      13    37,500,000  FUEL  20 %       02      200,000     1      28    35,000,000  METS  55 %


Grp. #  # FACT Units  TL  ORDERS  WORK IN PROCESS ONE QUARTER  ONE HALF  THREE QUARTERS
01      250,000   1  CNGD     2,083,334 CNGD     2,083,333 CNGD     2,083,333 CNGD
02       75,000   1  MTSP     9,375,000 MTSP     9,375,000 MTSP     9,375,000 MTSP
03       75,000   1  AUT-1       93,750 AUT-1       93,750 AUT-1       93,750 AUT-1
04       75,000   1  EWP-1       37,500 EWP-1       37,500 EWP-1       37,500 EWP-1
05       75,000   1  MINE-1      31,250 MINE-1      31,250 MINE-1      31,250 MINE-1
06      250,000   1  STU-1   12,500,000 STU-1   12,500,000 STU-1   12,500,000 STU-1
07       50,000   1  RSCH        12,500 RSCH        12,500 RSCH        12,500 RSCH


Domestic Espionage (Internal Spies)
10 Type A      0 Type B     10 Type C      0 Type D      0 Type E      0 Type F      0 Type G

Group A, Report on the rebel situation: rebels =       0   rebel soldiers =       0
Group C, Report on foreign espionage operations as you requested:

Owner #    Type A    Type B    Type C    Type D    Type E    Type F    Type G
0               0         0         0         0         0         0         0


Survey Report for Planet # 2  in System  0 / 0 / 0
Habitability = 25       Farmland in use = 1,950,000       Population = 238,800,600
Deposits
No. Type Yield Qty______     No. Type Yield Qty______     No. Type Yield Qty______
01  ****     %               10  ****     %               20  ****     %
02  ****     %               11  ****     %               21  ****     %
...                          ...                          ...
```

## Header

The header names the game, the turn (one quarter of a galactic standard year),
your nation, and the date. The next line identifies the reporting entity — its
type ([open-air colony]({{< relref "../reference/units.md#entities" >}}) here),
its name, its ID number in parentheses, and its
[location]({{< relref "../reference/exploration.md#ship-movement" >}}) by orbit
and [system]({{< relref "../reference/game-setup.md#solar-systems" >}}).

## Vital and Other Statistics

These two blocks summarize the colony's economy for the turn. They restate values
computed elsewhere:

- `TL`, `S.O.L.`, deaths, births, pay (`USK Pay`, `PRO Pay`, `SLD Pay`), and
  `Rations` come from [Population]({{< relref "../reference/population.md" >}}) and
  [Food]({{< relref "../reference/food.md" >}}). Pay is in `CNGD`; rations are a
  percentage of a [full ration]({{< relref "../reference/food.md#rations" >}}).
- `TPT Capacity`, `Total MASS`, and `Space Avail.` come from
  [Transports]({{< relref "../reference/ship-systems.md#transports" >}}) and
  [Mass]({{< relref "../reference/mass.md" >}}).
- `FUEL used/FARM`, `FUEL used/MINE`, `FUEL used/FACT`, and `FUEL mined` are the
  fuel the production units drew this turn; see
  [Farming]({{< relref "../reference/farming.md" >}}),
  [Mining]({{< relref "../reference/mining.md" >}}), and
  [Manufacturing]({{< relref "../reference/manufacturing.md" >}}).
- `FOOD consumed`/`FOOD produced`, `METS mined`, `METS used/FACT`,
  `NMTS used/FACT`, and `CNGD paid`/`CNGD produced` tie the production cycle
  together; see [Mining]({{< relref "../reference/mining.md" >}}),
  [Manufacturing]({{< relref "../reference/manufacturing.md" >}}), and
  [Consumer Goods]({{< relref "../reference/ship-systems.md#consumer-goods" >}}).

## Census Report

The census lists population by class — `UEM`, `USK`, `PRO`, `SLD` — and the `CNW`
[cadre]({{< relref "../reference/units.md#population-units" >}}). For what each
class is and how it changes, see
[Population]({{< relref "../reference/population.md#population-classes" >}}).

{{< callout type="warning" >}}
**TODO:** The exact field layout of the census grid has no dedicated reference
page yet. Link it here once one exists.
{{< /callout >}}

## Storage and Assembled Items

The report splits the colony's holdings three ways:

- **Storage / Non-Assembly Items** and **Storage / Unassembled Items** are units
  and resources held in [storage]({{< relref "../reference/mass.md#storage" >}}).
  An [operational unit]({{< relref "../reference/glossary.md" >}}) in storage
  (for example `AUT-1`, `EWP-1`, `MINE-1`, `STU-1`) is not yet functional.
- **Assembled Items** are the operational units that have been
  [assembled]({{< relref "../reference/manufacturing.md#assembling" >}}) and are
  working — here `FARM-1`, `MSL-1`, `SEN-1`, and `STU-1`.

## Mines

Each mine group lists its number, unit count, `TL`, the deposit it works, that
deposit's quantity and type, and its [yield]({{< relref "../reference/mining.md#yield" >}}).
See [Mining]({{< relref "../reference/mining.md" >}}).

## Factory groups

Each factory group lists its number, `FACT` unit count, `TL`, the unit it is
building (`ORDERS`), and three [work-in-process]({{< relref "../reference/shortages.md#work-in-process-and-timing" >}})
buckets — one quarter, one half, and three quarters complete. A group delivers a
quarter of its annual output each turn once its pipeline fills; see
[Factory groups]({{< relref "../reference/manufacturing.md#factory-groups" >}}) and
[Work in process and timing]({{< relref "../reference/shortages.md#work-in-process-and-timing" >}}).

## Domestic Espionage

This section reports your own spy units by function, the rebel situation, and any
foreign-espionage findings your spies returned. For what each spy function does,
see [Spy functions]({{< relref "../reference/espionage.md#spy-functions" >}}).

{{< callout type="warning" >}}
**TODO:** The internal-espionage report grid (the per-type spy counts and the
foreign-spy table) has no dedicated reference page yet. Spy functions are
documented in [Espionage]({{< relref "../reference/espionage.md" >}}); link the
report layout here once a reference page exists.
{{< /callout >}}

## Survey Report

A survey report gives the planet's
[habitability number]({{< relref "../reference/habitability.md" >}}), farmland in
use, population, and the **exact** quantity, type, and
[yield]({{< relref "../reference/mining.md#yield" >}}) of each deposit. This is the
exact counterpart to the approximate quantities a probe returns; see
[Surveys]({{< relref "../reference/exploration.md#surveys" >}}) and
[Approximation]({{< relref "../reference/exploration.md#approximation" >}}).

{{< callout type="warning" >}}
**TODO:** The exact field layout of the survey-report deposit grid has no
dedicated reference page yet. Link it here once one exists.
{{< /callout >}}

To draft the orders that produce this report, see
[Write a turn's orders]({{< relref "writing-orders.md" >}}).
