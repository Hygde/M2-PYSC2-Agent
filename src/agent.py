import logging, numpy as np
from pysc2.agents.base_agent import BaseAgent
from pysc2.lib import actions, features, units
from Actions import SelectAction

# List of known unit types. It is taken from:
# https://github.com/Blizzard/s2client-api/blob/master/include/sc2api/sc2_typeenums.h

# How to run:
# python -m pysc2.bin.agent --agent agent.Agent --map Simple64 --agent_race terran --use_feature_units True

## This agent inherits of PySC2's BaseAgent class
class Agent(BaseAgent):

    ## Constructor
    def __init__(self):
        super(Agent, self).__init__()
        self.__initLogger()
        np.set_printoptions(threshold=np.nan)

    """PRIVATE"""

    # This functions returns True if the action is available
    # @param action is the action to test
    # @param obs is all the observation of the current state of the game
    def __validAction(self, action, obs):
        return action in obs.observation.available_actions

    # This function initializes the root logger and creates _logger attribute
    def __initLogger(self):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self._logger.handlers[0] = ch

    """PROTECTED"""

    """PUBLIC"""        

    ## This function is called at each step of the game
    # @param obs is all the available observation of the current state of the game
    def step(self, obs):
        super(Agent, self).step(obs)
        result = actions.FUNCTIONS.no_op()
        self._logger.debug(self.steps)
        if self.steps == 1:
            act = SelectAction(units.Terran.SCV, 1)
            result = act.action(obs)
        
        self._logger.debug(obs.observation['single_select'])
        self._logger.debug(obs.observation['multi_select'])
        input()
        return result

    ## This function is called to reset the episode
    def reset(self):
        super(Agent, self).reset()