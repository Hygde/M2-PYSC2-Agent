from .sc2action import SC2Action
from pysc2.lib import features, actions

class SelectAction(SC2Action):
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

    def action(self, obs):
        result = super(SelectAction, self).action(obs)#return no_op()
        if self._iteration == 0:
            units = self.__getUnitsOfType(obs, self._unit_type)
            if self._n_select == 1: result = self.__select_single(units[0])
            elif self._n_select > 1: pass
        return result




