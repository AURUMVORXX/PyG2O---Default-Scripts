import g2o
from ..behaviour.monster import AIMonster

class AIMinecrawler(AIMonster):
    
    instance = 'MINECRAWLER'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 400
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 4000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Minecrawler')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIMinecrawlerWarrior(AIMonster):
    
    instance = 'MINECRAWLERWARRIOR'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 400
        self.target_distance = 1200
        self.chase_distance = 1000
        self.warn_time = 4000
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Minecrawler Warrior')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)