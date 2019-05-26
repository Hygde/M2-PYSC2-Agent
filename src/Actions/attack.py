from pysc2.lib import actions, units
from .sc2action import SC2Action
from .select_action import SelectAction, SelectType
from .TrainUnits import TrainUnits
from .movecamera import MoveCamera
from .movescreen import MoveScreen

class Attack(SC2Action):

    def __init__(self, top, initial_camera_position):
        super(Attack, self).__init__()
        self._duration = 6
        self._top = top
        self._attack_coordinates = [39.5, 45.5] if self._top else [20, 25]
        self._initial_camera_position = initial_camera_position
        self._act = SelectAction(units.Terran.Barracks, SelectType.SINGLE)

    def action(self,obs):
        result = super(Attack, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._act = TrainUnits(units.Terran.Reaper, 5)
            elif self._iteration == 2:self._act = SelectAction(units.Terran.Reaper, SelectType.ALL_TYPE)
            elif self._iteration == 3:self._act = MoveCamera(self._attack_coordinates)
            elif self._iteration == 4:self._act = MoveScreen([32,32])
            elif self._iteration == 5:self.act = MoveCamera(self._initial_camera_position)
        if not self._act.isFinished():result = self._act.action(obs)

        return result
