from pysc2.lib import units
from .sc2action import SC2Action
from .builder import Builder, BFUNCID
from .select_action import SelectAction, SelectType
from Tools import Observations as mobs

## This class builds refinery
class _Vespenes(SC2Action):

    def __init__(self):
        super(_Vespenes, self).__init__()
        self._duration = 2
        self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)

    def action(self, obs):
        result = super(_Vespenes, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:
                self._geyser_position = mobs.getUnitsOfType(obs, units.Neutral.VespeneGeyser)
                self._logger.debug(self._geyser_position)
                self._act = Builder(BFUNCID.REFINERY, self._geyser_position[0])
            elif self._iteration == 2:self._act = Builder(BFUNCID.REFINERY, self._geyser_position[1], True)
        if not self._act.isFinished():result = self._act.action(obs)
        return result


