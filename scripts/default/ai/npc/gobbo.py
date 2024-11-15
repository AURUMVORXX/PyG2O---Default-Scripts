import g2o
from ..behaviour.monster import AIMonster

class AIYoungGobboGreen(AIMonster):
    
    instance = 'YGOBBO_GREEN'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 600
        self.warn_time = 3000
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Young Gobbo Green')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIGobboGreen(AIMonster):
    
    instance = 'GOBBO_GREEN'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 600
        self.warn_time = 3000
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Gobbo Green')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIGobboBlack(AIMonster):
    
    instance = 'GOBBO_BLACK'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 600
        self.warn_time = 3000
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Gobbo Black')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIGobboWarrior(AIMonster):
    
    instance = 'GOBBO_WARRIOR'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 600
        self.warn_time = 3000
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Gobbo Warrior')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIGobboSkeleton(AIMonster):
    
    instance = 'GOBBO_SKELETON'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 300
        self.target_distance = 1200
        self.chase_distance = 600
        self.warn_time = 3000
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Gobbo Skeleton')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)