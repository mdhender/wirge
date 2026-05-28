---
title: Glossary
weight: 185
---

Key terms used throughout the Epimethean Challenge documentation. Where a term
names a unit, the code in parentheses is the game engine's authoritative code;
see [Units]({{< relref "units.md" >}}) for the full catalog.

## A

- **Anti-missile** (`ANM`) — A weapon launched by a missile launcher to destroy incoming missiles.
- **Assembly** — An order family that forms or disassembles units, including `SPY` and `CNW` population-cadre allocations. See [Population]({{< relref "population.md#orders" >}}).
- **Assault craft** (`ASC`) — A land/space vehicle used to invade a ship or colony.
- **Assault weapon** (`ASW`) — A weapon carried by soldiers in surface combat.
- **Asteroid** — A [planet]({{< relref "planets.md#types" >}}) type too small to be spherical; represents an entire asteroid belt and is treated as a single planet. Its habitability number is always 0.
- **Automation** (`AUT`) — A unit that replaces unskilled workers as labor in farms, mines, and factories.

## B

- **Binary system** — A [solar system]({{< relref "game-setup.md#solar-systems" >}}) containing two stars that share one set of co-ordinates.
- **Birth increase** — Population growth (colonies only) that enters the `UEM` class. See [Population]({{< relref "population.md#population-changes" >}}).

## C

- **Cadre** — A population allocation tracked separately from census totals. Includes `TRN`, `SPY`, `CNW`, and `RBL`.
- **Cluster** — The complete game map: 100 solar systems whose locations differ from one game to the next.
- **Colony** — A permanent installation a player establishes at a planet, in one of three forms: open-air, enclosed, or orbiting.
- **Combat round** (`CR`) — One increment of a combat exchange; some weapons' fuel use is measured per combat round.
- **Construction worker** (`CNW`) — A population-cadre allocation of 1 professional and 1 unskilled worker that carries out assembly and dis-assembly orders.
- **Consumer goods** (`CNGD`) — Factory output used to pay the population.
- **Control** — A player's claim over a planet, established by an orbiting or surface colony — or a trade station — and a declaration of control.
- **Co-ordinates** — The three two-digit numbers (`00`–`30`, e.g. `28-02-18`) that designate a [solar system]({{< relref "game-setup.md#cluster" >}}). Stars sharing co-ordinates lie in the same system. A star appends a letter suffix to the co-ordinates (`28-02-18A`), and an orbit appends `/` and its number (`28-02-18A/5`).

## D

- **Deposit** — A body of a single natural resource on a planet's surface. A planet holds up to 40 deposits, each of 1,000,000–99,000,000 units, with a fixed [yield]({{< relref "mining.md#yield" >}}).
- **Disband** — A population order that returns soldier units to unskilled-worker status. See [Population]({{< relref "population.md#population-changes" >}}).
- **Draft** — A population order that recruits soldiers or trainees. See [Population]({{< relref "population.md#orders" >}}).

## E

- **Eleventh orbit** (11th orbit) — A bookkeeping slot on each star, addressed as `<star>/11` (for example `00-00-00A/11`), used to hold a ship that has arrived by an interstellar jump. It is not a planetary orbit — those run 1–10 — and never holds a planet; a ship there must move to an orbit from 1 to 10 before it can act at any planet. See [Game Setup]({{< relref "game-setup.md#11th-orbit" >}}).
- **Empire** — *(Future rules.)* A collection of nations; the basis of a future [Empire Victory]({{< relref "victory-conditions.md" >}}). Not defined in this version of the game.
- **Enclosed colony** (`CENC`) — A sealed surface colony, allowed on any planet; requires life support.
- **Energy shield** (`ESH`) — A unit that absorbs energy-weapon damage.
- **Energy weapon** (`EWP`) — A line-of-sight combat weapon.
- **Entity** — A ship or colony. Often written "S/C" (ship/colony) in reports and documentation.

## F

