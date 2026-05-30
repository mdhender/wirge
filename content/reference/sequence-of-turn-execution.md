---
title: Sequence of Turn Execution
weight: 170
---

A turn resolves in a fixed sequence of stages, listed below in the order they
execute. The same order repeats every turn. Each stage's output follows the
four-turn cadence described in
[The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}).

{{< callout type="info" >}}
Production (stages 1–2) is calculated before combat (stage 3) and before any
order processing, so a group formed by an order this turn produces nothing until
a later turn. See [The Production Cycle]({{< relref "../explanation/production-cycle.md" >}})
for the timing.
{{< /callout >}}

1. Mining and farming production is calculated.
   See [Mining]({{< relref "mining.md" >}}) and
   [Farming]({{< relref "farming.md" >}}).
2. Manufacturing production is calculated.
   See [Manufacturing]({{< relref "manufacturing.md" >}}).
3. Combat takes place.
   See [Combat]({{< relref "combat.md" >}}).
4. Set up orders are processed.
   See [Establishment]({{< relref "colonies-and-ships.md#establishment" >}}) and
   [Writing Orders]({{< relref "writing-orders.md" >}}).
5. Dis-assembly orders are processed.
   See [Dis-assembling]({{< relref "manufacturing.md#dis-assembling" >}}).
6. Build change orders are entered.
   See [Retooling]({{< relref "manufacturing.md#retooling" >}}).
7. Mining change orders are entered.
   See [Mining]({{< relref "mining.md" >}}).
8. Transfers are processed.
   See [Colonies and Ships]({{< relref "colonies-and-ships.md" >}}) and
   [Writing Orders]({{< relref "writing-orders.md" >}}).
9. Assembly orders are processed.
   See [Assembling]({{< relref "manufacturing.md#assembling" >}}).
10. All market and trade station activity takes place.
    See [Trade Stations]({{< relref "trade.md#trade-stations" >}}).
11. Surveys are carried out.
    See [Surveys]({{< relref "exploration.md#surveys" >}}).
12. Probe and sensor reports are compiled.
    See [Probes]({{< relref "exploration.md#probes" >}}).
13. Espionage activity takes place.
    See [Espionage]({{< relref "espionage.md" >}}).
14. Ship movement occurs.
    See [Ship movement]({{< relref "exploration.md#ship-movement" >}}).
15. Draft orders are processed.
    See [Population]({{< relref "population.md#population-changes" >}}) and
    [Writing Orders]({{< relref "writing-orders.md" >}}).
16. Pay and ration orders are entered.
    See [Rations]({{< relref "food.md#rations" >}}).
17. Rebellion occurs.
    See [When rebellion occurs]({{< relref "rebellion.md#when-rebellion-occurs" >}}).
18. Rebel increases take place.
    See [Rebel increase]({{< relref "rebellion.md#rebel-increase" >}}).
19. Naming and control orders are processed.
    See [Taking control]({{< relref "control-of-planets.md#taking-control" >}}) and
    [Writing Orders]({{< relref "writing-orders.md" >}}).
20. Population increases are calculated.
    See [Population]({{< relref "population.md#population-changes" >}}).
21. News service reports are compiled.
    See [News Service]({{< relref "communication.md#news-service" >}}).
