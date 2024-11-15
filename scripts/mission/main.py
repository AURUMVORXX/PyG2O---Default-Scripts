import g2o
from .classes import ClassArcher, ClassTank, ClassFighter

@g2o.event('onPlayerJoin')
def evtJoin(**kwargs):
    pid = kwargs['playerid']
    g2o.sendMessageToAll(0, 255, 0, f'{g2o.getPlayerName(pid)} connected with the server.')
    
    ClassArcher(pid)
    g2o.spawnPlayer(pid)
    g2o.setPlayerPosition(pid, 0, 0, 0)
    
@g2o.event('onPlayerRespawn')
def evtRespawn(**kwargs):
    pid = kwargs['playerid']
    
    if (g2o.isNpc(pid)):
        return None
    
    g2o.sendMessageToAll(255, 150, 0, f'{g2o.getPlayerName(pid)} has respawned.')
    
    ClassArcher(pid)
    g2o.spawnPlayer(pid)