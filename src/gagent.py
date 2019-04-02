import logging, numpy as np
from pysc2.agents.base_agent import BaseAgent
from absl import app
from pysc2.env import sc2_env
from pysc2.lib import actions, features, units

try:
    from UnitType import TerranUnits
except ImportError as imp:
    try:
        from src.UnitType import TerranUnits
    except ImportError as imp:
        print(repr(imp))
        import sys
        sys.exit(1)
# List of known unit types. It is taken from:
# https://github.com/Blizzard/s2client-api/blob/master/include/sc2api/sc2_typeenums.h

# How to run:
# python -m pysc2.bin.agent --agent agent.GAgent --map Simple64 --agent_race terran --use_feature_units True

## This is a protoss agent
class GAgent(BaseAgent):

    ## Constructor
    def __init__(self):
        super(GAgent, self).__init__()
        # self.__initLogger()

    """PRIVATE"""

    # This functions returns True if the action is available
    # @param action is the action to test
    # @param obs is all the observation of the current state of the game
    # def __validAction(self, action, obs):
    #     return action in obs.observation.available_actions
    #
    # # This function initializes the root logger and creates _logger attribute
    # def __initLogger(self):
    #     self._logger = logging.getLogger()
    #     self._logger.setLevel(logging.DEBUG)
    #     formatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
    #     ch = logging.StreamHandler()
    #     ch.setLevel(logging.DEBUG)
    #     ch.setFormatter(formatter)
    #     self._logger.handlers[0] = ch
    #
    # """PROTECTED"""

    """PUBLIC"""

    ## This function is called at each step of the game
    # @param obs is all the available observation of the current state of the game
    def step(self, obs):
        super(GAgent, self).step(obs)
        #print(repr(obs.observation))
        #np.set_printoptions(threshold=np.nan)
        # self._logger.debug(self.steps)
        #print(len([unit for unit in obs.observation.feature_units if unit.unit_type == TerranUnits.SCV.value]))
        return actions.FUNCTIONS.no_op()

    ## This function is called to reset the episode
    def reset(self):
        super(GAgent, self).reset()