from Actions import SC2Action
from enum import IntEnum
from pysc2.lib import actions

## This class is an enumeration which defines supply depot abilities
class SupplyDepotAbility(IntEnum):
    LOWER = actions.FUNCTIONS.Morph_SupplyDepot_Lower_quick.id
    RAISE = actions.FUNCTIONS.Morph_SupplyDepot_Raise_quick.id

## This class defines the way to use an ability
class UseAbility(SC2Action):
    ## Constructor of the class
    # @param ability is the ability to use
    def __init__(self, ability):
        super(UseAbility,self).__init__()
        self._ability = ability

    ## This function defines the way to use ability
    # @param obs is the handler of the current state of the game
    def action(self, obs):
        result = super(UseAbility, self).action(obs)
        if self._ability in obs.observation.available_actions:
            result = actions.FunctionCall(self._ability, [self._NOT_QUEUED])
            self._iteration += 1
        return result