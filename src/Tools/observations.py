from pysc2.lib import features, actions
import logging

class Observations:
    def __init__(self):
        self._logger = logging.getLogger("ObservationsLogger")

    ## This function get the position current player units and returns the mean of all the position.
    # @param obs is the handler of the current state of the game
    def getPlayerPosition(self, obs):
        #This function should be run when the agent is launched
        player_y, player_x = (obs.observation.feature_minimap.player_relative == features.PlayerRelative.SELF).nonzero()
        return player_x.mean(), player_y.mean()