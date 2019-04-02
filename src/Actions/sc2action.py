from pysc2.lib import features, actions
import logging

## This class is the parent of all SC2 actions
class SC2Action:

    #features
    _PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
    _UNIT_TYPE = features.SCREEN_FEATURES.unit_type.index
    _SELECTED = features.SCREEN_FEATURES.selected.index

    #params
    _SELF = 1
    _NOT_QUEUED = [0]
    _QUEUED = [1]

    ## Contructor of the SC2Action class
    def __init__(self):
        self._logger = logging.getLogger("SC2Action")
        self._iteration = 0
        self._duration = 1

    ## This function performs is a standard no op function
    # @param obs defines the observation of the current state of the game
    def action(self, obs):
        self._logger.debug("Performing action")
        return actions.FUNCTIONS.no_op()

    ## This function tests if the current action is finished
    def isFinished(self):
        result = self._iteration >= self._duration
        self._logger.debug(result)
        return result