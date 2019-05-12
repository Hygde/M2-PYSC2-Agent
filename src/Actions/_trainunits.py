from .sc2action import SC2Action
from .select_action import SelectAction

from pysc2.lib import actions

class _TrainUnits(SC2Action):

    def __init__(self, building, select_type, ntrain):
        super(_TrainUnits, self).__init__()
        self._selector = SelectAction(building, select_type)
        self._duration = 2
        self._ntrain = ntrain

    def _setRallyPoint(self, coord_xy):
        self._logger.debug(coord_xy)
        return actions.FUNCTIONS.FunctionCall(actions.FUNCTIONS.Rally_Units_minimap.id, [self._NOT_QUEUED, coord_xy])

    def action(self, obs):
        return super(_TrainUnits, self).action(obs)
