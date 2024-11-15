import g2o
from ..behaviour.monster import AIMonster

class AIWaran(AIMonster):
    
    instance = 'WARAN'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 350
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 5000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Waran')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIFireWaran(AIMonster):
    
    instance = 'FIREWARAN'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 350
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 5000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Fire Waran')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)