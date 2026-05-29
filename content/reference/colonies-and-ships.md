---
title: Colonies and Ships
weight: 60
---

Colonies and ships are the four **entity** types a nation operates: three forms
of colony — open-air, enclosed, and orbiting — and the mobile ship. For each
entity's production capabilities and life-support requirements, see
[Entities]({{< relref "units.md#entities" >}}); for definitions, see the
[glossary]({{< relref "glossary.md" >}}).

## Comparison

| Attribute | Open-air (`COPN`) | Enclosed (`CENC`) | Orbiting (`CORB`) | Ship (`SHIP`) |
| --------- | ----------------- | ----------------- | ----------------- | ------------- |
| Allowed per nation per planet | 1 | 1 | 1 | Any number |
| Located on planet surface | Habitable terrestrial | Uninhabitable terrestrial | — | — |
| Located on asteroid | — | yes | — | — |
| Located in orbit | — | — | Any planet | Any planet |
| Life support (`LSP`) required | no | yes | yes | yes |
| Structural units (`STU`) per unit of mass | 1 | 5 | 10 | 10 |
| Size limitation | none | none | none | none |

{{< callout type="info" >}}
A nation may have one open-air colony, one enclosed colony, one orbiting colony,
and any number of ships at a single planet.
{{< /callout >}}

When counting the structural units an entity requires, units held in
[storage]({{< relref "mass.md#storage" >}}) count as only half their
[mass]({{< relref "mass.md" >}}), and the mass of the structural units housing
the entity is not counted at all.

## Establishment

A **set up order** establishes a new entity (see
[Writing Orders]({{< relref "writing-orders.md" >}})). It transfers materials —
any type and amount, including population — from an existing ship or colony at
the same location to the new site. A set up order is used only for establishment
and precludes [transfer]({{< relref "writing-orders.md" >}}) and
[assembly]({{< relref "writing-orders.md" >}}) orders on that entity.

A set up order must transfer:

- **Structural units (`STU`)** — the frame for the entity. See
  [Structural Units]({{< relref "ship-systems.md#structural-units" >}}).
- **Either farm units (`FARM`), or enough food (`FOOD`) to feed the population
  for at least one turn.** See [Farming]({{< relref "farming.md" >}}) and
  [Food]({{< relref "food.md" >}}).
- **At least one population unit.** An unpopulated entity is available for
  control by any other nation that installs a population unit there.
- **Enough construction workers (`CNW`) to assemble the entity.** See
  [Units]({{< relref "units.md" >}}).

If the transferred construction workers are insufficient to complete the
assembly, only the proportional portion is completed. When the construction
workers finish, they return to the ship or colony they were transferred from,
unless the set up order specifies otherwise.
