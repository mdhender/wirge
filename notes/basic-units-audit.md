# Basic Units Audit

Source: `user-manual/basic-units.md`

Status key:

- **Published**: covered by a published reference page.
- **Engine rule**: intentionally differs from the original rule book and is documented as an engine rule.
- **Future page**: belongs in a reference page that has not been converted yet.
- **Unresolved**: needs a design or rules decision.

## Description

- [x] **Published**: Basic units are units held by a ship or colony and determine whether that entity can comply with orders. Destination: `content/reference/units.md`.
- [x] **Published**: Basic-unit categories are population, weapons, production, and miscellaneous. Destination: `content/reference/units.md`.
- [x] **Published**: A ship/colony without sensors cannot probe. Destination: `content/reference/ship-systems.md#sensors` and `content/reference/planets.md#learning-about-a-planet`.
- [x] **Published**: "Ship/colony" means either ship or colony. Destination: `content/reference/glossary.md`.

## Population

- [x] **Published**: Population orders cover rationing, pay, drafting, and assembly. Destination: `content/reference/population.md#orders`.
- [x] **Published**: Ships have no population increases. Destination: `content/reference/population.md#ships`.
- [x] **Engine rule**: Ship crew consists of professionals. The source says all ship personnel except soldiers are professionals; the published page distinguishes professional crew from transported `USK`/`UEM`. Destination: `content/reference/population.md#ships`.
- [x] **Published**: Ship crew is paid 0.01 `GOLD` per population unit per turn; ship soldiers are paid 0.005 `GOLD`; transported colonists and similar passengers receive no wages but are fed. Destination: `content/reference/population.md#ships`.
- [x] **Published**: Ship wages exchange for `CNGD` at a home-planet market or trade station, and crew is paid when the ship is at an owner colony with enough `GOLD`. Destination: `content/reference/population.md#ships`.
- [x] **Published**: `UEM`, `USK`, `PRO`, and `SLD` definitions, 100 people per unit, standard `CNGD` pay, and 0.0625% non-combat death rate. Destination: `content/reference/population.md#population-classes`.
- [x] **Published**: Birth increases enter `UEM`, occur quarterly, range from 0.25% to 2.5%, and depend on unpopulated habitable land and standard of living. Destination: `content/reference/population.md#population-changes`.
- [x] **Published**: When `UEM` exceeds 30% of total population, 2% of `UEM` becomes `USK`; disbanded soldiers also become `USK`. Destination: `content/reference/population.md#population-changes`.
- [x] **Engine rule**: The hidden `RBL` tally does not affect `UEM` maturation in any way; neither the cutoff population nor the `UEM` amount is adjusted by `RBL`. Destination: `content/reference/population.md#population-changes`.
- [x] **Published**: `TRN` training, 1 `PRO` per 100 `TRN`, and 5% trainee graduation per turn. Destination: `content/reference/population.md#population-changes`.
- [x] **Engine rule**: Soldier retirement is modeled as 1.25% per turn, rounded up, rather than the source's 5% annually. Destination: `content/reference/population.md#population-changes`.
- [x] **Published**: Soldier drafting from `USK`, draft cap at current `SLD`, and unrestricted soldier disbanding. Destination: `content/reference/population.md#population-changes`.
- [x] **Published**: `SPY` and `CNW` cadre definitions, assembly/disassembly, population basis, pay, death rate, limits by available component classes, and separate turn-report chart visibility. Destination: `content/reference/population.md#population-cadres`.
- [x] **Published**: `RBL` is a tally rather than a class; pay and death rates do not apply; rebels increase with underpayment, underfeeding, and starvation; `RBL` is not shown in the separate cadre turn-report chart. Destination: `content/reference/population.md#population-cadres` and `content/reference/rebellion.md`.
- [x] **Engine rule**: The source says pay rates for all population classes may be adjusted. The engine applies player-set pay rates to population classes; cadre pay is derived from the classes allocated to each cadre. Destination: `content/reference/population.md#population-cadres` and `content/reference/population.md#orders`.

## Weapons

- [x] **Published**: `ASW` surface use, fuel 0, mass 20 MU. Destination: `content/reference/weapons.md#assault-weapons`.
- [x] **Published**: `ASC` invasion use, fuel 0.1 per turn, mass 5 x TL MU. Destination: `content/reference/weapons.md#assault-craft`.
- [x] **Published**: `MRBT` soldier replacement, no spy replacement, TL x 2 capacity, fuel 0, mass `(2 x TL) + 20` MU. Destination: `content/reference/weapons.md#military-robots`.
- [x] **Published**: `MSS` general combat use, lower accuracy than energy weapons, fuel 0, mass 4 x TL MU. Destination: `content/reference/weapons.md#missiles`.
- [x] **Published**: `MSL` launches `MSS` and `ANM`; missile accuracy depends on launcher TL; fuel 0; mass 25 x TL MU. Destination: `content/reference/weapons.md#missile-launchers`.
- [x] **Published**: `ANM` destroys attacking missiles; percentage destroyed depends on `ANM` TL; fuel 0; mass 4 x TL MU. Destination: `content/reference/weapons.md#anti-missiles`.
- [x] **Published**: `EWP` use in all combat except surface-to-surface colony combat; fuel 4 x TL per combat round; mass 10 x TL MU. Destination: `content/reference/weapons.md#energy-weapons`.
- [x] **Published**: `ESH` deflects energy beams; deflection depends on TL per combat round; fuel 10 x TL; mass 50 x TL MU. Destination: `content/reference/weapons.md#energy-shields`.
- [x] **Published**: `MTSP` combat supplies, fuel 0, mass 0.04 MU. Destination: `content/reference/weapons.md#military-supplies`.
- [x] **Published**: `TL`, `CR`, and `MU` terminology. Destination: `content/reference/glossary.md`.

