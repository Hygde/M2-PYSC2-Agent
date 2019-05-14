from pysc2.lib import features, actions, units
import logging, numpy as np
from ._estimator import _Estimator

## Tool class which gathers some utility function
class Observations:
    def __init__(self):
        self._logger = logging.getLogger("ObservationsLogger")

    ## This function get the position current player units and returns the mean of all the position.
    # @param obs is the handler of the current state of the game
    def getPlayerPosition(self, obs):
        #This function should be run when the agent is launched
        player_y, player_x = (obs.observation.feature_minimap.player_relative == features.PlayerRelative.SELF).nonzero()
        player_x, player_y = player_x.mean(), player_y.mean()
        self._logger.debug([player_x, player_y])
        return player_x, player_y

    ## This function returns the position of the camera
    # @param obs is the handler of the current state of the game
    def getCameraPosition(self, obs):
        ycam, xcam = np.array(obs.observation.feature_minimap.camera.nonzero())
        xcam, ycam = xcam.mean(), ycam.mean()
        self._logger.debug([xcam, ycam])
        return xcam, ycam

    ## This function returns the postion of minerals
    # @param obs is the handler of the current state of the game
    def getMineralPosition(self, obs):
        ydata, xdata = np.array(obs.observation.feature_minimap.player_relative == features.PlayerRelative.NEUTRAL).nonzero()
        dataset = np.array([el for el in zip(xdata, ydata)])
        result = _Estimator().getPositionOfMinerals(dataset)
        self._logger.debug(result)
        return result

    ## This function returns True if the starting base is on the top side of the map
    # @param initial_camera_position defines the initial position of the camera
    def isOnTop(self, initial_camera_position):
        result = True if initial_camera_position[1] < 32 else False
        self._logger.debug(result)
        return result
