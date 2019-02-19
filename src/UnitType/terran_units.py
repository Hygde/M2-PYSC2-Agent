from enum import Enum

# SRC :
# https://github.com/Blizzard/s2client-api/blob/master/include/sc2api/sc2_typeenums.h

class TerranUnits(Enum):
    ARMORY = 29# CANCEL, HALT, CANCEL_LAST, RESEARCH_TERRANSHIPWEAPONS, RESEARCH_TERRANVEHICLEANDSHIPPLATING, RESEARCH_TERRANVEHICLEWEAPONS
    AUTOTURRET = 31# SMART, STOP, ATTACK
    BANSHEE = 55# SMART, MOVE, PATROL, HOLDPOSITION, STOP, ATTACK, BEHAVIOR_CLOAKON, BEHAVIOR_CLOAKOFF
    BARRACKS = 21# SMART, TRAIN_MARINE, TRAIN_REAPER, TRAIN_GHOST, TRAIN_MARAUDER, CANCEL, HALT, CANCEL_LAST, RALLY_UNITS, LIFT, BUILD_TECHLAB, BUILD_REACTOR
    BARRACKSFLYING = 46# SMART, MOVE, PATROL, HOLDPOSITION, STOP, LAND, BUILD_TECHLAB, BUILD_REACTOR
    BARRACKSREACTOR = 38# CANCEL
    BARRACKSTECHLAB = 37# RESEARCH_STIMPACK, RESEARCH_COMBATSHIELD, RESEARCH_CONCUSSIVESHELLS, CANCEL, CANCEL_LAST
    BATTLECRUISER = 57# SMART, MOVE, PATROL, HOLDPOSITION, EFFECT_YAMATOGUN, EFFECT_TACTICALJUMP, STOP, ATTACK
    BUNKER = 24# SMART, EFFECT_SALVAGE, CANCEL, HALT, UNLOADALL, STOP, LOAD, RALLY_UNITS, ATTACK, EFFECT_STIM
    COMMANDCENTER = 18# SMART, TRAIN_SCV, MORPH_PLANETARYFORTRESS, MORPH_ORBITALCOMMAND, CANCEL, HALT, LOADALL, UNLOADALL, CANCEL_LAST, LIFT, RALLY_WORKERS
    COMMANDCENTERFLYING = 36# SMART, MOVE, PATROL, HOLDPOSITION, LOADALL, UNLOADALL, STOP, LAND
    CYCLONE = 692# SMART, MOVE, PATROL, HOLDPOSITION, EFFECT_LOCKON, CANCEL, STOP, ATTACK
    ENGINEERINGBAY = 22# RESEARCH_HISECAUTOTRACKING, RESEARCH_TERRANSTRUCTUREARMORUPGRADE, RESEARCH_NEOSTEELFRAME, CANCEL, HALT, CANCEL_LAST, RESEARCH_TERRANINFANTRYARMOR, RESEARCH_TERRANINFANTRYWEAPONS
    FACTORY = 27# SMART, TRAIN_SIEGETANK, TRAIN_THOR, TRAIN_HELLION, TRAIN_HELLBAT, TRAIN_CYCLONE, TRAIN_WIDOWMINE, CANCEL, HALT, CANCEL_LAST, RALLY_UNITS, LIFT, BUILD_TECHLAB, BUILD_REACTOR
    FACTORYFLYING = 43# SMART, MOVE, PATROL, HOLDPOSITION, STOP, LAND, BUILD_TECHLAB, BUILD_REACTOR
    FACTORYREACTOR = 40# CANCEL
    FACTORYTECHLAB = 39# RESEARCH_INFERNALPREIGNITER, RESEARCH_DRILLINGCLAWS, RESEARCH_RAPIDFIRELAUNCHERS, RESEARCH_SMARTSERVOS, CANCEL, CANCEL_LAST
    FUSIONCORE = 30# RESEARCH_BATTLECRUISERWEAPONREFIT, CANCEL, HALT, CANCEL_LAST
    GHOST = 50# SMART, MOVE, PATROL, HOLDPOSITION, EFFECT_NUKECALLDOWN, EFFECT_EMP, EFFECT_GHOSTSNIPE, CANCEL, STOP, ATTACK, BEHAVIOR_CLOAKON, BEHAVIOR_CLOAKOFF, BEHAVIOR_HOLDFIREON, BEHAVIOR_HOLDFIREOFF
    GHOSTACADEMY = 26# BUILD_NUKE, RESEARCH_PERSONALCLOAKING, CANCEL, HALT, CANCEL_LAST
    HELLION = 53# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_HELLBAT, STOP, ATTACK
    HELLIONTANK = 484# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_HELLION, STOP, ATTACK
    LIBERATOR = 689# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_LIBERATORAGMODE, STOP, ATTACK
    LIBERATORAG = 734# SMART, MORPH_LIBERATORAAMODE, STOP, ATTACK
    MARAUDER = 51# SMART, MOVE, PATROL, HOLDPOSITION, STOP, ATTACK, EFFECT_STIM
    MARINE = 48# SMART, MOVE, PATROL, HOLDPOSITION, STOP, ATTACK, EFFECT_STIM
    MEDIVAC = 54# SMART, MOVE, PATROL, HOLDPOSITION, EFFECT_HEAL, EFFECT_MEDIVACIGNITEAFTERBURNERS, STOP, LOAD, UNLOADALLAT, ATTACK
    MISSILETURRET = 23# SMART, CANCEL, HALT, STOP, ATTACK
    MULE = 268# SMART, MOVE, PATROL, HOLDPOSITION, STOP, HARVEST_GATHER, HARVEST_RETURN, ATTACK, EFFECT_REPAIR
    ORBITALCOMMAND = 132# SMART, EFFECT_CALLDOWNMULE, EFFECT_SUPPLYDROP, EFFECT_SCAN, TRAIN_SCV, CANCEL_LAST, LIFT, RALLY_WORKERS
    ORBITALCOMMANDFLYING = 134# SMART, MOVE, PATROL, HOLDPOSITION, STOP, LAND
    PLANETARYFORTRESS = 130# SMART, TRAIN_SCV, LOADALL, STOP, CANCEL_LAST, ATTACK, RALLY_WORKERS
    RAVEN = 56# SMART, MOVE, PATROL, HOLDPOSITION, EFFECT_POINTDEFENSEDRONE, EFFECT_HUNTERSEEKERMISSILE, EFFECT_AUTOTURRET, STOP, ATTACK
    REAPER = 49# SMART, MOVE, PATROL, HOLDPOSITION, EFFECT_KD8CHARGE, STOP, ATTACK
    REFINERY = 20# CANCEL, HALT
    SCV = 45# SMART, MOVE, PATROL, HOLDPOSITION, BUILD_COMMANDCENTER, BUILD_SUPPLYDEPOT, BUILD_REFINERY, BUILD_BARRACKS, BUILD_ENGINEERINGBAY, BUILD_MISSILETURRET, BUILD_BUNKER, BUILD_SENSORTOWER, BUILD_GHOSTACADEMY, BUILD_FACTORY, BUILD_STARPORT, BUILD_ARMORY, BUILD_FUSIONCORE, HALT, STOP, HARVEST_GATHER, HARVEST_RETURN, ATTACK, EFFECT_SPRAY, EFFECT_REPAIR
    SENSORTOWER = 25# CANCEL, HALT
    SIEGETANK = 33# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_SIEGEMODE, STOP, ATTACK
    SIEGETANKSIEGED = 32# SMART, MORPH_UNSIEGE, STOP, ATTACK
    STARPORT = 28# SMART, TRAIN_MEDIVAC, TRAIN_BANSHEE, TRAIN_RAVEN, TRAIN_BATTLECRUISER, TRAIN_VIKINGFIGHTER, TRAIN_LIBERATOR, CANCEL, HALT, CANCEL_LAST, RALLY_UNITS, LIFT, BUILD_TECHLAB, BUILD_REACTOR
    STARPORTFLYING = 44# SMART, MOVE, PATROL, HOLDPOSITION, STOP, LAND, BUILD_TECHLAB, BUILD_REACTOR
    STARPORTREACTOR = 42# CANCEL
    STARPORTTECHLAB = 41# RESEARCH_BANSHEECLOAKINGFIELD, RESEARCH_RAVENCORVIDREACTOR, RESEARCH_ENHANCEDMUNITIONS, RESEARCH_BANSHEEHYPERFLIGHTROTORS, RESEARCH_RAVENRECALIBRATEDEXPLOSIVES, RESEARCH_HIGHCAPACITYFUELTANKS, RESEARCH_ADVANCEDBALLISTICS, CANCEL, CANCEL_LAST
    SUPPLYDEPOT = 19# MORPH_SUPPLYDEPOT_LOWER, CANCEL, HALT
    SUPPLYDEPOTLOWERED = 47# MORPH_SUPPLYDEPOT_RAISE
    THOR = 52# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_THORHIGHIMPACTMODE, STOP, ATTACK
    THORAP = 691# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_THOREXPLOSIVEMODE, CANCEL, STOP, ATTACK
    VIKINGASSAULT = 34# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_VIKINGFIGHTERMODE, STOP, ATTACK
    VIKINGFIGHTER = 35# SMART, MOVE, PATROL, HOLDPOSITION, MORPH_VIKINGASSAULTMODE, STOP, ATTACK
    WIDOWMINE = 498# SMART, MOVE, PATROL, HOLDPOSITION, BURROWDOWN, STOP, ATTACK
    WIDOWMINEBURROWED = 500# SMART, EFFECT_WIDOWMINEATTACK, BURROWUP