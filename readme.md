# Protoss agent

## Requierement pysc2 2.0
The installation procedure is available here : [https://github.com/deepmind/pysc2](https://github.com/deepmind/pysc2 "Installation procedure")

## Run the agent
Here is the command to run the agent:
python3 -m pysc2.bin.agent --agent agent.Agent --map Simple64 --agent_race protoss --use_feature_units True

## Goals
Here is the list of the goals:
* element 1
* element 2
* etc.

## Brainstorming

* AI based upon unit microgestion (Unit abilities)
    * Protoss
        * High templar (Disruption, psionic storm)
        * Sentry (Force field, plasma shieGenerate sc2 ld)
        * Disruptor (???)
        * Mothership (Timewarp, Mass recall)
        * Warp Prism (Phasing mode)
    * Terran
        * Raven (Auto-turret, Interference matrix, Missile)
    * Zerg
        * Infestator(Neural parasite, Fungal Growth, Infested Terran)
        * Viper (Blinding cloud, Abduct, Parasitic Bomb)
        
    * Global notes:
        * Think about support units coming with the duo micro units (Potential learning).
        * Think about the best way to interact between the duo units (Potential learning).
        * Use of the environments (Unit abilities + environments) (Potential learning).
        * Reactivity to enemy composition and key use of abilities (Potential learning).
* Counter AI:
    * Global Notes:
        * Learn about countering enemy composition (Potential learning).
        * Find ultimate counter to specific composition (Potential learning).
        * Find counter considering current state (Potential learning).
            * Current technology tree.
            * Shades of countering (Dilemna, building tech for better unit or using current ones).
        * Problem with reactivity (Building takes time, weight on best units (for race), unit building properties).
        
## Wrapper

* Fonctions (Implicitly implement highest queue priority):
    * Select Unit (Coordinates)
    * Select Group Unit (Mono) 
        * Select all of unit type
        * Select amount of unit type
        * Selection with zone of units (rectangular)
    
    * Move selected units
        * Use minimap
        * Use Screen
    * Do function (Général) (Compliquer)
    * Create building
    * Create unit
    * Move screen
        * Use screen
        * Use minimap
    * Attack with selected units:
        * Coordinates
        * Unit

## Counter Rush

* Course of action:
    1) Find the right timing to build the wall
    2) Find the right position for:
        1) Supply D * 2
        2) Barrack
    3) Find the right timing to counter
    4) What if, there's is no rush?
    5) What's next if game is still ongoing?