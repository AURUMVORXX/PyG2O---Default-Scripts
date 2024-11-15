import g2o
from ..behaviour.monster import AIMonster

class AIYoungWolf(AIMonster):
    
    instance = 'YWOLF'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 3000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Young Wolf')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIWolf(AIMonster):
    
    instance = 'WOLF'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 3000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Wolf')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        g2o.setPlayerStrength(self.id, 30)