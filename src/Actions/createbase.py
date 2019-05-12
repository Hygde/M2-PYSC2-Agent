import numpy as np
from pysc2.lib import units, actions
from .sc2action import SC2Action
from .builder import Builder, BFUNCID
from .select_action import SelectAction, SelectType
from .traincommandcenterunits import TrainCommandCenterUnits

class CreateBase(SC2Action):
    def __init__(self, initial_camera_position, top):
        super(CreateBase, self).__init__()
        self._top = top
        self._duration = 7
        self._initial_camera_position = initial_camera_position
        self._act = TrainCommandCenterUnits(1)

    def _moveCamera(self, coord_xy=None):
        if coord_xy == None:
            result = actions.FUNCTIONS.move_camera([28.5, 23.5])
            if not self._top:result = actions.FUNCTIONS.move_camera([33.5, 48.5])
        else:result = actions.FUNCTIONS.move_camera(coord_xy)
        return result

    def action(self, obs):
        result = super(CreateBase, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)
            elif self._iteration == 2:result = self._moveCamera()
            elif self._iteration == 3:self._act = Builder(BFUNCID.SUPPLYDEPOT, [44,30] if self._top else [12, 28], self._NOT_QUEUED)
            elif self._iteration == 4:self._act = Builder(BFUNCID.BARRACKS, [43,38] if self._top else [21, 30], self._QUEUED)
            elif self._iteration == 5:self._act = Builder(BFUNCID.SUPPLYDEPOT, [54,40] if self._top else [22, 38], self._QUEUED)
            elif self._iteration == 6:result = self._moveCamera(self._initial_camera_position)
            else:pass
            """minerals =  np.array([[unit.x, unit.y] for unit in obs.observation.feature_units if unit.unit_type == units.Neutral.MineralField])
            print(minerals)
            result = actions.FunctionCall("Move_screen", [self._QUEUED, minerals[0]])"""
        if not self._act.isFinished():result = self._act.action(obs)
        #input(self._iteration)
        return result