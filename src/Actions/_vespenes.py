import numpy as np
from pysc2.lib import units
from .sc2action import SC2Action
from .select_action import SelectAction, SelectType
from .harvest import Harvest
from Tools import Observations as mobs

## This class builds refinery and SCVs to extract vespene
class _Vespenes(SC2Action):

    ## Constructor of the class
    def __init__(self, geyser_position):
        super(_Vespenes, self).__init__()
        self._duration = 10
        self._geyser_position = geyser_position
        self._act = SelectAction(None, SelectType.SINGLE, self._geyser_position[0])

    ## This function checks if the building of selected rafinery is completed
    # @param obs is the handler of the current state of the game
    def _refineryReady(self, obs):
        if obs.observation.single_select[0][-1] != 0:self._iteration -=1
        else:self._act = SelectAction(None, SelectType.IDLE_WORKER)

    ## This function defines the way to create rafineries and the way to exploit it
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(_Vespenes, self).action(obs)
        self._logger.warning(self._iteration)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._refineryReady(obs)
            elif self._iteration == 2:self._act = Harvest(None, self._geyser_position[0])
            elif self._iteration == 3:self._act = SelectAction(None, SelectType.IDLE_WORKER)
            elif self._iteration == 4:self._act = Harvest(None, self._geyser_position[0])
            elif self._iteration == 5:self._act = SelectAction(None, SelectType.SINGLE, self._geyser_position[1])
            elif self._iteration == 6:self._refineryReady(obs)
            elif self._iteration == 7:self._act = Harvest(None, self._geyser_position[1])
            elif self._iteration == 8:self._act = SelectAction(None, SelectType.IDLE_WORKER)
            elif self._iteration == 9:self._act = Harvest(None, self._geyser_position[1])
        if not self._act.isFinished():result = self._act.action(obs)
        return result