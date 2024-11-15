import g2o
from ..behaviour.monster import AIMonster

class AIZombie(AIMonster):
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 250
        self.target_distance = 800
        self.chase_distance = 800
        self.warn_time = 3000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Zombie')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)