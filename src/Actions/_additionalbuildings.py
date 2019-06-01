import numpy as np
from pysc2.lib import units, actions
from .sc2action import SC2Action
from .TrainUnits import TrainUnits
from .select_action import SelectAction, SelectType
from .movecamera import MoveCamera
from .builder import Builder, BFUNCID
from .UseAbility import UseAbility
from .harvest import Harvest
from .rallypoint import RallyPoint

class _AdditionalBuildings(SC2Action):

    def __init__(self, initial_camera_position, top):
        super(_AdditionalBuildings, self).__init__()
        self._initial_camera_position = initial_camera_position
        self._top = top
        self._duration = 16
        self._act = SelectAction(units.Terran.EngineeringBay, SelectType.SINGLE)

    def _barracksReady(self, obs):
        if(obs.observation.multi_select[:,-1] == 0).sum() != 2:self._iteration -=  1
        else:self._act = RallyPoint(units.Terran.Barracks, ([52,48] if self._top else [28,20]))

    def action(self, obs):
        result = super(_AdditionalBuildings, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._act = UseAbility(actions.FUNCTIONS.Research_TerranInfantryArmor_quick.id)
            elif self._iteration == 2:self._act = UseAbility(actions.FUNCTIONS.Research_TerranInfantryWeapons_quick.id)
            elif self._iteration == 3:self._act = SelectAction(units.Terran.SCV, SelectType.IDLE_WORKER)
            elif self._iteration == 4:self._act = Builder(BFUNCID.MISSILETURRET, [36,46] if self._top else [46,37])
            elif self._iteration == 5:self._act = Builder(BFUNCID.MISSILETURRET, [35,34] if self._top else [42,21], queued=True)
            elif self._iteration == 6:self._act = Builder(BFUNCID.FACTORY, [34,21] if self._top else [48, 48], queued=True)
            elif self._iteration == 7:self._act = SelectAction(units.Terran.Barracks, SelectType.ALL_TYPE)
            elif self._iteration == 8:self._barracksReady(obs)
            elif self._iteration == 9:self._act = TrainUnits(units.Terran.Marine, 3)
            elif self._iteration == 10:self._act = TrainUnits(units.Terran.Reaper, 7)
            elif self._iteration == 11:self._act = SelectAction(units.Terran.SCV, SelectType.IDLE_WORKER)
            elif self._iteration == 12:self._act = Builder(BFUNCID.ARMORY, [15,50] if self._top else [60, 49], queued=True)
            elif self._iteration == 13:self._act = MoveCamera(self._initial_camera_position)
            elif self._iteration == 14:self._act = Harvest(units.Neutral.MineralField, queued=True)
            elif self._iteration == 15:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])
        if not self._act.isFinished():result = self._act.action(obs)
        return result