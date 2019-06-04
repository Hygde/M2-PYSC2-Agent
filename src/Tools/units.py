from pysc2.lib.units import Terran, Zerg, Protoss
from enum import IntEnum

class TerranAirArmy(IntEnum):
    Viking = Terran.VikingFighter.value
    Medivac = Terran.Medivac.value
    Liberator = Terran.Liberator.value
    Raven = Terran.Raven.value
    Banshee = Terran.Banshee.value
    BattleCruiser = Terran.Battlecruiser.value
    CommandCenterFlying = Terran.CommandCenterFlying.value
    Barrack = Terran.BarracksFlying.value
    OrbitalCommandFlying = Terran.OrbitalCommandFlying.value
    Factory = Terran.FactoryFlying.value
    Starport = Terran.StarportFlying.value

class TerranGroundArmy(IntEnum):
    Viking = Terran.VikingAssault.value
    Marine = Terran.Marine.value
    Marauder = Terran.Marauder.value
    Reaper = Terran.Reaper.value
    Ghost = Terran.Ghost.value
    Hellion = Terran.Hellion.value
    Hellbat = Terran.Hellbat.value
    SiegeTank = Terran.SiegeTank.value
    SiegeTankSieged = Terran.SiegeTankSieged.value
    Cyclone = Terran.Cyclone.value
    WidowMine = Terran.WidowMine.value
    Thor = Terran.Thor.value

class ZergAirArmy(IntEnum):
    Overlord = Zerg.Overlord.value
    OverlordCocoon = Zerg.OverseerCocoon.value
    Overseer = Zerg.Overseer.value
    OverseerCocoon = Zerg.OverseerCocoon.value
    Mutalisk = Zerg.Mutalisk.value
    Corruptor = Zerg.Corruptor.value
    BroodLord =  Zerg.BroodLord.value
    BroodLordCocoon = Zerg.BroodLordCocoon.value
    Viper = Zerg.Viper.value
    LocustFlying = Zerg.LocustFlying.value

class ZergGroundArmy(IntEnum):
    Queen = Zerg.Queen.value
    Zergling = Zerg.Zergling.value
    Baneling = Zerg.Baneling.value
    Roach = Zerg.Roach.value
    Ravager = Zerg.Ravager.value
    Hydralisk = Zerg.Hydralisk.value
    Infestor = Zerg.Infestor.value
    SwarmHost = Zerg.SwarmHost.value
    Ultralisk = Zerg.Ultralisk.value
    Locust = Zerg.Locust.value
    Broodling = Zerg.Broodling.value
    Changeling = Zerg.Changeling.value
    InfestedTerran = Zerg.InfestedTerran.value

class ProtossAirArmy(IntEnum):
    Observer = Protoss.Observer.value
    ObserverSurveillanceMode = Protoss.ObserverSurveillanceMode.value
    WarpPrism = Protoss.WarpPrism.value
    WarpPrismPhased = Protoss.WarpPrismPhasing.value
    Phoenix = Protoss.Phoenix.value
    VoidRay = Protoss.VoidRay.value
    Oracle = Protoss.Oracle.value
    Carrier = Protoss.Carrier.value
    Tempest = Protoss.Tempest.value
    MothershipCore = Protoss.MothershipCore.value
    Mothership = Protoss.Mothership.value

class ProtossGroundArmy(IntEnum):
    Zealot = Protoss.Zealot.value
    Stalker = Protoss.Stalker.value
    Sentry = Protoss.Sentry.value
    Adept = Protoss.Adept.value
    HighTemplar = Protoss.HighTemplar.value
    DarkTemplar = Protoss.DarkTemplar.value
    Immortal = Protoss.Immortal.value
    Colossus = Protoss.Colossus.value
    Disruptor = Protoss.Disruptor.value
    Archon = Protoss.Archon.value