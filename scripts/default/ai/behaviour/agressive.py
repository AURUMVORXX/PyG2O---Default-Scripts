import g2o
from .base import AIBase
from ..helpers import AI_CollectNearestTarget, AI_GetDistancePlayers

class AIAgressive(AIBase):
    
    def __init__(self, npc_id):
        self.enemy_id = -1
        self.collect_target = AI_CollectNearestTarget
        self.weapon_mode = None
        
        self.attack_distance = 300
        self.target_distance = 1000
        self.chase_distance = 1000
        self.warn_time = 0
        
        self.max_distance = 0
        self.warn_start = 0
        super().__init__(npc_id)
        
    def Reset(self):
        super().Reset()
        self.wait_until = 0
        self.warn_start = 0
        self.max_distance = self.target_distance
            
    def ValidateEnemy(self):
        if (self.enemy_id != -1):
                
            if (not g2o.isPlayerConnected(self.enemy_id) or not g2o.isPlayerDead(self.enemy_id)):
                return False
                
            distance = AI_GetDistancePlayers(self.id, self.enemy_id)
            return distance <= self.max_distance
            
        return False
        
    def Update(self, ts):
        if (g2o.isPlayerDead(self.id)):
            return None
        
        if (not self.ValidateEnemy() and self.collect_target):
            last_enemy_id = self.enemy_id
            self.enemy_id = self.collect_target(self)
                
            if (last_enemy_id != self.enemy_id):
                self.OnFocusChange(last_enemy_id, self.enemy_id)
                    
        if (self.enemy_id != -1):
            self.AttackRoutine(ts)
        else:
            self.DailyRoutine(ts)
                
    def AttackRoutine(self, ts):
        pass
        
    def DailyRoutine(self, ts):
        pass
        
    def OnFocusChange(self, from_id, to_id):
        pass