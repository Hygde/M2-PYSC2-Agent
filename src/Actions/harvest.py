import numpy as np
from enum import IntEnum
from .sc2action import SC2Action
from pysc2.lib import actions, units

## This function defines the way to gather ressources
class Harvest(SC2Action):

    ## To return to the previous gathering type
    __RETURN = actions.FUNCTIONS.Harvest_Return_quick.id
    ## To gather a resource at a location
    __GATHER = actions.FUNCTIONS.Harvest_Gather_SCV_screen.id

    ## Constructor of the class
    def __init__(self, resource_type=None, queued=False):
        super(Harvest, self).__init__()
        self._harvest_type = self.__RETURN if resource_type == None else self.__GATHER
        self._resource_type = resource_type
        self._queued_state = self._QUEUED if queued else self._NOT_QUEUED

    ## This function defines the way to gather resources
    def action(self, obs):
        result = super(Harvest, self).action(obs)
        coord_xy = np.array([[res.x, res.y] for res in obs.observation.feature_units if res.unit_type == self._resource_type])
        if self._harvest_type in obs.observation["available_actions"]:
            if self._harvest_type == self.__RETURN:result = actions.FunctionCall(self._harvest_type, [self._queued_state])
            elif len(coord_xy):
                result = actions.FunctionCall(self._harvest_type,[self._queued_state, [coord_xy[0]]])
            else:self._iteration -= 1
            self._iteration += 1
        return result