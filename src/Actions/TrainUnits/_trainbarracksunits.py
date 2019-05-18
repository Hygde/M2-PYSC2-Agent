from ._trainunits import _TrainUnits
from pysc2.lib import units, actions

## This class defines the way to train barracks units
class _TrainBarracksUnits(_TrainUnits):

    ## Constructor of the class
    # @param unit_type defines the unit to train
    # @param ntrain defines the number of units to train
    def __init__(self, unit_type, ntrain):
        super(TrainBarracksUnits, self).__init__(ntrain)
        self._train_func = self._getTrainFunction(unit_type)

    ## This function returns the train action according to the unit_type
    # @param unit_type defines the unit to train
    def _getTrainFunction(self, unit_type):
        result = actions.FUNCTIONS.Train_Marine_quick.id
        if unit_type == units.Terran.Marauder: result = actions.FUNCTIONS.Train_Marauder_quick.id
        elif unit_type == units.Terran.Reaper: result = actions.FUNCTIONS.Train_Reaper_quick.id
        elif unit_type == units.Terran.Ghost: result = actions.FUNCTIONS.Train_Ghost_quick.id
        return result

    ## This function defines the cay to train barracks units
    # @apram obs is the handler of the current state of the game
    def action(self, obs):
        result = super(TrainBarracksUnits, self).action(obs)
        if self._train_func in obs.observation["available_actions"]:
            self._logger.debug("Adding one unit to training queue")
            result = actions.FunctionCall(self._train_func, [self._NOT_QUEUED])
            self._ntrain -= 1
            if self._ntrain == 0:self._iteration += 1
        return result