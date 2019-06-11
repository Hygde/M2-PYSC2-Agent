from .sc2action import SC2Action
from pysc2.lib import actions

## This class moves the camera to a position
class MoveCamera(SC2Action):
    def __init__(self, coord_xy):
        super(MoveCamera, self).__init__()
        self._coord_xy = coord_xy
        self._duration = 2

    ## This function move the camera to self._coord_xy
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(MoveCamera, self).action(obs)
        if self._iteration == 0 and actions.FUNCTIONS.move_camera.id in obs.observation.available_actions:
            print("I FUCKING MOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOVED")
            result = actions.FUNCTIONS.move_camera(self._coord_xy)
            self._iteration += 1
        elif self._iteration > 0:
            self._iteration += 1
        return result