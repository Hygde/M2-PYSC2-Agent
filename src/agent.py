import logging, numpy as np, sys
from pysc2.agents.base_agent import BaseAgent
from pysc2.lib import actions, features, units
from Actions import CreateBase, Attack
from Tools import Observations

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
        self._mobs = Observations()
        np.set_printoptions(threshold=sys.maxsize)

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

    ## This function initializes the agent
    # @param obs is the handler of the current state of the game
    def __initAgent(self, obs):
        self._logger.info("initializing the agent")
        self._initial_camera_position = self._mobs.getCameraPosition(obs)
        self._onTop = self._mobs.isOnTop(self._initial_camera_position)
        self._act = CreateBase(self._initial_camera_position, self._onTop)

    """PROTECTED"""

    """PUBLIC"""

    ## This function is called at each step of the game
    # @param obs is all the available observation of the current state of the game
    def step(self, obs):
        super(Agent, self).step(obs)
        result = actions.FUNCTIONS.no_op()
        self._logger.debug(obs.observation.available_actions)

        if self.steps == 1:self.__initAgent(obs)
        elif self._act.isFinished():self._act = Attack(self._onTop, [28.5, 23.5] if self._onTop else [30.5, 48.5])

        if not self._act.isFinished():result = self._act.action(obs)

        return result

    ## This function is called to reset the episode
    def reset(self):
        super(Agent, self).reset()
        self.steps = 0