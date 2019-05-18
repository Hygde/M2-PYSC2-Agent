from Actions import SC2Action
from pysc2.lib import actions, units

## Package class which defines general functions of unit training
class _TrainUnits(SC2Action):

    ## Contructor of the class
    # @param ntrain defines the number of units to train
    def __init__(self, ntrain):
        super(_TrainUnits, self).__init__()
        self._duration = 1
        self._ntrain = ntrain

    ## This function sets the rally point of selected buildings
    def _setRallyPoint(self, coord_xy):
        self._logger.debug(coord_xy)
        return actions.FUNCTIONS.FunctionCall(actions.FUNCTIONS.Rally_Units_minimap.id, [self._NOT_QUEUED, coord_xy])

    ## This function returns a no_op action. It must be implemented in child class
    # @param obs is the handler of the current state of the game
    def action(self, obs):return super(_TrainUnits, self).action(obs)
