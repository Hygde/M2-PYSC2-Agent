import numpy as np
from pysc2.lib import units, actions
from .sc2action import SC2Action
from .builder import Builder, BFUNCID
from .select_action import SelectAction, SelectType
from .movecamera import MoveCamera
from .movescreen import MoveScreen
from .traincommandcenterunits import TrainCommandCenterUnits
from .trainbarracksunits import TrainBarracksUnits 
from .harvest import Harvest

## This class describes the steps to build the base
class CreateBase(SC2Action):
    def __init__(self, initial_camera_position, top):
        super(CreateBase, self).__init__()
        self._top = top
        self._duration = 11
        self._initial_camera_position = initial_camera_position
        self._act = SelectAction(units.Terran.CommandCenter, SelectType.SINGLE)

    ## This function constructs the base
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(CreateBase, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._act = TrainCommandCenterUnits(1)
            elif self._iteration == 2:self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)
            elif self._iteration == 3:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])
            elif self._iteration == 4:self._act = Builder(BFUNCID.SUPPLYDEPOT, [44,30] if self._top else [28, 28], self._NOT_QUEUED)
            elif self._iteration == 5:self._act = Builder(BFUNCID.BARRACKS, [43,38] if self._top else [37, 30], self._QUEUED)
            elif self._iteration == 6:self._act = Builder(BFUNCID.SUPPLYDEPOT, [54,40] if self._top else [39, 39], self._QUEUED)
            elif self._iteration == 7:self._act = SelectAction(units.Terran.Barracks, SelectType.SINGLE)
            elif self._iteration == 8:self._act = TrainBarracksUnits(units.Terran.Marine, 5)
            elif self._iteration == 9:self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)
            elif self._iteration == 10:result = self._act = MoveCamera(self._initial_camera_position)
            else:self._act = Harvest(queued=True)
        if not self._act.isFinished():result = self._act.action(obs)
        return result