## Production

- [x] **Published**: `MINE` TL range 1-10, annual output 100 x TL MU, per-turn output 25 x TL MU, fuel 0.5 x TL, deposits, deposit control, surface-only mining, and 3 `USK` + 1 `PRO` labor. Destination: `content/reference/mining.md`.
- [x] **Future page**: `MINE` total mass is 10 + (2 x TL) MU. This belongs on a manufacturing/cost reference page.
- [x] **Published**: `FARM` outputs, fuel use, types, placement rules, `FARM-1` HN x 100,000 cap, and 3 `USK` + 1 `PRO` labor. Destination: `content/reference/farming.md`.
- [x] **Published**: `FARM` total mass is 6 + TL MU. Destination: `content/reference/farming.md#food-output`.
- [x] **Future page**: `FACT` annual output 20 x TL MU, total mass 12 + (2 x TL) MU, fuel 0.5 x TL, and detailed factory actions belong on the Manufacturing reference conversion. Interim destinations: `content/reference/units.md#production`, `content/reference/shortages.md`, and `notes/manufacturing.md`.
- [x] **Published**: Orbiting-colony farms and factories within the fifth orbit require no fuel because they use solar power. Destination: `content/reference/farming.md#inputs` and `content/reference/shortages.md#what-a-group-needs`.

## Miscellaneous

- [x] **Published**: `AUT` replaces `USK` for factories, farms, and mines; formula is `AUT units x TL = USK units replaced`; mass 4 x TL MU; fuel 0. Destination: `content/reference/ship-systems.md#automation`.
- [x] **Published**: `CNGD` is produced by factories, used for population pay, and has mass 0.6 MU. Destination: `content/reference/ship-systems.md#consumer-goods`.
- [x] **Published**: Population consumes 0.25 FOOD per population unit per turn unless rationed; FOOD mass is 6 MU. Destination: `content/reference/food.md#rations`.
- [x] **Engine rule**: Starvation is expressed in ration percentages (`P = max(Rs - Ra, 0) / Rs`) instead of the source's food-unit formula `(M - R) / M = S`; it is equivalent for planned rationing. Destination: `content/reference/food.md#starvation`.
- [x] **Engine rule**: Unplanned shortages raise the survival ration to 35% for that turn. Destination: `content/reference/food.md#unplanned-shortages`.
- [x] **Published**: `LSP` role, required entities, TL^2 capacity, mass 8 x TL MU, and fuel TL per turn. Destination: `content/reference/ship-systems.md#life-support`.
- [x] **Published**: `HDRV` role, TL light-year range, mixed-TL lowest-range rule, propulsion capacity 1,000 x TL MU, mass 45 x TL MU, fuel 40 x distance per operating drive, legal destinations, distance rules, operating-drive count, and exclusion of drive mass from that count. Destination: `content/reference/ship-systems.md#hyperdrives`.
- [x] **Published**: `SDRV` role, ship requirement, mixed-TL permission, close-to-planet constraint, no interplanetary/interstellar travel, mass 25 x TL MU, combat-only fuel TL^2 per round, thrust factor TL^2 x 1,000, and combat movement formula. Destination: `content/reference/ship-systems.md#space-drives`.
- [x] **Published**: `SEN` mass, fuel, automatic system reports, automatic orbital reports, and TL probes per turn. Destination: `content/reference/ship-systems.md#sensors`.
- [x] **Future page**: Probe procedure belongs in the Exploration reference conversion. Interim destination: `content/reference/planets.md#learning-about-a-planet`.
- [x] **Published**: `TPT` transfer use, combat carriage, operators, mass, capacity, proportional non-combat fuel, definition of material, and life-support/structural transfer limits. Destination: `content/reference/ship-systems.md#transports`.
- [x] **Future page**: Combat transport capacity and fuel use belong in the Combat reference conversion. Current destination: `content/reference/ship-systems.md#transports`.
- [x] **Published**: Structural units are required to build ships and colonies; standard mass is 0.5 MU. Destination: `content/reference/ship-systems.md#structural-units`.
- [x] **Future page**: Structural-unit requirements by ship and colony type belong in the Colonies and Ships reference conversion. Current destination: `content/reference/ship-systems.md#structural-units`.
- [x] **Engine rule**: Standard and light structural units are represented as `STU-1` and `STU-2`. Destination: `content/reference/units.md#differences-from-the-rule-book` and `content/reference/ship-systems.md#structural-units`.
- [x] **Published**: Light structural units are built only by orbiting colonies, substitute for regular structural units without exception, and have mass 0.05 MU. Destination: `content/reference/ship-systems.md#structural-units`.

## Remaining Explicit TODOs

- Convert Manufacturing into published reference material for factory output, factory mass and fuel, factory production procedure, and construction costs.
- Convert Colonies and Ships into published reference material for structural-unit requirements and entity construction constraints.
- Convert Exploration into published reference material for probe procedure details.
- Convert Combat into published reference material for combat transport use and weapon resolution.
