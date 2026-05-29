---
title: Trade
weight: 90
---

Trade takes place at trade stations a nation establishes and at home-planet
markets. All trade is conducted in `GOLD`.

## Trade stations

A trade station is an [orbiting colony]({{< relref "colonies-and-ships.md#comparison" >}})
(`CORB`) a nation establishes and controls, whose only function is trade. It has
no factories but may hold [farm units]({{< relref "farming.md" >}}) (`FARM`). It
may be armed, and it can be conquered or lost to
[rebellion]({{< relref "rebellion.md" >}}) as any colony can.

Any orbiting colony or ship at the same planet may use a station once its owner
grants permission (through a colonizing-permission order; see
[Writing Orders]({{< relref "writing-orders.md" >}})). Permission stays in force
until the owner retracts it.

All buying and selling is conducted in `GOLD`. A station matches a buyer's offer
against the seller's price; if the offer meets the seller's price plus a **1%
commission**, the trade completes. The commission is paid by the seller and kept
by the station, which may use it for any purpose. Buying and selling use a market
order (see [Writing Orders]({{< relref "writing-orders.md" >}})). Technology can
also be bought at a station; see
[Buying technology]({{< relref "technological-advancement.md#buying-technology" >}}).

A nation establishes a trade station with a
[set up order]({{< relref "colonies-and-ships.md#establishment" >}}) that states
the words "trade station". The minimum size of a trade station is enough
[structure]({{< relref "ship-systems.md#structural-units" >}}) to enclose **300
[mass units]({{< relref "mass.md" >}})**, together with **500 life support
units** ([`LSP`]({{< relref "ship-systems.md#life-support" >}})) and **100
[`PRO`]({{< relref "units.md#population-units" >}})**. There is no maximum size.

{{< callout type="info" >}}
The rule book gives the structural minimum as 3,000 structural units. An
[orbiting colony]({{< relref "colonies-and-ships.md#comparison" >}}) takes 10
structural units to enclose each mass unit, so 3,000 of them enclose 300 mass
units.
{{< /callout >}}

Trade stations carry a news service.

{{< callout type="warning" >}}
**TODO:** The Communication reference page (the news service, and how a nation
contacts a station's owner for permission) is not yet converted. Link the detail
here once it exists.
{{< /callout >}}

## Home planet markets

Everything stated under [Trade stations](#trade-stations) applies to home-planet
markets, with the following exceptions. A home-planet market sits on the surface
of each race's home planet. Markets are independent of any nation's control and
maintain themselves from their commissions, making purchases on their own behalf.
