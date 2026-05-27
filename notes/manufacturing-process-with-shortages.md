# Manufacturing

Total FACT units are the FACT units assigned to the FG.

Active FACT units are the subset of total FACT units that receive sufficient resources, managers, labor, and FUEL during the current turn.

## Allocating Managers, Labor, FUEL, and Resources

Factory units (FACT) use labor (PRO and USK or AUT) and FUEL to transform resources (METL and NMTL) into units.

Each turn, units are allocated in the following order:
1. Resources
2. PRO
3. AUT
4. USK
5. FUEL

Shortages complicate the allocation algorithm by reducing the number of active FACT units.

### Resource Allocation

Each FACT in a factory group (FG) can process a maximum of `20 × TL` MU of resources per year.
For example, a FACT-1 unit could process 20 MU of resources; a FACT-5 unit could process 100 MU.

A FG will never claim more resources than it can process in the current turn.

Examples:
* FG-1 contains 5 FACT-1. It requires 100 MU of resources (5 × 20 × 1) to operate at maximum capacity.
* FG-2 contains 5 FACT-1 and 10 FACT-3. It requires 700 MU of resources (5 × 20 × 1 + 10 × 20 × 3) to operate at maximum capacity.

Every active FG will attempt to claim enough resources each turn to operate at maximum capacity.

Resource claims are persistent.

Once resources have been assigned to an FG, those resources remain reserved for that FG in future turns unless the FG is shut down or it consumes them as part of the manufacturing process.

Resource allocation is prioritized by FG number; FG-1 will receive resources before FG-2.

If there is a shortage of resources, fewer FACT units will be active.
When this happens, higher TL FACT units have priority over lower TL FACT units within a FG.

Example:
* FG-1 contains 5 FACT-1 and 55 MUs are available. Only 2 FACT-1 units are active this turn, claiming 40 MUs. The remaining 15 MUs will be available for other factory groups to claim. 
* FG-2 contains 5 FACT-1 and 10 FACT-3 and 400 MUs are available. 2 FACT-3 units are active this turn, claiming all 400 MUs.

Note: Resources are consumed by the manufacturing process.

### Management and Labor Allocation

FGs use PRO to manage the group, and USK or AUT units as labor each turn.

#### Managers (PRO)

The number of PRO units depends on the number of FACT units in the FG.

| FACT units in FG | PRO per FACT unit |
|------------------|-------------------|
| 1 – 4            | 6                 |
| 5 – 49           | 5                 |
| 50 – 499         | 4                 |
| 500 – 4,999      | 3                 |
| 5,000 – 49,999   | 2                 |
| 50,000 +         | 1                 |

Examples:
* FG-1 contains 25 FACT-1 units. It requires 125 PRO units each turn (25 × 5)
* FG-2 contains 25 FACT-1 and 30 FACT-2 units. It requires 220 PRO units each turn (55 × 4)
* FG-12 contains 4,999 FACT-9 units. It requires 14,997 PRO units each turn (4,999 × 3)
* FG-13 contains 5,000 FACT-9 units. It requires 10,000 PRO units each turn (5,000 × 2)

PRO allocation is prioritized by FG number; FG-1 will receive PRO before FG-2.

If there is a shortage of resources allocated to the FG, the number of active FACT units will be lower, so fewer PRO units will be allocated. The number of PRO per FACT unit doesn't change.

Example:
* FG-12 has 4,999 total FACT-9 units but only 4 active FACT-9 due to a resource shortage. The FG will claim 12 PRO units (4 × 3).

If there is a shortage of PRO units, the number of active FACT units will be reduced.
When this happens, priority with the FG is by TL.

Example:
* An FG has 4,000 active FACT-1 units and 999 active FACT-9 units. Only 9,002 PRO are available. The group will be reduced to 2,001 active FACT-1 and 999 active FACT-9. The FG will claim 9,000 PRO units. The remaining 2 PRO units will be available for other factory groups to claim.

When the number of active FACT units changes, recalculate using the Reallocation Stability procedure.

#### Laborers (AUT and USK)

Each FG requires 3 labor units per PRO unit allocated.

The FG can use any combination of USK and AUT each turn.
(Note: AUT are allocated before USK.)

An AUT unit is equivalent to TL in labor units.

Examples:
* 10 AUT-1 = 10 labor units (10 × 1)
* 30 AUT-3 = 90 labor units (30 × 3)

Labor allocation is prioritized by FG number; FG-1 will receive labor units before FG-2.

If there is a shortage of labor units, the number of active FACT units will be reduced.
When this happens, priority with the FG is by TL.

