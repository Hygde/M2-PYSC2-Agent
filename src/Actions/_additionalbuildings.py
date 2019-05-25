import numpy as np
from pysc2.lib import units, actions
from .sc2action import SC2Action
from .TrainUnits import TrainUnits
from .select_action import SelectAction, SelectType
from .movecamera import MoveCamera
from .builder import Builder, BFUNCID
from .UseAbility import UseAbility
from .harvest import Harvest

class _AdditionalBuildings(SC2Action):

    def __init__(self, initial_camera_position, top):
        super(_AdditionalBuildings, self).__init__()
        self._initial_camera_position = initial_camera_position
        self._top = top
        self._wall_pos = [28.5, 23.5] if self._top else [30.5, 48.5]
        self._duration = 24
        self._act = TrainUnits(units.Terran.SCV, 1)

    def action(self, obs):
        result = super(_AdditionalBuildings, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:
                if len(obs.observation.build_queue) != 0:self._iteration -= 1
                else:self._act = SelectAction(units.Terran.SCV, SelectType.IDLE_WORKER)
            if self._iteration == 2:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])
            elif self._iteration == 3:self._act = Builder(BFUNCID.SUPPLYDEPOT, [24,30] if self._top else [48, 28], self._NOT_QUEUED)
            elif self._iteration == 4:self._act = Builder(BFUNCID.ENGINEERINGBAY, [23,38] if self._top else [57, 30], self._QUEUED)
            elif self._iteration == 5:self._act = Builder(BFUNCID.SUPPLYDEPOT, [34,40] if self._top else [59, 39], self._QUEUED)
            elif self._iteration == 6:self._act = Builder(BFUNCID.FACTORY, [10,40] if self._top else [57, 20], self._QUEUED)
            elif self._iteration == 7:self._act = Builder(BFUNCID.ARMORY, [15,50] if self._top else [60, 49], self._QUEUED)
            elif self._iteration == 8:self._act = SelectAction(units.Terran.EngineeringBay, SelectType.SINGLE)
            elif self._iteration == 9:self._act = UseAbility(actions.FUNCTIONS.Research_TerranInfantryArmor_quick.id)
            elif self._iteration == 10:self._act = UseAbility(actions.FUNCTIONS.Research_TerranInfantryWeapons_quick.id)
            elif self._iteration == 13:self._act = SelectAction(units.Terran.Barracks, SelectType.SINGLE)
            elif self._iteration == 14:self._act = TrainUnits(units.Terran.Reaper, 5)
            elif self._iteration == 15:self._act = SelectAction(units.Terran.SCV, SelectType.IDLE_WORKER)
            elif self._iteration == 16:self._act = MoveCamera(self._initial_camera_position)
            elif self._iteration == 17:self._act = Harvest(units.Neutral.MineralField)
            elif self._iteration == 18:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])
            elif self._iteration == 19:self._act = SelectAction(units.Terran.Barracks, SelectType.SINGLE)
            elif self._iteration == 20:self._act = TrainUnits(units.Terran.Reaper, 7)
            elif self._iteration == 21:self._act = SelectAction(units.Terran.EngineeringBay, SelectType.SINGLE)
            elif self._iteration == 22:self._act = UseAbility(actions.FUNCTIONS.Research_TerranInfantryArmor_quick.id)
            elif self._iteration == 23:self._act = UseAbility(actions.FUNCTIONS.Research_TerranInfantryWeapons_quick.id)

        if not self._act.isFinished():result = self._act.action(obs)
        return result