- **Factory** (`FACT`) — A [production unit]({{< relref "units.md#production" >}}) that manufactures other units from materials.
- **Factory group** — A set of `FACT` units that manufacture units together, tracked in four quarter buckets toward completion.
- **Farm** (`FARM`) — A production unit that grows FOOD, delivering its harvest once a year. See [Farming]({{< relref "farming.md" >}}).
- **Farm group** — A set of `FARM` units that grow FOOD together, tracked in four quarter buckets toward harvest.
- **Food** (`FOOD`) — The resource that feeds the population, produced by farms. See [Food]({{< relref "food.md" >}}).
- **Fuel** (`FUEL`) — The resource that powers mines, farms, factories, engines, and combat.

## G

- **Galactic standard year** — The in-game year; one [turn]({{< relref "game-setup.md#turn-length" >}}) equals one quarter of it.
- **Gas giant** — A [planet]({{< relref "planets.md#types" >}}) type whose surface colonies and natural resources sit on its moons, which are treated as part of the one planet. Habitability number 0–12.
- **Gold** (`GOLD`) — The currency resource, used in the market and for wages.
- **Group** — A set of like production units (mine, farm, or factory) worked together under one group number. A group number is never reused.

## H

- **Habitability number** (`HN`) — An intrinsic [planet property]({{< relref "habitability.md" >}}) (0–25) that sets how much population and farming its surface supports and whether open-air colonies are allowed.
- **Home system** — The solar system a player starts in; its planets are described in the player's initial turn report.
- **Hyper engine** (`HPD`) — A unit that propels a ship through hyper-space, within a system or between systems.
- **Hyper-space** — The medium hyper engines travel through; jump range is measured in light years.

## J

- **Jump** — A ship's movement through hyper-space. Every jump must end at an interplanetary or interstellar location, never in deep space.

## L

- **Life support** (`LSP`) — A unit that recycles air and water; required by ships and enclosed colonies.

## M

- **Market** — The home-planet market (and trade stations) where gold is exchanged for consumer goods and units are traded.
- **Mass unit** (`MU`) — The standard measure of mass, and of resource quantity.
- **Metallic resources** (`METS`) — Mined raw material (metals other than gold) consumed by factories.
- **Military robot** (`MRBT`) — A unit that replaces soldier units in combat.
- **Military supplies** (`MTSP`) — Ammunition, medicines, and the like, consumed by soldiers during combat.
- **Mine** (`MINE`) — A production unit that extracts a resource from a deposit; works only at a surface colony. See [Mining]({{< relref "mining.md" >}}).
- **Mine group** — A set of `MINE` units assigned to a single deposit. Each deposit has at most one mine group.
- **Missile** (`MSS`) — An indirect combat weapon launched by a missile launcher.
- **Missile launcher** (`MSL`) — A unit that launches missiles and anti-missiles.
- **Morale** — A population's contentment; declines when the actual ration falls below a full ration. See [Food]({{< relref "food.md#morale" >}}).

## N

- **Non-combat death rate** — The per-turn population loss rate from ordinary mortality rather than combat. See [Population]({{< relref "population.md#unit-types" >}}).
- **Nation** — The polity a single player governs. A planet holds up to 25 nations, which together form a race.
- **Natural resource** — One of the four substances held in a planet's [deposits]({{< relref "planets.md#natural-resources" >}}): GOLD, FUEL, METS, or NMTS.
- **Non-metallic resources** (`NMTS`) — Mined raw material (non-metals) consumed by factories.

## O

- **Open-air colony** (`COPN`) — A surface colony exposed to the planet's environment; allowed only where HN > 0, and the only colony that may use `FARM-1`.
- **Orbit** — One of a star's ten numbered positions (1 closest, 10 farthest); any may hold a planet.
- **Orbiting colony** (`CORB`) — A colony in orbit around a planet; requires life support and cannot mine.

## P

- **Planet** — A body occupying an [orbit]({{< relref "game-setup.md#stars-and-orbits" >}}); the basic site for colonies, mining, and farming. One of three types, with a habitability number and natural resources. See [Planets]({{< relref "planets.md" >}}).
- **Pay** — Consumer goods or gold given to population units. Colony population pay is expressed in `CNGD`; ship crew wages are expressed in `GOLD`. See [Population]({{< relref "population.md" >}}).
- **Population unit** — A unit of citizens. Population classes are `USK`, `PRO`, `SLD`, and `UEM`; population cadres are `TRN`, `SPY`, `CNW`, and `RBL`. See [Population]({{< relref "population.md" >}}).
- **Probe** — A sensor scan that reports a planet in the same system: its ships and colonies, its resource deposits (type and approximate quantity), and its habitability number.
- **Production unit** — A unit that turns inputs into output: a mine, farm, or factory. See [The Production Cycle]({{< relref "../explanation/production-cycle.md" >}}).
- **Professional** (`PRO`) — Skilled population requiring long apprenticeships; needed to manage production units.

