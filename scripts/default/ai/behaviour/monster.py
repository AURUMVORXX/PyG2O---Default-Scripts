import g2o
import random
from .agressive import AIAgressive
from ..helpers import AI_TurnToPlayer, AI_WaitForAction, AI_GetDistancePlayers, AI_Warn

class AIMonster(AIAgressive):
    
    def AttackRoutine(self, ts):
        AI_TurnToPlayer(self.id, self.enemy_id)
        if ((self.wait_until - ts) > 0 or AI_WaitForAction(self.id, self.wait_for_action_id)):
            return None
        
        self.wait_for_action_id = -1
        
        distance = AI_GetDistancePlayers(self.id, self.enemy_id)
        if (distance > self.attack_distance):
            if (not AI_Warn(self, ts)):
                g2o.playAni(self.id, 'S_FISTRUNL')
                
        else:
            g2o.npcAttackMelee(self.id, self.enemy_id, g2o.ATTACK_FORWARD, True)
            self.wait_for_action_id = g2o.getNpcLastActionId(self.id)
            self.wait_until = ts + 1000
            
    def OnFocusChange(self, from_id, to_id):
        if (to_id == -1):
            self.Reset()
            
    def OnHitReceived(self, kid, desc):
        change_action = random.randint(0, 100)
        if (change_action > 60):
            action = random.randint(0, 3)
            if (action == 0):
                g2o.playAni(self.id, 'T_FISTPARADEJUMPB')
            elif (action == 1):
                g2o.playAni(self.id, 'T_FISTRUNSTRAFER')
            elif (action == 2):
                g2o.playAni(self.id, 'T_FISTRUNSTRAFEL')
                
            self.wait_for_action_id = g2o.getNpcLastActionId(self.id)
        
        if (self.enemy_id != kid):
            enemy_distance = AI_GetDistancePlayers(self.id, self.enemy_id)
            killer_distance = AI_GetDistancePlayers(self.id, kid)
            
            if (killer_distance < enemy_distance):
                self.enemy_id = kid