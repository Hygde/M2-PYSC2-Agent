from .sc2action import SC2Action
from pysc2.lib import features, actions

## This class defines the way to select N units
# @param SC2Action is the base class that defines all generalities of SC2 actions
class SelectAction(SC2Action):

    ## Constructor of SelectAction class
    # @param unit_type is the type of units to select
    # @param n_select defines the number of units to select
    def __init__(self, unit_type, n_select):
        super(SelectAction, self).__init__()
        self._duration = 1
        self._unit_type = unit_type
        self._n_select = n_select

    def __getUnitsOfType(self, obs, unit_type):
        return [unit for unit in obs.observation.feature_units if unit.unit_type == unit_type]

    def __select_single(self, coord_yx):
        coord_xy = [coord_yx.x, coord_yx.y]
        return actions.FUNCTIONS.select_point("select", coord_xy)

    def __select_all_type(self, coord_yx):
        coord_xy = [coord_yx.x, coord_yx.y]
        return actions.FUNCTIONS.select_point("select_all_type", coord_xy)

    ## This function performs a selection of N units
    # @param obs defines the observation of the current state of the game
    def action(self, obs):
        result = super(SelectAction, self).action(obs)#return no_op()
        if self._iteration == 0:
            units = self.__getUnitsOfType(obs, self._unit_type)
            if self._n_select == 1: result = self.__select_single(units[0])
            elif self._n_select > 1: pass
            elif self._n_select == -1:result = self.__select_all_type(units[0])
        return result