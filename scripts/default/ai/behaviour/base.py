import g2o


class AIBase:
    
    instance = None
    
    def __init__(self, npc_id):
        self.id = npc_id
        self.spawn = None
        self.instance = None
        
        self.wait_until = 0
        self.wait_for_action_id = -1
        
    def Reset(self):
        self.wait_until = 0
        self.wait_for_action_id = -1
       
    @classmethod 
    def Create(cls, instance = ""):
        instance = instance if instance != '' else cls.instance
        
        npc_id = g2o.createNpc('NPC', instance)
        if (npc_id == -1):
            return None
        
        state = cls(npc_id)
        state.instance = instance
        state.Setup()
        
        return state
    
    def Update(self):
        pass
    
    def Setup(self):
        pass
    
    def Spawn(self):
        pass
    
    def OnHitReceived(self, kid, desc):
        pass