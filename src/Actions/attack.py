from pysc2.lib import actions, features
from  pysc2.lib.units import Terran, Zerg, Protoss, Neutral
from .sc2action import SC2Action
from .select_action import SelectAction, SelectType
from .TrainUnits import TrainUnits
from .movecamera import MoveCamera
from .movescreen import MoveScreen
from Tools import Observations as mobs

import numpy as np

class Attack(SC2Action):

    def __init__(self, top, initial_camera_position):
        super(Attack, self).__init__()
        self._duration = 10
        self._top = top
        self._mobs = mobs()
        self._enemy_race = -1
        self._attack_coordinates = [39.5, 47] if self._top else [22, 25]
        self._initial_camera_position = initial_camera_position
        self._act = SelectAction(Terran.Barracks, SelectType.ALL_TYPE)

    def _getBarycenter(self, obs):
        result = np.array([[unit.x, unit.y] for unit in obs.observation.feature_units if unit.is_selected]).mean(axis=0)
        self._logger.debug(result)
        return result

    def _zergsOrder(self, enemies):
        self._logger.debug("zerg")
        result = np.array([[e[1], e[2]] for e in enemies if (e[0] == Zerg.SpineCrawler.value) or e[0] > Zerg.Drone.value
         and e[0] != Zerg.Overlord.value and e[0] != Zerg.Overseer.value and e[0] != Zerg.Larva.value])
        if result.size == 0:result = np.array([[e[1], e[2]] for e in enemies if e[0] == Zerg.Drone.value])
        if result.size == 0:result = np.array([[e[1], e[2]] for e in enemies if e[0] < Zerg.Drone.value])
        return result

    def _protossOrder(self, enemies):
        self._logger.debug("protoss")
        result = np.array([[e[1], e[2]] for e in enemies if (e[0] >= Protoss.Zealot.value and not e[0] == Protoss.Probe.value) or e[0] == Protoss.PhotonCannon.value])
        if result.size == 0:result = np.array([[e[1], e[2]] for e in enemies if e[0] == Protoss.Probe.value])
        if result.size == 0:result = np.array([[e[1], e[2]] for e in enemies if e[0] < Protoss.Zealot.value])
        return result

    def _terranOrder(self, enemies):
        self._logger.debug("terran")
        result = np.array([[e[1], e[2]] for e in enemies 
            if (e[0] >= Terran.SCV.value and e[0] != Terran.OrbitalCommand.value and e[0] != Terran.Medivac.value)
             or (e[0] == Terran.Bunker.value) or (Terran.AutoTurret.value <= e[0] <= Terran.SiegeTank.value)])
        if result.size == 0:np.array([[e[1], e[2]] for e in enemies if e[0] == Terran.SCV.value])
        if result.size == 0:np.array([[e[1], e[2]] for e in enemies if e[0] < Terran.SCV.value])
        return result

    def _cap(self, value):
        result = value
        if value > 64:result = 64
        if value < 0:result = 0
        return result

    def _getEnemyPosition(self, obs):
        neutre = np.array([v.value for v in Neutral])
        #enemies = [[u.unit_type, u.x, u.y] for u in obs.observation.feature_units if (not u.is_selected) and (not u.unit_type in neutre) and (0 < u.x < 65) and (0 < u.y < 65)]
        enemies = [[u.unit_type, self._cap(u.x), self._cap(u.y)] for u in obs.observation.feature_units if (not u.is_selected) and (not u.unit_type in neutre) and (0 < u.x < 65) and (0 < u.y < 65)]
        if self._enemy_race == 0:target = self._terranOrder(enemies)
        elif self._enemy_race == 1:target = self._zergsOrder(enemies)
        elif self._enemy_race == 2:target = self._protossOrder(enemies)
        else: target = enemies
        return target

    def _getDistance(self, army_position, enemies):
        self._logger.debug(army_position)
        self._logger.info(enemies)
        arr = np.array([np.power(army_position[0] - enemy[0], 2) + np.power(army_position[1] - enemy[1], 2) for enemy in enemies])
        result = np.sqrt(arr)
        self._logger.debug(result)
        return result

    def __attack(self, obs):
        #input("attack")
        result = actions.FUNCTIONS.no_op()
        try:
            army_count = obs.observation.multi_select
            army = self._getBarycenter(obs)
            enemies = self._getEnemyPosition(obs)
            if army_count.size > 0 and enemies.size > 0:
                distances = self._getDistance(army, enemies)
                print(distances)
                index = distances.tolist().index(min(distances))
                result = actions.FUNCTIONS.Attack_screen("now", enemies[index])
                self._iteration -= 1
        except:self._iteration -= 1
        return result

    def _waitArmy(self, obs):
        y ,_ = (obs.observation.feature_screen.selected == True).nonzero()
        self._enemy_race = self._mobs.getEnemyRace(obs)
        if (len(y) == 0) or (self._enemy_race < 0):self._iteration -= 1
        #else:input("self._enemy_race ="+str(self._enemy_race))

    def _minimapAttack(self, obs):
        result = actions.FUNCTIONS.no_op()
        if len(obs.observation.multi_select) > 0 or len(obs.observation.single_select) > 0:
            y, x = (obs.observation.feature_minimap.player_relative == 4).nonzero()
            if y.size and actions.FUNCTIONS.Attack_minimap.id in obs.observation.available_actions:
                result = actions.FUNCTIONS.Attack_minimap("now", [x[0], y[0]])
                self._iteration -= 1
        return result

    def action(self,obs):
        result = super(Attack, self).action(obs)
        if self._act.isFinished():
            self._iteration += 1
            if self._iteration == 1:self._act = TrainUnits(Terran.Reaper, 10)
            elif self._iteration == 2:self._act = SelectAction(Terran.Reaper, SelectType.ALL_TYPE)
            elif self._iteration == 3:self._act = MoveCamera(self._attack_coordinates)
            elif self._iteration == 4:self._act = MoveScreen([32,32])
            elif self._iteration == 6:self._waitArmy(obs)
            elif self._iteration == 7:result = self.__attack(obs)
            elif self._iteration == 8:result = self._minimapAttack(obs)
            elif self._iteration == 9:self._act = MoveCamera(self._initial_camera_position)
        if not self._act.isFinished():result = self._act.action(obs)

        return result
