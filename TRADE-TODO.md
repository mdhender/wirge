# TRADE-TODO — Convert "Trade" to a reference page

Plan for converting `user-manual/trade.md` (the manual's Trade chapter) into a
published Diátaxis **reference** page at `content/reference/trade.md`.

This plan is split into four small, independently reviewable tasks. Tasks 1–2
write the page content; task 3 wires it into the site; task 4 builds and
verifies. Read the shared context below before starting any task — it applies to
all of them.

## How to use this plan

Each task has a **Status** line: `TODO`, `IN PROGRESS`, or `DONE`. To advance the
work, implement the first task whose status is not `DONE` (tasks are ordered and
build on each other), then set its **Status** to `DONE`. A typical session
prompt: "Implement the next task in TRADE-TODO.md. Update the task status to DONE
when complete."

| Task | Status |
| ---- | ------ |
| 1 — Create the page; Trade stations | DONE |
| 2 — Home planet markets | DONE |
| 3 — Wire the page into the site and apply weight | DONE |
| 4 — Build, verify, and consistency pass | DONE |

Keep this table in sync with the per-task **Status** lines below.

Use the Diátaxis skill (`.agents/skills/diataxis/SKILL.md`) when writing
documentation; reference pages must **describe and only describe** (austere,
factual, no instruction or "why"), per `references/reference.rst`.

---

## Goal

Produce one authoritative reference page describing trade: what a trade station
is and how it is established, used, and trades for gold; and how home-planet
markets differ. The page must match the house style of the existing reference
pages and must **not** duplicate rules that already live elsewhere — it links to
them instead.

## Source material

`user-manual/trade.md` is the source (Trade Stations, Home Planet Markets, and
one footnote pointing to Communications). Read it in full first. Do **not** edit
the source — `user-manual/` is sacred (see `CLAUDE.md`); fix unclear rules in our
docs, not the manual.

There is **no `notes/` file dedicated to trade**; a grep of `notes/` turns up
only incidental mentions of "trade"/"market" and adds nothing authoritative for
this page.

The source carries these authoritative data points to convert:

1. **A trade station is an orbiting colony** a nation establishes and controls,
   whose **only** function is trade. It has no factories but may have farm units;
   it may be armed; it can be conquered or lost to rebellion as any colony can.
2. **Use with permission** — any orbiting colony or ship at the same planet may
   use a station once the owner grants permission; permission stays in force
   until retracted.
3. **Trade is in gold.** A station matches a buyer's offer against the seller's
   price; if the offer meets the seller's price **plus a 1% commission**, the
   trade completes. The **commission is paid by the seller and kept by the
   station**, which may use it for any purpose. Buying and selling use a **market
   order**.
4. **Establishment and size** — a station is created with a **set up order** that
   states the words "trade station". Minimum size is **3,000 structural units,
   500 life support units, 100 professional units**; there is no maximum.
5. **News service** — trade stations carry a news service (detailed under
   Communication).
6. **Home-planet markets** — everything under Trade Stations applies, except: a
   market sits on each race's home-planet **surface**, is **independent of any
   nation's control**, and **maintains itself from its commissions**, making
   purchases on its own behalf.

## Overlap map (link, do not restate)

| Source statement | Already covered in |
| ---------------- | ------------------ |
| A trade station is an orbiting colony (`CORB`); per-planet limits, size, life support | `colonies-and-ships.md#comparison` |
| Establishment via a set up order (transfers materials, `STU`/`FARM`/population/`CNW`) | `colonies-and-ships.md#establishment`; `writing-orders.md` |
| Conquest / loss to rebellion of a colony | `rebellion.md` |
| Farm units (`FARM`) a station may hold | `farming.md`; `units.md#production` |
| `STU` / `LSP` minimum-size unit codes | `ship-systems.md#structural-units`; `ship-systems.md#life-support` |
| `PRO` minimum-size unit code | `units.md#population-units`; `population.md#population-classes` |
| `GOLD` as the trade currency | `units.md#resources`; `glossary.md` "Gold" |
| Market order, set up order, colonizing-permission order | `writing-orders.md` (stub — page-level link only; order-type anchors don't exist yet) |
| Buying technology (`PRTO`) at a market/trade station | `technological-advancement.md#buying-technology` |

Note: a trade station's "conquered or lost to rebellion" behavior is generic
colony behavior — state it in one factual sentence and link `rebellion.md`; do
not restate the rebellion rules.

## Terminology and code mapping (source → our docs)

Our docs use the engine codes and the term **nation** (not "player"). Map the
manual's wording as you convert:

| Source term | Use in our page |
| ----------- | --------------- |
| Trade station | trade station (an orbiting colony, `CORB`) |
| "the player" (establishes / controls / trades) | **nation** |
| Gold units | `GOLD` |
| Structural units (minimum size) | structural units (`STU`) |
| Life support units (minimum size) | life support units (`LSP`) |
| Professional units (minimum size) | `PRO` |
| Farm units | `FARM` |
| Market order | market order (link `writing-orders.md`) |
| Set up order | set up order (link `colonies-and-ships.md#establishment`) |
| Permission to trade / "contact the owner" | colonizing-permission order (link `writing-orders.md`); the owner-contact mechanism is under Communication (pending) |
| Commission | commission |
| News service | news service (under Communication — pending) |
| Home planet market | home-planet market |

## Conventions to follow (from the existing reference pages)

- **Front matter:** `title:` and `weight:` only. Title: `Trade`. Weight: `90`
  (see "Page weight and ordering").
- **Cross-links:** Hugo `relref` shortcodes, e.g.
  `[Establishment]({{< relref "colonies-and-ships.md#establishment" >}})`.
  Same-directory reference pages take a bare filename. **Note:**
  `writing-orders.md` lives in `content/reference/` (not `content/how-to/`), so
  it is a bare-filename `relref` from `trade.md`.
- **Markdoc shortcodes:** the source uses a Markdoc `{% fnref %}` / `{% footnotes %}`
  footnote (the "contact the owner → See Communications" note), which does **not**
  render in Hugo/Hextra. Fold it into prose or a callout. No Markdoc shortcodes
  may survive in the output.
- **Callouts:** `{{< callout type="info" >}}` for clarifications;
  `{{< callout type="warning" >}}` for the `TODO` about the unconverted
  Communication chapter (see "Link targets").
- **Codes** in backticks (`GOLD`, `STU`, `LSP`, `PRO`, `FARM`, `CORB`, …).
- **No duplication:** state the trade-specific rules authoritatively here; link
  out for everything in the overlap map. Do **not** re-explain the set up order,
  orbiting-colony attributes, or rebellion mechanics.
- **IP/naming:** never brand the game "Empyrean Challenge"; use "Epimethean
  Challenge" / "nation".

## Page weight and ordering (resolved)

The reference weights step by ten in Working-Index order: Manufacturing 70,
Technological Advancement 80, **Trade 90**, then Exploration (100), Rebellion
(110). Trade is **item 8** in the Working Index in `content/_index.md`, so its
weight is **90**.

No collision and no re-weighting of other pages is required: 90 is free between
`technological-advancement` (80) and `rebellion` (110). (`shortages` at 75 sorts
under Manufacturing and is unaffected.)

## Link targets — existing vs. pending

**Already exist** (link at the right anchor): `colonies-and-ships.md`
(`#comparison`, `#establishment`), `rebellion.md`, `farming.md`, `units.md`
(`#production`, `#population-units`, `#resources`), `ship-systems.md`
(`#structural-units`, `#life-support`), `population.md`,
`technological-advancement.md` (`#buying-technology`), `writing-orders.md`
(page-level only — its market/set up/colonizing-permission anchors don't exist
yet), `glossary.md`.

> **Correction to the brief:** `technological-advancement.md` is **already
> converted** and has a `#buying-technology` section. It is therefore **not** a
> missing target — it is a reciprocal link to wire (Task 3), and its existing
> `warning` TODO callout (which waits for this Trade page) should be resolved.

**Pending — do not invent a link:** there is **no Communication reference page**
yet (Communication is Working-Index item 14, not converted). The source points at
Communication twice — for the news service, and for the "contact the owner"
footnote. Handle both (see Tasks 1 and 3) with a single
`{{< callout type="warning" >}}` `TODO` and state the facts in prose; do **not**
fabricate a `communication.md` `relref` and do **not** create a stub here (the
Communication conversion owns that).

Out of scope as a link: a trade station can also **establish control of a
planet** (noted in the glossary), but the source `trade.md` does not state it and
Control of Planets is Working-Index item 13, not converted — leave it out.

---

## Task 1 — Create the page; Trade stations

**Status:** DONE

**Scope:** create `content/reference/trade.md` with front matter, a one-line
intro, and the full `## Trade stations` section.

**Steps:**

1. Front matter: `title: Trade`, `weight: 90`.
2. Intro (1–2 sentences, reference tone): trade takes place at trade stations a
   nation establishes and at home-planet markets; all trade is in `GOLD`.
3. `## Trade stations`:
   - A trade station is an [orbiting colony]({{< relref "colonies-and-ships.md#comparison" >}})
     (`CORB`) a nation establishes and controls, whose only function is trade. It
     has no factories but may hold [farm units]({{< relref "farming.md" >}})
     (`FARM`); it may be armed; it can be conquered or lost to
     [rebellion]({{< relref "rebellion.md" >}}) as any colony can (one factual
     sentence — link, do not restate).
   - **Use with permission:** any orbiting colony or ship at the same planet may
     use a station once its owner grants permission (a colonizing-permission
     order — link `writing-orders.md` at page level); permission stays in force
     until retracted. Fold the source's `{% fnref %}` footnote ("contact the
     owner → See Communications") into prose; the owner-contact mechanism is
     under Communication, which is covered by the warning `TODO` (step 6).
   - **Trading:** all buying and selling is in `GOLD`. A station matches a
     buyer's offer against the seller's price; if the offer meets the seller's
     price plus a **1% commission**, the trade completes. The commission is paid
     by the seller and kept by the station, which may use it for any purpose.
     Buying and selling use a **market order** (link `writing-orders.md` at page
     level).
   - **Establishment and size:** a station is created with a
     [set up order]({{< relref "colonies-and-ships.md#establishment" >}}) that
     states the words "trade station". Minimum size is **3,000 structural units
     (`STU`), 500 life support units (`LSP`), and 100 `PRO`**; there is no
     maximum. Link `STU`/`LSP` to `ship-systems.md#structural-units` /
     `#life-support` and `PRO` to `units.md#population-units`.
   - **News service:** trade stations carry a news service. Because Communication
     is not yet converted, state the fact and add the warning `TODO` (step 6)
     rather than linking.
4. Keep the entity attributes (per-planet limits, life support, size limitation)
   linked to `colonies-and-ships.md#comparison`, not restated.
5. Map every unit name to its engine code; use "nation" throughout.
6. Add a single `{{< callout type="warning" >}}` `TODO` covering the missing
   Communication page (it owns both the news service and the owner-contact
   detail). Example wording:

   ```
   {{< callout type="warning" >}}
   **TODO:** The Communication reference page (the news service, and how nations
   contact a station's owner for permission) is not yet converted. Link the detail
   here once it exists.
   {{< /callout >}}
   ```

   Do **not** invent a `communication.md` `relref`.

**Acceptance criteria:**

- `content/reference/trade.md` exists with valid front matter (`weight: 90`).
- The Trade stations section states: orbiting-colony nature, no factories /
  may have `FARM`, may be armed, conquest/rebellion (linked, not restated);
  use-with-permission; `GOLD` trading with the 1% seller-paid commission; set up
  order with "trade station"; the 3,000 `STU` / 500 `LSP` / 100 `PRO` minimum and
  "no maximum"; and the news service.
- The source footnote is folded into prose; no `{% … %}` Markdoc shortcodes
  survive; the Communication dependency is a `warning` callout (no fabricated
  link).
- Codes in backticks; "nation" per the mapping; no "Empyrean Challenge".

---

## Task 2 — Home planet markets

**Status:** DONE

**Scope:** add the `## Home planet markets` section.

**Steps:**

1. `## Home planet markets`: everything stated under Trade stations applies,
   except — state these factually:
   - A home-planet market sits on the **surface** of each race's home planet.
   - Markets are **independent of any nation's control**.
   - A market **maintains itself from its commissions**, making purchases on its
     own behalf.
2. Express the "everything under Trade stations applies, with these exceptions"
   relationship with a brief cross-reference to the section above (an in-page
   anchor or a short sentence), rather than repeating the trading mechanics.

**Acceptance criteria:**

- `## Home planet markets` present; states surface location, independence from
  nation control, and self-maintenance from commissions (purchasing on its own
  behalf).
- It defers to the Trade stations section for the shared rules instead of
  restating them.
- Reference tone; codes in backticks; no "Empyrean Challenge"; no Markdoc
  shortcodes.

---

## Task 3 — Wire the page into the site and apply weight

**Status:** DONE

**Scope:** make the page reachable and relink the lines/cells that now have a
real target. No new body content.

**Steps:**

1. **Working Index** in `content/_index.md`: turn the three bare-text lines into
   links, mirroring how Manufacturing/Rebellion are linked:
   - `8 - TRADE` → `8 - [TRADE]({{< relref "reference/trade.md" >}})`
   - `8.1 - Trade Stations` → anchor `#trade-stations`
   - `8.2 - Home Planet Markets` → anchor `#home-planet-markets`
   Leave Exploration (9) and below as bare text — they are not yet converted.
2. **Glossary** (`glossary.md`):
   - **Add** a `Commission` entry under **C** (the 1% fee a seller pays a trade
     station, which the station keeps), linking `trade.md#trade-stations`.
   - **Relink** the existing `Trade station` entry (under **T**) to
     `trade.md#trade-stations`.
   - **Relink** the existing `Market` entry (under **M**) to
     `trade.md#home-planet-markets`.
   - The `Gold` and `Control` entries already mention the market/trade station;
     relink the relevant phrase to `trade.md` only if it reads naturally —
     otherwise leave intact. Do not duplicate existing entries.
3. **Resolve the Tech Advancement reciprocal TODO:** in
   `technological-advancement.md#buying-technology`, the "market or trade station"
   phrase links `writing-orders.md` and is followed by a `warning` callout
   reading "The Trade reference page … is not yet converted." Relink the
   market/trade-station phrase to `trade.md` and **remove that `warning`
   callout** now that the target exists.
4. **Reciprocal links** where genuinely helpful (keep host wording; just add the
   `relref`): `colonies-and-ships.md#comparison` may note that an orbiting colony
   can be a trade station; `rebellion.md` may note a trade station can be lost to
   rebellion. Add only if it earns its place. The Trade page itself may note that
   technology (`PRTO`) can be bought at a station, linking
   `technological-advancement.md#buying-technology`.

**Acceptance criteria:**

- `content/_index.md` lines `8`, `8.1`, `8.2` resolve via `relref`; Exploration
  and below remain bare.
- Glossary has the new `Commission` entry and relinked `Trade station` / `Market`
  entries, all resolving; no duplicates introduced.
- The Tech Advancement `#buying-technology` market/trade-station phrase links
  `trade.md` and its now-stale `warning` TODO callout is removed.
- Any reciprocal links added resolve and preserve the host page's wording.

---

## Task 4 — Build, verify, and consistency pass

**Status:** DONE

**Scope:** confirm everything builds, links resolve, and nothing regressed.

**Steps:**

1. Run `hugo --gc` and confirm a clean build with **no** `relref` "not found"
   errors and no duplicate-weight warnings.
2. Grep the changed pages for leftover Markdoc shortcodes (`{%`),
   broken/relative Markdown links, and the string "Empyrean Challenge".
3. Confirm sidebar order: `trade` (90) sits after `technological-advancement`
   (80) and before `rebellion` (110).
4. Confirm every `relref` in the new page targets an existing file and that each
   anchor (`#comparison`, `#establishment`, `#structural-units`,
   `#life-support`, `#population-units`, `#buying-technology`, …) resolves.
   Confirm the only deliberately *unlinked* target is the pending Communication
   chapter, which is covered by the `warning` TODO callout (no
   `communication.md` `relref`).
5. Re-read against `CLAUDE.md` and the Diátaxis skill: reference mode (not mixed),
   no engine code added, no duplication of rules owned by other pages (the set up
   order, orbiting-colony attributes, rebellion).

**Acceptance criteria:**

- `hugo` builds with no errors or broken-`relref` warnings.
- No `{% %}` shortcodes, no "Empyrean Challenge", no broken links in any changed
  or new file.
- The page reads as authoritative reference and defers (via links) to the pages
  in the overlap map for shared rules; the Communication dependency is flagged,
  not faked.

---

## Out of scope

- Re-converting **Communication** (the news service / owner-contact mechanism;
  Working-Index item 14) — its link is left as a flagged `TODO`.
- Re-converting **Technological Advancement** (owned by
  `technological-advancement.md`) — link `#buying-technology` and resolve its
  reciprocal TODO.
- Re-explaining the **set up order**, orbiting-colony attributes (owned by
  `colonies-and-ships.md`), or **rebellion** mechanics (owned by `rebellion.md`).
- **Control of Planets** (Working-Index item 13) — a trade station can establish
  control, but the source `trade.md` does not state it and that chapter is not
  converted.
- Any engine code (lives in the separate `pyre` repo).
- Editing `user-manual/trade.md`.