## R

- **Race** — All the nations on one planet, considered together; the basis of a future [Race Victory]({{< relref "victory-conditions.md" >}}).
- **Ration** — The FOOD served per population unit per turn, set by a `RATION` order. A full ration is 0.25 FOOD units. See [Food]({{< relref "food.md" >}}).
- **Rebel** (`RBL`) — A tally of population willing to rebel, not a separate class; rises with underpayment, underfeeding, and especially starvation.
- **Research point** (`RSCH`) — Output used to pay for technological advancement.
- **Resource** — A farmed or mined substance: FOOD, METS, NMTS, FUEL, or GOLD.

## S

- **Sensor** (`SEN`) — A unit that reports on solar systems and on ships and colonies, and conducts probes.
- **Ship** (`SHIP`) — A mobile entity that can move between orbits and systems; requires life support and cannot host factories or mines.
- **Ship/colony** (S/C) — Collective term for an entity — that is, either a ship or a colony.
- **Soldier** (`SLD`) — Military population.
- **Solar system** — A set of one or more stars sharing the same co-ordinates. Named by its co-ordinates alone (e.g. `12-13-14`); each of its stars adds a letter suffix.
- **Space drive** (`SPD`) — A unit that maintains a ship's orbit and maneuvers it in combat; cannot be used for interplanetary or interstellar travel.
- **Spy** (`SPY`) — A population-cadre allocation of 1 professional and 1 soldier that reports on other players and incites rebellion.
- **Standard of living** (`SOL`) — A measure of population well-being, shaped by pay and rations, that bears on morale.
- **Star** — A stellar body within a solar system. Identified by the system co-ordinates plus a letter suffix (`A`, `B`, `C`, …) — for example `12-13-14A` — which is required even in a single-star system.
- **Starvation** — Loss of population when the actual ration falls below the survival ration (25% of a full ration). See [Food]({{< relref "food.md#starvation" >}}).
- **Structural unit** (`STU`) — The framing required to build ships and colonies.
- **Surface colony** — An open-air or enclosed colony on a planet's surface (as distinct from an orbiting colony). Only a surface colony may mine.
- **Survey** — A scan from a ship or colony at a planet that reports its deposits' locations, types, and exact resource quantities.

## T

- **Technological level** (`TL`) — A unit's tech rating, which sets its mass, cost, and effectiveness.
- **Terrestrial** — A spherical [planet]({{< relref "planets.md#types" >}}) type, not necessarily "earth-like." Habitability number 0–25.
- **Trade station** — An installation for trade between players; it can also establish control of a planet.
- **Trainee** (`TRN`) — A population-cadre allocation of an unskilled worker being trained into a professional.
- **Transport** (`TPT`) — A unit that moves units between ships and colonies and carries soldiers into combat.
- **Trinary system** — A solar system containing three stars.
- **Turn** — One game cycle, equal to one quarter of a Galactic standard year.

## U

- **Unemployables** (`UEM`) — All citizens not represented by the working or soldier classes; all birth increases enter this category.
- **Unit** — Any item that may be held by a ship or colony. See [Units]({{< relref "units.md" >}}) for the full catalog.
- **Unskilled worker** (`USK`) — Population providing labor that needs little training.

## W

- **Weapon** — A combat unit: `ASW`, `ASC`, `MRBT`, `MSS`, `MSL`, `ANM`, `EWP`, `ESH`, or `MTSP`. See [Units]({{< relref "units.md#weapons" >}}).
- **Work in process** (`WIP`) — A production unit's accumulated progress toward its output, advancing 25% per active turn. See [Shortages]({{< relref "shortages.md#work-in-process-and-timing" >}}).

## Y

- **Yield** — A deposit's fixed percentage that sets how much of a mine group's extraction becomes usable product each turn. See [Mining]({{< relref "mining.md#yield" >}}).
