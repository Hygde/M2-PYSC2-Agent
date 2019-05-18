import numpy as np
from pysc2.lib import units, actions
from .sc2action import SC2Action
from .select_action import SelectAction, SelectType
from .TrainUnits import TrainCommandCenterUnits
from ._createwall import _CreateWall

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
            elif self._iteration == 2:self._act = _CreateWall(self._initial_camera_position, self._top)
        if not self._act.isFinished():result = self._act.action(obs)
        return result