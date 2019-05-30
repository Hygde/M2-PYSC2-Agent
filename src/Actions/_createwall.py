from pysc2.lib import units, actions
from .sc2action import SC2Action
from .builder import Builder, BFUNCID
from .select_action import SelectAction, SelectType
from .movecamera import MoveCamera
from .movescreen import MoveScreen
from .TrainUnits import TrainUnits
from .harvest import Harvest
from .UseAbility import UseAbility, SupplyDepotAbility
from .rallypoint import RallyPoint

## This class describes the steps to build the base
class _CreateWall(SC2Action):
    def __init__(self, initial_camera_position, top):
        super(_CreateWall, self).__init__()
        self._top = top
        self._duration = 19
        self._initial_camera_position = initial_camera_position
        self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)

    ## This function constructs the base
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(_CreateWall, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])
            elif self._iteration == 2:self._act = Builder(BFUNCID.SUPPLYDEPOT, [44,30] if self._top else [28, 28], self._NOT_QUEUED)
            elif self._iteration == 3:self._act = Builder(BFUNCID.BARRACKS, [43,38] if self._top else [37, 30], self._QUEUED)
            elif self._iteration == 4:self._act = Builder(BFUNCID.SUPPLYDEPOT, [54,40] if self._top else [39, 39], self._QUEUED)
            elif self._iteration == 5:self._act = SelectAction(units.Terran.Barracks, SelectType.SINGLE)
            elif self._iteration == 6:self._act = RallyPoint(units.Terran.Barracks, ([54,42] if self._top else [28,20]), queued=True)
            elif self._iteration == 7:self._act = TrainUnits(units.Terran.Marine, 5)
            elif self._iteration == 8:self._act = SelectAction(units.Terran.SupplyDepot, SelectType.SINGLE, coord_xy=[44,30] if self._top else [28, 28])
            elif self._iteration == 9:self._act = UseAbility(SupplyDepotAbility.LOWER)
            elif self._iteration == 10:self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)
            elif self._iteration == 11:result = self._act = MoveCamera(self._initial_camera_position)
            elif self._iteration == 12:self._act = Harvest(units.Neutral.MineralField, queued=True)
            elif self._iteration == 13:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])
            elif self._iteration == 14:self._act = SelectAction(units.Terran.SupplyDepot, SelectType.SINGLE, coord_xy=[44,30] if self._top else [28, 28])
            elif self._iteration == 15:
                if len([[unit.x, unit.y] for unit in obs.observation.feature_units if unit.unit_type == units.Terran.SCV]) == 0:self._act = UseAbility(SupplyDepotAbility.RAISE)
                else: self._iteration -= 1
            elif self._iteration == 16:self._act = SelectAction(units.Terran.Barracks, SelectType.SINGLE)
            elif self._iteration == 17:self._act = TrainUnits(units.Terran.Marine, 2)
            else:self._act = MoveCamera(self._initial_camera_position)
        if not self._act.isFinished():result = self._act.action(obs)
        return result