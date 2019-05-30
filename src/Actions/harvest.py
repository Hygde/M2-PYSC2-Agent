import numpy as np
from enum import IntEnum
from .sc2action import SC2Action
from pysc2.lib import actions, units

## This function defines the way to gather ressources
class Harvest(SC2Action):

    ## To gather a resource at a location
    __GATHER = actions.FUNCTIONS.Harvest_Gather_screen.id

    ## Constructor of the class
    def __init__(self, resource_type, coord_xy=np.array([]), queued=False):
        super(Harvest, self).__init__()
        self._coord_xy = np.array([[]]) if type(coord_xy) == type(None) else np.array([coord_xy])
        self._resource_type = resource_type
        self._queued_state = self._QUEUED if queued else self._NOT_QUEUED

    ## This function defines the way to gather resources
    def action(self, obs):
        result = super(Harvest, self).action(obs)
        if self._coord_xy.size == 0:self._coord_xy = np.array([[res.x, res.y] for res in obs.observation.feature_units if res.unit_type == self._resource_type])
        if self.__GATHER in obs.observation.available_actions:
            result = actions.FunctionCall(self.__GATHER, [self._queued_state, self._coord_xy[0]])
            self._iteration += 1
        return result