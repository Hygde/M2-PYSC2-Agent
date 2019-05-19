from ._trainunits import _TrainUnits
from pysc2.lib import actions, units

## This class defines an easy way to train SCV
class _TrainCommandCenterUnits(_TrainUnits):

    __TRAIN_SCV = actions.FUNCTIONS.Train_SCV_quick.id

    def __init__(self, ntrain):
        super(_TrainCommandCenterUnits, self).__init__(ntrain)

    ## This function defines the way to create N-SCV
    # obs is the handler of the current state of the game
    def action(self, obs):
        result = super(_TrainCommandCenterUnits, self).action(obs)
        if self.__TRAIN_SCV in obs.observation["available_actions"]:
            self._logger.debug("Adding one unit to training queue")
            result = actions.FunctionCall(self.__TRAIN_SCV, [self._NOT_QUEUED])
            self._ntrain -= 1
            if self._ntrain == 0:self._iteration += 1
        return result
