import numpy as np
from pysc2.lib import units
from .sc2action import SC2Action
from .builder import Builder, BFUNCID
from .select_action import SelectAction, SelectType
from .TrainUnits import TrainUnits
from .rallypoint import RallyPoint
from Tools import Observations as mobs

## This class builds refinery and SCVs to extract vespene
class _Vespenes(SC2Action):

    ## Constructor of the class
    def __init__(self, top):
        super(_Vespenes, self).__init__()
        self._duration = 12
        self._top = top
        self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)

    ## This function checks if the building of selected rafinery is completed
    # @param obs is the handler of the current state of the game
    def _refineryReady(self, obs):
        if obs.observation.single_select[0][-1] != 0:self._iteration -=1
        else:self._act = SelectAction(units.Terran.CommandCenter, SelectType.SINGLE)

    ## This function defines the way to create rafineries and the way to exploit it
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(_Vespenes, self).action(obs)
        self._logger.warning(self._iteration)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:
                self._geyser_position = mobs.getUnitsOfType(obs, units.Neutral.VespeneGeyser)
                self._act = Builder(BFUNCID.REFINERY, self._geyser_position[0])
            elif self._iteration == 2:self._act = Builder(BFUNCID.REFINERY, self._geyser_position[1], True)
            elif self._iteration == 3:self._act = SelectAction(units.Terran.Refinery, SelectType.SINGLE)
            elif self._iteration == 4:self._refineryReady(obs)
            elif self._iteration == 5:self._act = RallyPoint(units.Terran.CommandCenter, self._geyser_position[0])
            elif self._iteration == 6:self._act = TrainUnits(units.Terran.SCV, 3)
            elif self._iteration == 7:
                if len(mobs.getUnitsOfType(obs, units.Terran.Refinery)) != 2:self._iteration -= 1
                else:self._act = SelectAction(units.Terran.Refinery,SelectType.SINGLE, coord_xy=self._geyser_position[1])
            elif self._iteration == 8:self._refineryReady(obs)
            elif self._iteration == 9:
                if len(obs.observation.build_queue) != 0:self._iteration -= 1
                else:self._act = RallyPoint(units.Terran.CommandCenter, self._geyser_position[1])
            elif self._iteration == 10:self._act = TrainUnits(units.Terran.SCV, 2)
            else:
                if len(obs.observation.build_queue) != 0:self._iteration -= 1
                else:
                    pos = np.array([[unit.x, unit.y] for unit in obs.observation.feature_units if unit.unit_type == units.Terran.CommandCenter]) + (np.array([10,0]) if self._top else np.array([-10,-10]))
                    self._act = RallyPoint(units.Terran.CommandCenter, pos[0], queued=False)
        if not self._act.isFinished():result = self._act.action(obs)
        return result