import g2o
from ..behaviour.monster import AIMonster

class AIYoungGiantRat(AIMonster):
    
    instance = 'YGIANT_RAT'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 3000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Young Giant Rat')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        

class AIGiantRat(AIMonster):
    
    instance = 'GIANT_RAT'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 3000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Giant Rat')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)