When the number of active FACT units changes, recalculate using the Reallocation Stability procedure.

#### FUEL

The amount of fuel required by an FG depends on the number of active FACT units and their TL.
Each active FACT in an FG requires `0.5 × TL` FUEL units per turn.
For example, a FACT-1 unit requires 0.5 FUEL and a FACT-5 requires 2.5.

For the FG, sum the individual results and then round the result up.

Example:
* An FG with 15 FACT-1 and 10 FACT-2 units requires 18 FUEL units per turn (15 × 0.5 × 1 + 10 × 0.5 × 2, round 17.5 up to 18).

If there is a shortage of FUEL units, the number of active FACT units will be reduced.
When this happens, priority with the FG is by TL.

When the number of active FACT units changes, recalculate using the Reallocation Stability procedure.

### Reallocation Stability

When a shortage reduces the number of active FACT units, recalculate the FG’s PRO, labor, and FUEL requirements using the reduced active FACT count.

The active FACT count may only decrease during this process. It must never increase during the same turn’s reallocation pass.

Repeat this recalculation until one of the following is true:

1. The active FACT count is 0.
2. The active FACT count is unchanged after one complete pass through PRO, labor, and FUEL allocation.

If the active FACT count reaches 0, the FG performs no manufacturing this turn and does not advance WIP.

## Work In Progress

Work In Process (WIP) includes all items in the process of being Manufactured.

Example:
* FG-1 has 50,000 FACT-1 active. It is ordered on turn 3 to assemble 1,000 LSP-2. The turn report will show the WIP as follows:

|TURN|WIP 1/4 Comp.|WIP 1/2 Comp.|WIP 3/4 Comp.|Storage    |Notes                   |
|----|-------------|-------------|-------------|-----------|------------------------|
|  3 |      0      |      0      |      0      |    0      |Assembly order processed|
|  4 |  1,000 LSP-2|      0      |      0      |    0      |1st turn of production  |
|  5 |      0      |  1,000 LSP-2|      0      |    0      |2nd turn of production  |
|  6 |      0      |      0      |  1,000 LSP-2|    0      |3rd turn of production  |
|  7 |      0      |      0      |      0      |1,000 LSP-2|4th turn of production  |
|  8 |  1,000 LSP-2|      0      |      0      |    0      |1st turn of production  |
|  9 |      0      | 1,000 LSP-2 |      0      |    0      |2nd turn of production  |
| 10 |      0      |      0      |  1,000 LSP-2|    0      |3rd turn of production  |
| 11 |      0      |      0      |      0      |2,000 LSP-2|4th turn of production  |

Note that the Factory Group does not Finish 1/4 of the LSP-2 per turn (250 in other words), but instead will get the entire 1,000 one quarter of the way to being Finished.
On turn 7 of the example, 1,000 LSP-2 will appear in the Storage Inventory of the Colony and the WIP will again look like it did on turn 3 except for the fact that items showing in the Finished column will also be visible in Storage Inventory.

## Shortages

Shortages reduce the number of active FACT units in the group. This causes a ripple in the WIP.

When an FG is not running at capacity, the group prioritizes finishing work. Resources, managers, labor and FUEL will be allocated to the queues in this order:

1. WIP 3/4 Complete
2. WIP 1/2 Complete
3. WIP 1/4 Complete
4. Start new work

Example:
* FG-1 has 50,000 FACT-1 active. It is ordered on turn 3 to assemble 1,000 LSP-2. On turn 5, there is a FUEL shortage, and only 25,000 FACT-1 are active. The shortage is resolved on turn 6. The turn report will show the WIP as follows:

|TURN|WIP 1/4 Comp.|WIP 1/2 Comp.|WIP 3/4 Comp.|Storage    |
|----|-------------|-------------|-------------|-----------|
|  3 |      0      |      0      |      0      |    0      |
|  4 |  1,000 LSP-2|      0      |      0      |    0      |
|  5 |      0      |  1,000 LSP-2|      0      |    0      |
|  6 |      0      |    500 LSP-2|    500 LSP-2|    0      |
|  7 |      0      |      0      |    500 LSP-2|  500 LSP-2|
|  8 |      0      |      0      |      0      |1,000 LSP-2|
|  9 |  1,000 LSP-2|      0      |      0      |    0      |
| 10 |      0      | 1,000 LSP-2 |      0      |    0      |
| 11 |      0      |      0      |  1,000 LSP-2|    0      |
| 12 |      0      |      0      |      0      |2,000 LSP-2|
