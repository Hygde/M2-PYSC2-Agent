from .sc2action import SC2Action
from pysc2.lib import units, actions

## This class defines an easy way to set rally points
class RallyPoint(SC2Action):
    ## Constructor of the class
    # @param unit_type defines the selected production unit
    # @param coord_xy is the new position of the rally point
    # @param queued defines the queued state of the action
    def __init__(self, unit_type, coord_xy, queued=False):
        super(RallyPoint, self).__init__()
        self._rally_func = self._getFunction(unit_type)
        self._rally_position = coord_xy
        self._queued_state = self._QUEUED if queued else self._NOT_QUEUED

    ## This function returns the right rally point function according to the production unit
    # @param unit_type is the production unit
    def _getFunction(self, unit_type):
        result = actions.FUNCTIONS.Rally_Units_screen.id
        if unit_type == units.Terran.CommandCenter:result = actions.FUNCTIONS.Rally_Workers_screen.id
        return result

    ## This function defines the way to set the rally point
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(RallyPoint, self).action(obs)
        if self._rally_func in obs.observation.available_actions:
            result = actions.FunctionCall(self._rally_func, [self._queued_state, self._rally_position])
            self._iteration += 1
        return result