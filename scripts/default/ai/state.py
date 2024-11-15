
import g2o

attached = []
states = {}

class AISpawnPoint:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.angle = 0
        self.world = None
        
def AI_GetNPCState(npc_id):
    if (npc_id in states):
        return states[npc_id]
    
    return None

def AI_GetAttachedNPCs():
    return attached

def AI_SpawnNPC(npc_state, x, y, z, angle, world):
    
    attached.append(npc_state)
    states[npc_state.id] = npc_state
    
    npc_state.spawn = AISpawnPoint()
    npc_state.spawn.x = x
    npc_state.spawn.y = y
    npc_state.spawn.z = z
    npc_state.spawn.angle = angle
    npc_state.spawn.world = world
    npc_state.Reset()
    npc_state.Spawn()
    
    g2o.setPlayerWorld(npc_state.id, world)
    g2o.setPlayerPosition(npc_state.id, x, y, z)
    g2o.setPlayerAngle(npc_state.id, angle)
    g2o.spawnPlayer(npc_state.id)