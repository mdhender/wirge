# Appendices

## Appendix I

### Approximation

These are estimates given in probe and sensor reports.
They will be given as the log base 10 of the actual number:

| Mass                  | Approximation |
|-----------------------|---------------|
| 0 - 9                 | 0             |
| 10 - 99               | 1             |
| 100 - 999             | 2             |
| 1,000 - 9,999         | 3             |
| 10,000 - 99,999       | 4             |
| 100,000 - 999,999     | 5             |
| 1,000,000 - 9,999,999 | 6             |
|                       | and so on.    |

### Fractions

All fractions of units will be truncated.
Or rounded up.
Depends on the context.

### Groups

Apply to factories and mines, which are organized into groups whenever they are put into operation.
Factory units in a group all manufacture the same unit.
Mine units in a group all mine the same deposit.

### Habitability Number

Limits the number of open farms which may operate on the surface of a planet.
It also limits the number of population units who can live there without increasing the chances of rebellion.
For instance, a planet with a habitability number of 1 can only have 100,000 farm units, and if more than 10,000,000 population units reside there, the chances of revolt will increase.
This applies to open colonies only.

### Hyper Space

Since tachyons don't actually exist in this universe, but in a parallel one, the tachyon universe is named Hyper Space.

### Mass

Mass is measured in mass units which will be set at 17,000 pounds, or approximately the weight of 100 men.

### Storage

Certain items must be assembled to be operational and dis-assembled to be transferred.
So, when units are not operational, they are said to be in storage.

## Appendix II

### Quantities Represented by Units

| UNIT              | NUMBER OF ITEMS PER UNIT                     |
|-------------------|----------------------------------------------|
| Anti-missile      | 1                                            |
| Assault Craft     | 1                                            |                                            
| Assault Weapons   | enough to arm 1 soldier unit                 |
| Automation        | enough to replace 1 worker unit times its TL |
| Consumer Goods    | indeterminate                                |
| Energy Shield     | 1                                            |
| Energy Weapon     | 1                                            |
| Factory           | 1                                            |
| Farm              | 1                                            |
| Hyper Engines     | 1                                            |
| Life Support      | 1                                            |
| Light Structural  | enough to house 1 mass unit                  |
| Military Robots   | 100 robots                                   |
| Military Supplies | enough for 1 soldier unit per combat round   |
| Mine              | 1                                            |
| Missile           | 1                                            |
| Missile Launcher  | 1                                            |
| Sensor            | 1                                            |
| Space Drive       | 1                                            |
| Structural        | enough to house 1 mass unit                  |
| Transport         | 1                                            |

Natural resource units are each 1 mass unit of that resource.

## Appendix III
Examples.

### Farm Group

Farm Group 1 contains 125,000 FAM-1 units producing 12,500,000 units of food per year.

Each FRM-1 unit requires 1 PRO and 1 USK labor per turn.
That is a total of 125,000 PRO and 375,000 USK labor per turn for the group.

The FRM-1 unit requires 0.5 FUEL per turn.
That is a total of 62,500 FUEL for the group per turn.

Farms produce 100 units of FOOD per year.
It's undocumented, but one-quarter of the results are available each turn.
That's what I've seen in the turn reports.

The farm group produces 3,125,000 units of FOOD per turn.

### Factory Group

Factory Group 1 contains 250,000 FCT-1 units producing CNGD units.

The group contains more than 50,000 units, so each unit requires 1 PRO and 3 USK labor per turn.
That is a total of 250,000 PRO and 750,000 USK labor.

Each FCT-1 unit requires 0.5 FUEL per turn.
That is a total of 125,000 FUEL.

Each FCT-1 unit can consume up to 20 mass units per year.
That is a total of 5,000,000 mass units per year.

CNGD units require 0.2 METS and 0.4 NMTS per unit, which is a total of 0.6 mass units per unit.
When we divide 20 mass units per year by 0.6 mass units per CNGD unit, we get 33.3333 CNGD units per year.
For CNGD, that works out to approximately 6.6667 METS and 13.3333 NMTS per year.
That totals to 20 mass units per year, which matches the consumption constraint on the factory unit.

The work in progress (WIP) calculations are weird.

In one year, the factory group will produce 250,000 * 33.3333, which is approximately 8,333,333 units per year.

