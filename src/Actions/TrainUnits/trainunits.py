from pysc2.lib import units
from ._trainbarracksunits import _TrainBarracksUnits
from ._traincommandcenterunits import _TrainCommandCenterUnits

def __isBarracksUnit(unit_type):return units.Terran.Marine <= unit_type <= units.Terran.Marauder
def __isCommandCentersUnit(unit_type):return unit_type == units.Terran.SCV

## This function returns the right training unit class
def TrainUnits(unit_type, ntrain):
    result = None
    if __isBarracksUnit(unit_type):result = _TrainBarracksUnits(unit_type, ntrain)
    if __isCommandCentersUnit(unit_type): result = _TrainCommandCenterUnits(ntrain)
    return result