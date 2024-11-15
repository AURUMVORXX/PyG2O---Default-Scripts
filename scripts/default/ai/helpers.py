import g2o

def AI_GetDistancePlayers(from_id, to_id):
    from_pos    = g2o.getPlayerPosition(from_id)
    to_pos      = g2o.getPlayerPosition(to_id)
    
    return g2o.getDistance3d(from_pos['x'], from_pos['y'], from_pos['z'], to_pos['x'], to_pos['y'], to_pos['z'])

def AI_GetAngleToPlayer(from_id, to_id):
    from_pos    = g2o.getPlayerPosition(from_id)
    to_pos      = g2o.getPlayerPosition(to_id)
    
    return g2o.getVectorAngle(from_pos['x'], from_pos['z'], to_pos['x'], to_pos['z'])

def AI_TurnToPlayer(from_id, to_id):
    from_pos    = g2o.getPlayerPosition(from_id)
    to_pos      = g2o.getPlayerPosition(to_id)
    
    g2o.setPlayerAngle(from_id, g2o.getVectorAngle(from_pos['x'], from_pos['z'], to_pos['x'], to_pos['z']))
    
def AI_WaitForAction(npc_id, action_id):
    return action_id != -1 and not g2o.isNpcActionFinished(npc_id, action_id)

def AI_Warn(npc_state, ts):
    
    if (npc_state.warn_time == 0):
        return False
    
    if (npc_state.warn_start == 0):
        npc_state.warn_start = ts
    
    if ((ts - npc_state.warn_start) < npc_state.warn_time):
        g2o.playAni(npc_state.id, 'T_WARN')
        return True
    
    return False

def AI_CollectNearestTarget(npc_state):
    
    streamed = g2o.getStreamedPlayersByPlayer(npc_state.id)
    from_pos = g2o.getPlayerPosition(npc_state.id)
    
    nearest_playerid = -1
    nearest_distance = 999999
    
    for pid in streamed:
        if (g2o.isPlayerDead(pid)):
            continue
        
        to_pos      = g2o.getPlayerPosition(pid)
        distance    = g2o.getDistance3d(from_pos['x'], from_pos['y'], from_pos['z'], to_pos['x'], to_pos['y'], to_pos['z'])
        
        if (distance < nearest_distance and distance <= npc_state.target_distance):
            nearest_playerid = pid
            nearest_distance = distance
            
    return nearest_playerid