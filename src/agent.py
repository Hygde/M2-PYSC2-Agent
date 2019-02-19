import logging
from pysc2.agents.base_agent import BaseAgent
from pysc2.lib import actions, features

# List of known unit types. It is taken from:
# https://github.com/Blizzard/s2client-api/blob/master/include/sc2api/sc2_typeenums.h

# How to run:
# python -m pysc2.bin.agent --agent agent.Agent --map Simple64 --agent_race protoss --use_feature_units True

## This is a protoss agent
class Agent(BaseAgent):

    ## Constructor
    def __init__(self):
        super(Agent, self).__init__()
        self.__initLogger()

    """PRIVATE"""

    # This function initializes the root logger and creates _logger attribute
    def __initLogger(self):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(module)s :: %(funcName)s :: %(message)s")
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

    """PROTECTED"""

    """PUBLIC"""

    ## This function is called at each step of the game
    # @param obs is all the available observation of the current state of the game
    def step(self, obs):
        super(Agent, self).step(obs)
        return actions.FUNCTIONS.no_op()