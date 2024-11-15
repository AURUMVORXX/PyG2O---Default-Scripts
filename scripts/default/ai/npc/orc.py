import g2o
from ..behaviour.humanoid import AIHumanoid

class AIOrcWarriorRoam(AIHumanoid):
    
    instance = 'ORCWARRIOR_ROAM'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 250
        self.target_distance = 1000
        self.chase_distance = 500
        self.warn_time = 3000
        self.weapon_mode = g2o.WEAPONMODE_2HS
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Orc')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIOrcShamanSit(AIHumanoid):
    
    instance = 'ORCSHAMAN_SIT'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        self.attack_distance = 1000
        self.target_distance = 1000
        self.chase_distance = 0
        self.weapon_mode = g2o.WEAPONMODE_MAG
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Orc Shaman')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        g2o.setPlayerMaxMana(self.id, 1000)
        g2o.setPlayerMana(self.id, 1000)
        g2o.setPlayerTalent(self.id, g2o.TALENT_MAGE, 6)
        g2o.equipItem(self.id, 'ITSC_INSTANTFIREBALL', 0)