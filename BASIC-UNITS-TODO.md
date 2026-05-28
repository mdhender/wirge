# Basic Units Conversion TODO

Source: `user-manual/basic-units.md`

Goal: finish converting the remaining Basic Units material into Diataxis-style
reference pages under `content/reference/`. Keep `user-manual/` unchanged except
for true typo fixes.

## Session 1: Population

Convert the population material from `basic-units.md` into a new reference page,
most likely `content/reference/population.md`.

Cover:

- Population unit definitions from Population Chart A.
- People per unit, consumer-goods pay, and non-combat death rates from Population
  Chart B.
- Birth increases, unemployable maturation, trainee graduation, soldier
  retirement, drafting, disbanding, spy assembly, construction-worker assembly,
  and rebels.
- Orders applicable to population units: ration, pay, draft, and assembly.
- Population units on ships, including wages and when ship crews are paid.
- Links to existing `food.md` for ration and starvation details.

Completion checks:

- `content/reference/units.md` links to the new population page.
- `content/reference/glossary.md` includes any missing population terms.
- No how-to instructions are mixed into the reference page.

## Session 2: Weapons

Convert the weapons chart into a dedicated reference page, most likely
`content/reference/weapons.md`.

Cover:

- Assault weapons.
- Assault craft.
- Military robots.
- Missiles.
- Missile launchers.
- Anti-missiles.
- Energy weapons.
- Energy shields.
- Military supplies.
- For each weapon: code, description, TL behavior, fuel use, mass formula, and
  combat applicability where the source states it.

Completion checks:

- `content/reference/units.md` links to the new weapons page.
- `content/reference/glossary.md` includes any missing weapon terms.
- Combat procedure is not duplicated here; link future/current combat reference
  material when available.

## Session 3: Miscellaneous and Ship Systems

Convert the remaining miscellaneous unit material into one or more reference
pages. A single `content/reference/ship-systems.md` may be enough, with
automation included there or split out if it becomes too large.

Cover:

- Automation: worker replacement formula, mass, fuel use, and applicable
  production uses.
- Consumer goods: mass and role as population pay, with links to population and
  manufacturing material.
- Life support: capacity, mass, fuel use, and where required.
- Hyper engines: jump range, propulsion capacity, mass, fuel use, lowest-TL rule,
  engine-count rule, distance rules, and legal jump destinations.
- Space drives: ship requirement, combat-only fuel use, thrust factor, mass, and
  movement formula.
- Sensors: mass, fuel use, automatic system/orbit reports, ship/colony reports,
  and probe rate.
- Transports: transfer use, combat use, professional-operator requirement,
  capacity, mass, fuel use, proportional fuel rule, and life-support/structural
  limits.
- Structural units and light structural units: build role, mass, substitution,
  and orbiting-colony manufacturing restriction.

Completion checks:

- `content/reference/units.md` links to the new detailed page or pages.
- Existing `game-setup.md`, `planets.md`, `mining.md`, `farming.md`, and
  `food.md` links remain valid.
- Any engine terminology differences are documented in the existing
  "Differences from the rule book" style.

## Session 4: Cross-Link and Audit

Audit every fact in `user-manual/basic-units.md` against the published reference
pages and clean up navigation.

Tasks:

- Build a checklist from every table row, formula, footnote, and constraint in
  `basic-units.md`.
- Mark each item as published, superseded by an engine rule, moved to a future
  page, or intentionally unresolved.
- Update `content/reference/units.md` so it acts as the unit catalog and points to
  detailed pages rather than duplicating everything.
- Update `content/reference/glossary.md` for newly introduced terms.
- Add or fix `relref` links between the new pages and existing pages.
- Check front matter weights. Basic Units is fifth in `user-manual/toc.json`, so
  closely related reference pages should stay near weight `50` unless their
  position is intentionally refined.
- Run `hugo` to verify the site builds.

Completion checks:

- Every Basic Units source fact has a documented destination or explicit TODO.
- The reference section remains information-oriented: factual descriptions,
  tables, formulas, constraints, and concise examples only.
- Hugo builds without broken links or shortcode errors.
