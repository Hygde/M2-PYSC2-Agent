from Actions import SC2Action
from pysc2.lib import actions, units

## Package class which defines general functions of unit training
class TrainUnits(SC2Action):

    ## Contructor of the class
    # @param ntrain defines the number of units to train
    def __init__(self, unit_type, ntrain):
        super(TrainUnits, self).__init__()
        self._duration = 1
        self._train_func = self._getTrainFunction(unit_type)
        self._ntrain = ntrain

    ## This function sets the rally point of selected buildings
    def _setRallyPoint(self, coord_xy):
        self._logger.debug(coord_xy)
        return actions.FUNCTIONS.FunctionCall(actions.FUNCTIONS.Rally_Units_minimap.id, [self._NOT_QUEUED, coord_xy])

    ## This function returns the train action according to the unit_type
    # @param unit_type defines the unit to train
    def _getTrainFunction(self, unit_type):
        result = None
        if unit_type == units.Terran.SCV:result = actions.FUNCTIONS.Train_SCV_quick.id
        elif unit_type == units.Terran.Marine:result = actions.FUNCTIONS.Train_Marine_quick.id
        elif unit_type == units.Terran.Marauder: result = actions.FUNCTIONS.Train_Marauder_quick.id
        elif unit_type == units.Terran.Reaper: result = actions.FUNCTIONS.Train_Reaper_quick.id
        elif unit_type == units.Terran.Ghost: result = actions.FUNCTIONS.Train_Ghost_quick.id
        return result

    ## This function returns a no_op action. It must be implemented in child class
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(TrainUnits, self).action(obs)
        self._logger.debug(self._train_func in obs.observation.available_actions)
        if self._train_func in obs.observation.available_actions:
            self._logger.debug("Adding one unit to training queue")
            result = actions.FunctionCall(self._train_func, [self._NOT_QUEUED])
            self._ntrain -= 1
            if self._ntrain == 0:self._iteration += 1
        return result

