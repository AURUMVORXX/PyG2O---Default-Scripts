
import g2o
from ..behaviour.humanoid import AIHumanoid

class AIHumanBanditMelee(AIHumanoid):
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 200
        self.target_distance = 1000
        self.chase_distance = 500
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Bandit')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIHumanBanditRanged(AIHumanoid):
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 950
        self.target_distance = 1000
        self.chase_distance = 500
        self.weapon_mode = g2o.WEAPONMODE_BOW
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Bandit')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)