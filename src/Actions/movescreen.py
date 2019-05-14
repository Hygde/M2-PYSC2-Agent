from .sc2action import SC2Action
from pysc2.lib import actions

## This class defines a simple way to move units
class MoveScreen(SC2Action):

    ## Constructor of the class
    # @param moveto_xy is an array like which contains [x, y]
    def __init__(self, moveto_xy):
        super(MoveScreen, self).__init__()
        self._moveto_xy = moveto_xy

    ## This function moves the selected units to coordinates
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(MoveScreen, self).action(obs)
        if (self._iteration == 0) and (actions.FUNCTIONS.Move_screen.id in obs.observation.available_actions):
            print((actions.FUNCTIONS.Move_screen.id in obs.observation.available_actions))
            result = actions.FUNCTIONS.Move_screen(self._QUEUED, self._moveto_xy)
            self._iteration += 1
            input("movescreen")
        return result