In the first turn (let's call that Turn 1), the factory group will consume 125,000 FUEL, 1,666,666.6667 METS, and 3,333,333.3333 NMTS.
It will produce 8,333,333 units, but these units are not 100% complete.
They are in WIP and are only 25% complete.

In Turn 2, the factory group will consume 125,000 FUEL but no additional METS or NMTS.
It will not produce any new units, but will work on the existing 8,333,333 units.
They are in still WIP and are now 50% complete.

In Turn 3, the factory group will consume 125,000 FUEL but no additional METS or NMTS.
It will not produce any new units, but will work on the existing 8,333,333 units.
They are in still WIP and are new 75% complete.

In Turn 4, the factory group will consume 125,000 FUEL but no additional METS or NMTS.
It will complete the work on 8,333,333 units, but won't deliver any of them to the player until Turn 5.

2,083,334 units.


Factory Group 7 contains 50,000 FCT-1 units producing RSCH units.

12,500 units.

The example in section 6.3:

Factory Group 8 contains 50,000 FCT-1 units and is building MSS-2.

MSS requires 2 x TL METS and 2 x TL NMTS per unit, for a total of 4 METS and 4 NMTS per unit.
Production starts on turn 3; the first missiles will be completed on turn 7.

The player wants to produce 125,000 missiles per year.
Each MSS-2 requires 8 mass units of material per unit.
125,000 times 8 is 1,000,000 mass units.
The group needs 1,000,000 / 20, which is 50,000 FCT-1 units, to support this production rate.

The factory group will consume 25,000 FUEL per turn.

Turn 3, the factory group will consume 25,000 FUEL, 1,000,000 METS, and 1,000,000 NMTS.
This is enough material to produce 125,000 missiles.
It will produce 125,000 missiles, which are WIP and are 25% complete (WIP/25%).

Turn 4, the factory group will consume 25,000 FUEL and no additional METS or NMTS.
It will process 125,000 missiles, changing them from WIP/25% to WIP/50%.

Turn 5, there is a FUEL shortage and the factory group can consume only 12,500 FUEL.
This is enough fuel to process 62,500 missiles, changing them from WIP/50% to WIP/75%.
The remaining 62,500 missiles that were WIP/50% remaining at WIP/50%.
(Work is throttled, not abandoned when there is a FUEL shortage.)

Turn 6, the shortage is relieved and the factory group can consume 25,000 FUEL.
It will process 125,000 missiles.
The 62,500 missiles that were WIP/75% are now WIP/100% (complete and ready to be delivered to the player).
The 62,500 missiles that were WIP/50% are changed to WIP/75%.

Turn 7, the factory group will consume 12,500 FUEL and no additional METS or NMTS.
It will process 62,000 missiles.
The 62,500 which were WIP/100% are now delivered to the player.
The remaining 62,500 missiles that were WIP/75% and are now WIP/100% (complete and ready to be delivered to the player).

Turn 8, the factory group consumes no additional FUEL or METS or NMTS.
The 62,500 which were WIP/100% are now delivered to the player.

Turn 5 there is a shortage of FUEL.
Turn 6, the shortage is relieved.
Turn 7, 62,500 missiles are completed.
Turn 8, 62,500 missiles are completed.

Each missile will "cost" 4 metallic and 4 non-metallic units. This is done on turn 3, and the missiles will be completed on turn 7. A shortage, which allows his groups to function at half their capacity, occurs on turn 5 and is relieved on turn 6. Therefore, the player will receive 62,500 missiles on turn 7 and 62,500 on turn 8, instead of 125,000 on turn 7. (Since the shortage only took place for one quarter, the delay is for one quarter.) A shortage in a colony will affect all factory units, regardless of the unit they are manufacturing. Fuel is allocated to the mines and farms before the factories; fuel shortages usually affect only the factories.

```text
425,000 FUEL used by FCT-1 units in Turn 0.
```

## Appendix IV

Sample Documents.

### Orders File

```text
13, draft, 3600 soldier .
16, build change, 8, energy weapons-4 .
16, build change, 8, retool .
16, ration, 50% .
17, build change, research .
20, support, 342, 40% .
20, support, 342, 45, 35% .
22, invade, 342, 55% .
22, transfer, 10 spy units, 29 .
23, survey .
28, control, 2-4-6, 9 .
28, probe, 6 .
28, un-control, 2-4-6, 9 .
31, probe, 2, 4, 5 .
38, 1, check for spies .
38, 1, check rebels .
38, 102, attack spies, 54 .
38, 119, convert rebels .
38, 12, information, 54 .
38, 998, incite rebels, 54 .
38, pay, 0.7, unskilled .
38, pay, 1.6, professional .
38, pay, 1.2, soldier .
39, name, Dragonfire .
39, bombard, 121, 75% .
44, sell, 4, space drive-3, 0.2 .
5-12-38, 2, name, Goldball .
53, buy, TL-6, 1000000 .
58, assemble, 6000 missile launchers-1 .
77, move, 6 .
78, draft, 16880 trainee units 99, disband, 5000 .
79, move, 4-6-19 .
83, assemble, 25680 mine-2, 148 .
91, assemble, 54000 factories-6, consumer goods .
98, raid, 644, 28%, gold .
129, permission to colonize, 99-12-26, 3 .
138, 200, permission granted .
162, 100, permission denied .
348, mining, 18, 92 .
555, buy, 25600, structural, 0.01 .
721, sell, TL-4, 800000 .
News, 02-29-64-3, """I'll be putting space drives-3 on the market next turn."" Tras-yo of Blenora" .
Set Up, 5.1, ship, 29, transfer, 58, 60 structural units, 5 space drives-1, 5 Life Supports-1, 5 Food, 5 Professionals, 1 sensor-1, 16800 fuel, 61 hyper engines-1, END .
```

### Turn Report

```text
Game # EC-5               Turn # 1                                              Player #  13              Date 02/20/84

Open Colony      Not Named( 13 ) on                                          Orbit # 2 in System  0 / 0 / 0

Ship or Colony Activity Report

Vital Statistics ******************
1.0000 TL         0.4881 S.O.L.    0.0625% Deaths      0.0000% Births
0.1250 USK Pay    0.3750 PRO Pay   0.2500 SLD Pay    100.0000% Rations

Other Statistics ******************
400,000 TPT Capacity     15,920,040 Total POP          89,494,472 Total MASS
4,952,743 Space Avail.         65,000 FUEL used/FRM         150,000 FUEL used/MIN      500,000 FUEL mined
425,000 FUEL used/FCT     3,980,010 FOOD consumed       3,250,000 FOD produced     2,750,000 METS mined
1,395,833 METS used/FCT     1,354,167 NMTS used/FCT       1,942,513 CNGD paid        2,083,333 CNGD produced
2,990,000 employed USKs     1,430,000 employed PROs         400,000 unused TPT cap

Census Report *********************
5,900,000 UEM-0     6,000,000 USK-0     1,500,000 PRO-0     2,500,000 SLD-0      10,000 CNW-0

Storage/Non-Assembly Items ********
2,400,000 ASW-1       150,000 ANM-1       150,000 MSS-1        20,000 TPT-1
5,354,167 METS      2,645,833 NMTS      1,360,000 FUEL         20,000 GOLD    4,269,990 FOOD     940,821 CNGD

Storage/Unassembled Items *********
93,750 AUT-1        37,500 EWP-1        31,250 MIN-1           20 SEN-1   14,500,000 STUN

Assembled Items *******************
130,000 FRM-1        50,000 MSL-1            20 SEN-1   60,000,000 STUN


Mine # Units_____  TL  Dep. #  Deposit Qty.  Type  Yield   Mine # Units_____  TL  Dep. #  Deposit Qty.  Type  Yield
01    100,000   1      13    37,500,000  FUEL   20 %       02    200,000   1      28    35,000,000  METS   55 %


Grp. #  # FCT Units  TL  ORDERS  WORK IN PROCESS ONE QUARTER  WORK IN PROCESS ONE HALF  WORK IN PROCESS THREE QUARTERS
01      250,000   1  CNGD          2,083,334 CNGD               2,083,333 CNGD            2,083,333 CNGD
02       75,000   1  MTSP          9,375,000 MTSP               9,375,000 MTSP            9,375,000 MTSP
03       75,000   1  AUT-1            93,750 AUT-1                 93,750 AUT-1              93,750 AUT-1
04       75,000   1  EWP-1            37,500 EWP-1                 37,500 EWP-1              37,500 EWP-1
05       75,000   1  MIN-1            31,250 MIN-1                 31,250 MIN-1              31,250 MIN-1
06      250,000   1  STUN         12,500,000 STUN              12,500,000 STUN           12,500,000 STUN
07       50,000   1  RSCH             12,500 RSCH                  12,500 RSCH               12,500 RSCH


Domestic Espionage (Internal Spies)
10 Type A      0 Type B     10 Type C      0 Type D      0 Type E      0 Type F      0 Type G

Group A, Report on the rebel situation: rebels =       0   rebel soldiers =       0
Group C, Report on foreign espionage operations as you requested:

Owner #    Type A Spies    Type B Spies    Type C Spies    Type D Spies    Type E Spies    Type F Spies    Type G Spies
0               0               0               0               0               0               0               0


Survey Report for Planet # 2  in System  0 / 0 / 0
Habitability = 25              Farmland in use =    1,950,000              Population =    238,800,600
Deposits
No. Type Yield Qty______     No. Type Yield Qty______     No. Type Yield Qty______     No. Type Yield Qty______
01  ****     %               10  ****     %               20  ****     %               30  ****     %
02  ****     %               11  ****     %               21  ****     %               31  ****     %
03  ****     %               12  ****     %               22  ****     %               32  ****     %
04  ****     %               13  ****     %               23  ****     %               33  ****     %
05  ****     %               14  ****     %               24  ****     %               34  ****     %
06  ****     %               15  ****     %               25  ****     %               35  ****     %
07  ****     %               16  ****     %               26  ****     %
08  ****     %               17  ****     %               27  ****     %
09  ****     %               18  ****     %               28  ****     %
19  ****     %               29  ****     %
```
