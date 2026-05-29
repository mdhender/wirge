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
