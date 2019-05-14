from ._trainunits import _TrainUnits
from pysc2.lib import units, actions

class TrainBarracksUnits(_TrainUnits):

    def __init__(self, select_type, unit_type, ntrain):
        super(TrainBarracksUnits, self).__init__(units.Terran.Barracks, select_type, ntrain)
        self._train_func = self._getTrainFunction(unit_type)

    def _getTrainFunction(self, unit_type):
        result = None
        if unit_type == units.Terran.Marine:result = actions.FUNCTIONS.Train_Marine_quick.id
        elif unit_type == units.Terran.Marauder: result = actions.FUNCTIONS.Train_Marauder_quick.id
        elif unit_type == units.Terran.Reaper: result = actions.FUNCTIONS.Train_Reaper_quick.id
        elif unit_type == units.Terran.Ghost: result = actions.FUNCTIONS.Train_Ghost_quick.id
        return result

    def action(self, obs):
        result = super(TrainBarracksUnits, self).action(obs)
        if self._iteration == 0:
            self._logger.debug("self._iteration == 0")
            result = self._selector.action(obs)
            if self._selector.isFinished():self._iteration += 1
        elif self._iteration == 1 and self._train_func in obs.observation["available_actions"]:
            self._logger.debug("self._iteration == 1")
            result = actions.FunctionCall(self._train_func, [self._NOT_QUEUED])
            self._ntrain -= 1
            if self._ntrain == 0:self._iteration += 1
        return result