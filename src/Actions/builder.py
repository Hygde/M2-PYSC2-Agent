from .sc2action import SC2Action
from pysc2.lib import features, actions
from enum import IntEnum

## enum of building function
class BFUNCID(IntEnum):
    SUPPLYDEPOT = actions.FUNCTIONS.Build_SupplyDepot_screen.id
    REFINERY = actions.FUNCTIONS.Build_Refinery_screen.id
    BARRACKS = actions.FUNCTIONS.Build_Barracks_screen.id
    ENGINEERINGBAY = actions.FUNCTIONS.Build_EngineeringBay_screen.id
    MISSILETURRET = actions.FUNCTIONS.Build_MissileTurret_screen.id
    BUNKER = actions.FUNCTIONS.Build_Bunker_screen.id

## Defines the way to build a batiment
class Builder(SC2Action):
    def __init__(self, to_build, coord_xy, queued=False):
        super(Builder, self).__init__()
        self._duration = 1
        self._to_build = to_build
        self._queued = self._QUEUED if queued else self._NOT_QUEUED
        self._coord_xy = coord_xy

    ## This function builds a batiment
    # @param obs is the current state of the game
    def action(self, obs):
        result = super(Builder, self).action(obs)
        if self._iteration == 0 and self._to_build in obs.observation.available_actions:
            result = actions.FunctionCall(self._to_build, [self._queued, self._coord_xy])
            self._iteration += 1
        return result