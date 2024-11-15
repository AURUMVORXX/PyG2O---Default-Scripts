import g2o
from ..behaviour.humanoid import AIHumanoid

class AISkeleton(AIHumanoid):
    
    instance = 'SKELETON'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 250
        self.target_distance = 1200
        self.chase_distance = 1000
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Skeleton')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AISkeletonMage(AIHumanoid):
    
    instance = 'SKELETONMAGE'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 1000
        self.target_distance = 1000
        self.chase_distance = 1000
        self.weapon_mode = g2o.WEAPONMODE_MAG
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Skeleton Mage')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        g2o.setPlayerMaxMana(self.id, 1000)
        g2o.setPlayerMana(self.id, 1000)
        g2o.setPlayerTalent(self.id, g2o.TALENT_MAGE, 6)
        g2o.equipItem(self.id, 'ITSC_ICECUBE', 0)
        
class AILesserSkeleton(AIHumanoid):
    
    instance = 'LESSER_SKELETON'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 250
        self.target_distance = 1200
        self.chase_distance = 1000
        self.weapon_mode = g2o.WEAPONMODE_1HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Lesser Skeleton')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AISkeletonLord(AIHumanoid):
    
    instance = 'SKELETON_LORD'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 250
        self.target_distance = 1200
        self.chase_distance = 1000
        self.weapon_mode = g2o.WEAPONMODE_2HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Skeleton Lord')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)