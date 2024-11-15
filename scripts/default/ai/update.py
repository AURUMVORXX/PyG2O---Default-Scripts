
import g2o
import time
from threading import Timer, get_ident, active_count
from .state import AI_GetAttachedNPCs, AI_GetNPCState

initial_ts = int(time.time() * 1000)
timer = None

def AI_Update():
    current_ts = int(time.time() * 1000) - initial_ts
    npcs = AI_GetAttachedNPCs()
    
    for state in npcs:
        state.Update(current_ts)
        
    timer = Timer(0.5, AI_Update)
    timer.start()

timer = Timer(0.5, AI_Update)
timer.start()

@g2o.event('onPlayerDamage')
def AI_HitNPC(**kwargs):
    pid = kwargs['playerid']
    kid = kwargs['killerid']
    desc = kwargs['description']
    
    if (kid != -1 and pid >= g2o.getMaxSlots()):
        
        npc_state = AI_GetNPCState(pid)
        if (npc_state):
            npc_state.OnHitReceived(kid, desc)
            
@g2o.event('onPlayerRespawn')
def AI_RespawnNPC(**kwargs):
    pid = kwargs['playerid']
    
    if (g2o.isNpc(pid)):
        npc_state = AI_GetNPCState(pid)
        if (npc_state):
            npc_state.Reset()
            npc_state.Spawn()
            
            g2o.setPlayerWorld(npc_state.id, npc_state.spawn.world)
            g2o.setPlayerPosition(npc_state.id, npc_state.spawn.x, npc_state.spawn.y, npc_state.spawn.z)
            g2o.setPlayerAngle(npc_state.id, npc_state.spawn.angle)
            g2o.spawnPlayer(pid)