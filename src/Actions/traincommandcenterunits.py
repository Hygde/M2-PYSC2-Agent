from ._trainunits import _TrainUnits
from .select_action import SelectAction, SelectType
from pysc2.lib import actions, units


class TrainCommandCenterUnits(_TrainUnits):

    __TRAIN_SCV = actions.FUNCTIONS.Train_SCV_quick.id

    def __init__(self, ntrain):
        super(TrainCommandCenterUnits, self).__init__(units.Terran.CommandCenter, SelectType.SINGLE, ntrain)

    def action(self, obs):
        result = super(TrainCommandCenterUnits, self).action(obs)
        if self._iteration == 0:
            self._logger.debug("self._iteration == 0")
            result = self._selector.action(obs)
            self._iteration += 1
        elif self._iteration == 1 and self.__TRAIN_SCV in obs.observation["available_actions"]:
            self._logger.debug("self._iteration == 1")
            result = actions.FunctionCall(self.__TRAIN_SCV, [self._NOT_QUEUED])
            self._ntrain -= 1
            if self._ntrain == 0:self._iteration += 1
        return result
