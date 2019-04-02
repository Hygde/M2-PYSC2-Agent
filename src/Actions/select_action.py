from .sc2action import SC2Action
from pysc2.lib import features, actions

class SelectAction(SC2Action):
    def __init__(self, unit_type, n):
        super(SelectAction, self).__init__()
        self._duration = 2
        self._unit_type = unit_type

    def __getUnitsOfType(self, obs, unit_type):
        return [unit for unit in obs.observation.feature_units if unit.unit_type == unit_type]

    def __select_single(self, units, coord_xy):
        return actions.FUNCTIONS.select_point("select", coord_xy)


    def action(self, obs):
        super(SelectAction, self).action(obs)
        if self._iteration == 0:
            units = self.__getUnitsOfType(obs, self._unit_type)



