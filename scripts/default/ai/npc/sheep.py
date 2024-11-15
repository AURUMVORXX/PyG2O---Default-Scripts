import g2o
from ..behaviour.monster import AIMonster

class AISheep(AIMonster):
    
    instance = 'SHEEP'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Sheep')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)
        
class AIHammel(AIMonster):
    
    instance = 'HAMMEL'
    
    def __init__(self, npc_id):
        super().__init__(npc_id)
        
    def Setup(self):
        g2o.setPlayerName(self.id, 'Hammel')
        
    def Spawn(self):
        g2o.setPlayerInstance(self.id, self.instance)