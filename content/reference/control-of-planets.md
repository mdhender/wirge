---
title: Control of Planets
weight: 140
---

Control is a nation's claim over a planet, held through an orbiting or surface
colony — or a [trade station]({{< relref "trade.md#trade-stations" >}}) — there.
Controlling planets underlies the
[victory condition]({{< relref "victory-conditions.md" >}}).

## Taking control

A nation establishes control of a planet by having an orbiting or surface
[colony]({{< relref "colonies-and-ships.md#comparison" >}}) — or a
[trade station]({{< relref "trade.md#trade-stations" >}}) — there (for how a
colony is [established]({{< relref "colonies-and-ships.md#establishment" >}})) and
declaring rulership with a **control order** (see
[Writing Orders]({{< relref "writing-orders.md" >}})).

When two nations send control orders for the same planet on the same turn, the
computer randomly selects one to establish the colony and become the planet's
ruler. The other nation's order is aborted.

## Controlled planets

A nation that wishes to colonize a planet another nation controls has two
options.

- **Bombard or capture** the ruler's colony. See
  [Bombardment]({{< relref "combat.md#bombardment" >}}) and
  [Captured colonies]({{< relref "combat.md#captured-colonies" >}}).
- **Request permission** from the ruler by diplomatic message, agreeing to
  whatever consideration the ruler requires in return. The considerations may be
  a large initial fee; a percentage of mined resources; a quarterly or annual fee
  payable in `GOLD`; or sole buying and selling by the new colony through the
  ruler's [trade station]({{< relref "trade.md#trade-stations" >}}), if the ruler
  has one. A nation requests permission with a colonizing-permission order (see
  [Writing Orders]({{< relref "writing-orders.md" >}})).

{{< callout type="warning" >}}
**TODO:** Link the Communication reference page (Diplomatic Messages) here with a
`relref` once that page exists.
{{< /callout >}}

## Relinquishing planets

A nation may relinquish control of a planet at any time with an **uncontrol
order** (see [Writing Orders]({{< relref "writing-orders.md" >}})).
