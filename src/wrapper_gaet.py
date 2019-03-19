import logging
from pysc2.lib import actions, features
from src.UnitType.terran_units import TerranUnits

class Sc2Tools:
    def __init__(self):
        def __init__(self, obs):
            self._logger = logging.getLogger("Sc2ToolsLogger")
            self._obs = obs

        def _getUnitByType(self, unitType):
            return [unit for unit in self._obs.observation.feature_units if unit.unit_type == unitType]

        def select(self, unit_type, amount=None, target=None):
            result = actions.FUNCTIONS.no_op()
            unit = self._getUnitByType(unit_type)
            if len(unit) > 0:
                if not (amount == None) and (amount > 0): unit = unit[:amount]  # keep the amount
            elif not (target == None):
                if len(target) == 2:
                    result = actions.FUNCTIONS.select()
                else:
                    pass


        def movescreen