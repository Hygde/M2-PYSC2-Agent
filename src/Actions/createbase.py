import numpy as np
from pysc2.lib import units, actions
from .sc2action import SC2Action
from .select_action import SelectAction, SelectType
from .TrainUnits import TrainUnits
from ._createwall import _CreateWall
from ._vespenes import _Vespenes
from ._additionalbuildings import _AdditionalBuildings
from .builder import Builder, BFUNCID
from .movecamera import MoveCamera
from .harvest import Harvest
from .UseAbility import UseAbility
from .rallypoint import RallyPoint
from Tools import Observations as mobs

## This class describes the steps to build the base
class CreateBase(SC2Action):
    def __init__(self, initial_camera_position, top):
        super(CreateBase, self).__init__()
        self._top = top
        self._duration = 26
        self._initial_camera_position = initial_camera_position
        self._act = SelectAction(units.Terran.CommandCenter, SelectType.SINGLE)

    ## This function constructs the base
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(CreateBase, self).action(obs)

        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._act = TrainUnits(units.Terran.SCV, 1)
            elif self._iteration == 2:self._act = _CreateWall(self._initial_camera_position, self._top)
            elif self._iteration == 3:self._act = SelectAction(units.Terran.CommandCenter, SelectType.SINGLE)
            elif self._iteration == 4:
                self._geyser_position = mobs.getUnitsOfType(obs, units.Neutral.VespeneGeyser)
                pos = np.array([[unit.x, unit.y] for unit in obs.observation.feature_units if unit.unit_type == units.Terran.CommandCenter])
                pos += (np.array([10,0]) if self._top else np.array([-10,-10]))
                self._act = RallyPoint(units.Terran.CommandCenter, pos[0], queued=False)
            elif self._iteration == 5:self._act = TrainUnits(units.Terran.SCV, 5)
            elif self._iteration == 6:self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE)
            elif self._iteration == 7:self._act = Builder(BFUNCID.REFINERY, self._geyser_position[0], queued=True)
            elif self._iteration == 8:self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE, mobs.getUnitsOfType(obs, units.Terran.SCV)[0])
            elif self._iteration == 9:self._act = Builder(BFUNCID.REFINERY, self._geyser_position[1])
            elif self._iteration == 10:self._act = SelectAction(units.Terran.SCV, SelectType.SINGLE, mobs.getUnitsOfType(obs, units.Terran.SCV)[0])
            elif self._iteration == 11:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])
            elif self._iteration == 12:self._act = Builder(BFUNCID.SUPPLYDEPOT, [24,30] if self._top else [48, 28], self._NOT_QUEUED)
            elif self._iteration == 13:self._act = Builder(BFUNCID.ENGINEERINGBAY, [23,38] if self._top else [57, 30], self._QUEUED)
            elif self._iteration == 14:self._act = Builder(BFUNCID.BARRACKS, [10,40] if self._top else [57, 20], self._QUEUED)
            elif self._iteration == 15:self._act = Builder(BFUNCID.SUPPLYDEPOT, [34,40] if self._top else [59, 39], self._QUEUED)
            elif self._iteration == 16:self._act = MoveCamera(self._initial_camera_position)
            elif self._iteration == 17:self._act = Harvest(units.Neutral.MineralField, queued=True)
            elif self._iteration == 18:self._act = _Vespenes(self._geyser_position)
            elif self._iteration == 19:self._act = SelectAction(units.Terran.SCV, SelectType.IDLE_WORKER)
            elif self._iteration == 20:self._act = Harvest(units.Neutral.MineralField)
            elif self._iteration == 21:self._act = SelectAction(units.Terran.CommandCenter, SelectType.SINGLE)
            elif self._iteration == 22:self._act = TrainUnits(units.Terran.SCV, 1)
            elif self._iteration == 23:self._act = UseAbility(actions.FUNCTIONS.Morph_OrbitalCommand_quick.id)
            elif self._iteration == 24:self._act = SelectAction(units.Terran.SCV, SelectType.IDLE_WORKER)
            elif self._iteration == 25:self._act = MoveCamera([28.5, 23.5] if self._top else [30.5, 48.5])

        if not self._act.isFinished():result = self._act.action(obs)
        return result