
import g2o
from .agressive import AIAgressive
from ..helpers import AI_TurnToPlayer, AI_WaitForAction, AI_GetDistancePlayers, AI_Warn
import random

def get_wm_name(wm):
    if (wm == g2o.WEAPONMODE_FIST):
        return 'FIST'
    elif (wm == g2o.WEAPONMODE_1HS):
        return '1H'
    elif (wm == g2o.WEAPONMODE_2HS):
        return '2H'
    elif (wm == g2o.WEAPONMODE_BOW):
        return 'BOW'
    elif (wm == g2o.WEAPONMODE_CBOW):
        return 'CBOW'
    elif (wm == g2o.WEAPONMODE_MAG):
        return 'MAG'
    else:
        return ''
    
class AIHumanoid(AIAgressive):
    
    def AttackMove(self, ts):
        if (self.weapon_mode >= g2o.WEAPONMODE_1HS and self.weapon_mode <= g2o.WEAPONMODE_2HS):
            g2o.npcAttackMelee(self.id, self.enemy_id, random.randint(g2o.ATTACK_FORWARD, g2o.ATTACK_RIGHT), True)
        elif (self.weapon_mode >= g2o.WEAPONMODE_BOW and self.weapon_mode <= g2o.WEAPONMODE_CBOW):
            g2o.npcAttackRanged(self.id, self.enemy_id, True)
            self.wait_for_action_id = g2o.getNpcLastActionId(self.id)
        elif (self.weapon_mode == g2o.WEAPONMODE_MAG):
            g2o.npcSpellCast(self.id, self.enemy_id, True)
            self.wait_for_action_id = g2o.getNpcLastActionId(self.id)
        else:
            g2o.npcAttackMelee(self.id, self.enemy_id, 0, -1, True)
            
    def ParadeMove(self, wm_name):
        action = random.randint(0, 3)
        
        if (action ==  0):
            g2o.playAni(self.id, f'T_{wm_name}PARADEJUMPB')
        elif (action == 1):
            g2o.playAni(self.id, f'T_{wm_name}RUNSTRAFEL')
        elif (action == 2):
            g2o.playAni(self.id, f'T_{wm_name}RUNSTRAFER')
            
    def EnsureWeapon(self):
        if (g2o.getPlayerWeaponMode(self.id) == g2o.WEAPONMODE_NONE):
            if (self.weapon_mode == g2o.WEAPONMODE_MAG):
                g2o.readySpell(self.id, 0, 0)
            else:
                g2o.drawWeapon(self.id, self.weapon_mode)
                
            self.wait_for_action_id = g2o.getNpcLastActionId(self.id)
            return False
        
        return True
    
    def RemoveWeapon(self):
        weapon_mode = g2o.getPlayerWeaponMode(self.id)
        if (weapon_mode != g2o.WEAPONMODE_NONE):
            g2o.removeWeapon(self.id)
            
    def StartHitCombo(self, wm_name, ts):
        if (self.weapon_mode <= g2o.WEAPONMODE_2HS):
            change_action = random.randint(0, 100)
            if (change_action > 70):
                self.ParadeMove(wm_name)
            else:
                self.AttackMove(ts)
        else:
            self.AttackMove(ts)
            
    def AttackRoutine(self, ts):
        AI_TurnToPlayer(self.id, self.enemy_id)
        if ((self.wait_until - ts) > 0 or AI_WaitForAction(self.id, self.wait_for_action_id)):
            return None
        
        self.wait_for_action_id = -1
        if (not self.EnsureWeapon()):
            return None
        
        distance = AI_GetDistancePlayers(self.id, self.enemy_id)
        wm_name = get_wm_name(self.weapon_mode)
        
        if (distance > self.attack_distance):
            if (not AI_Warn(self, ts)):
                g2o.playAni(self.id, f'S_{wm_name}RUNL')
                
        else:
            self.StartHitCombo(wm_name, ts)
            
    def OnFocusChange(self, from_id, to_id):
        if (to_id == -1):
            g2o.playAni(self.id, 'S_RUN')
            
            self.RemoveWeapon()
            self.Reset()
            
    def OnHitReceived(self, kid, desc):
        change_action = random.randint(0, 100)
        if (change_action > 70):
            self.ParadeMove(get_wm_name(self.weapon_mode))
            self.wait_for_action_id = g2o.getNpcLastActionId(self.id)
            
        if (self.enemy_id != kid):
            enemy_distance = AI_GetDistancePlayers(self.id, self.enemy_id)
            killer_distance = AI_GetDistancePlayers(self.id, kid)
            
            if (killer_distance < enemy_distance):
                self.enemy_id = kid