from pysc2.lib import features, actions
import logging

class SC2Action:

    #features
    _PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
    _UNIT_TYPE = features.SCREEN_FEATURES.unit_type.index
    _SELECTED = features.SCREEN_FEATURES.selected.index

    #params
    _SELF = 1
    _NOT_QUEUED = [0]
    _QUEUED = [1]

    def __init__(self):
        self._logger = logging.getLogger("SC2Action")
        self._iteration = 0
        self._duration = 1

    def action(self, obs):
        self._logger.debug("Performing action")
        return actions.FUNCTIONS.no_op()

    def isFinished(self):
        result = self._iteration >= self._duration
        self._logger.debug(result)
        return result