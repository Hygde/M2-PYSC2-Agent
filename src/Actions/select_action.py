from .sc2action import SC2Action
from pysc2.lib import features, actions

import numpy as np
from enum import IntEnum

## This class defines the different selection type
class SelectType(IntEnum):
    ## Selects only on unit
    SINGLE = 0
    ## Selects all the units of a type
    ALL_TYPE = 1
    ## Selects the army ignoring the unit type
    ARMY = 2

## This class defines the way to select N units
# @param SC2Action is the base class that defines all generalities of SC2 actions
class SelectAction(SC2Action):

    ## Constructor of SelectAction class
    # @param unit_type is the type of units to select
    # @param n_select defines the number of units to select
    def __init__(self, unit_type, kind=None):
        super(SelectAction, self).__init__()
        self._duration = 1
        self._unit_type = unit_type
        self._kind = kind

    def __getUnitsOfType(self, obs, unit_type):
        return np.array([[unit.x, unit.y] for unit in obs.observation.feature_units if unit.unit_type == unit_type and unit.is_selected == False])

    def __select_single(self, coord_xy):
        return actions.FUNCTIONS.select_point("select", coord_xy)

    def __select_all_type(self, coord_xy):
        return actions.FUNCTIONS.select_point("select_all_type", coord_xy)

    def __select_army(self):return actions.FUNCTIONS.select_army("select")

    ## This function performs a selection of N units
    # @param obs defines the observation of the current state of the game
    def action(self, obs):
        result = super(SelectAction, self).action(obs)#return no_op()
        units = self.__getUnitsOfType(obs, self._unit_type)
        if self._iteration == 0:
            if self._kind == SelectType.SINGLE:result = self.__select_single(units[0])
            elif self._kind == SelectType.ALL_TYPE:result = self.__select_all_type(units[0])
            elif self._kind == SelectType.ARMY:result = self.__select_army()
        self._iteration += 1
        return result