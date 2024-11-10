import g2o
from scripts.playerlist import PlayerList

@g2o.event('onPlayerJoin')
@g2o.event('onPlayerRespawn')
def evtJoin(**kwargs):
    
    pid = kwargs['playerid']
    
    # Stats
    g2o.setPlayerHealth(pid, 1000)
    g2o.setPlayerMaxHealth(pid, 1000)
    g2o.setPlayerStrength(pid, 200)
    g2o.setPlayerDexterity(pid, 200)
    
    # Weapon skill percent
    g2o.setPlayerSkillWeapon(pid, g2o.WEAPON_1H, 100)
    g2o.setPlayerSkillWeapon(pid, g2o.WEAPON_2H, 100)
    g2o.setPlayerSkillWeapon(pid, g2o.WEAPON_BOW, 100)
    g2o.setPlayerSkillWeapon(pid, g2o.WEAPON_CBOW, 100)
    
    # Items
    g2o.giveItem(pid, 'ITFO_BEER', 1000)
    g2o.giveItem(pid, 'ITFO_WINE', 1000)
    g2o.giveItem(pid, 'ITFO_BOOZE', 1000)
    g2o.giveItem(pid, 'ITFO_ADDON_RUM', 1000)
    g2o.giveItem(pid, 'ITFO_ADDON_GROG', 1000)
    g2o.giveItem(pid, 'ITMI_JOINT', 1000)
    g2o.giveItem(pid, 'ITRW_ARROW', 1000)
    g2o.giveItem(pid, 'ITSC_INSTANTFIREBALL', 1000)
    g2o.giveItem(pid, 'ITPO_HEALTH_ADDON_04', 1000)
    g2o.giveItem(pid, 'ITMW_1H_SPECIAL_04', 1)
    g2o.giveItem(pid, 'ITAR_PAL_M', 1)
    g2o.giveItem(pid, 'ITRW_BOW_L_04', 1)
    
    g2o.equipItem(pid, 'ITAR_PAL_M')
    g2o.equipItem(pid, 'ITMW_1H_SPECIAL_04')
    g2o.equipItem(pid, 'ITRW_BOW_L_04')
    
    g2o.spawnPlayer(pid)
    
    if (evtJoin.eventName == 'onPlayerJoin'):
        g2o.sendMessageToAll(0, 255, 0, f'{g2o.getPlayerName(pid)} connected with the server')
        g2o.setPlayerPosition(pid, 0, 0, 0)
    elif (evtJoin.eventName == 'onPlayerRespawn'):
        g2o.sendMessageToAll(0, 255, 0, f'{g2o.getPlayerName(pid)} has respawned')
        
@g2o.event('onPlayerDead')
def evtDead(**kwargs):
    pid = kwargs['playerid']
    kid = kwargs['killerid']
    
    if (kid == -1):
        g2o.sendMessageToAll(255, 30, 0, f'{g2o.getPlayerName(pid)} killed himself.')
    else:
        g2o.sendMessageToAll(255, 30, 0, f'{g2o.getPlayerName(kid)} killed {g2o.getPlayerName(pid)}')
        
@g2o.event('onPlayerMessage')
def evtMessage(**kwargs):
    pid     = kwargs['playerid']
    message = kwargs['message']
    
    print(f'{g2o.getPlayerName(pid)} said: {message}')
    g2o.sendMessageToAll(pid, 255, 255, 255, message)
    
@g2o.event('onPlayerDisconnect')
def evtDisconnect(**kwargs):
    pid     = kwargs['playerid']
    reason  = kwargs['reason']
    
    PlayerList[pid].clear()
    
    if (reason == g2o.DISCONNECTED):
        g2o.sendMessageToAll(255, 0, 0, f'{g2o.getPlayerName(pid)} disconnected from the server.')
    elif (reason == g2o.LOST_CONNECTION):
        g2o.sendMessageToAll(255, 0, 0, f'{g2o.getPlayerName(pid)} lost connection with the server.')
    elif (reason == g2o.HAS_CRASHED):
        g2o.sendMessageToAll(255, 0, 0, f'{g2o.getPlayerName(pid)} has crashed.')
    
    print('Instance:', g2o.getPlayerInstance(pid))
    
@g2o.event('onPlayerCommand')
def evtCommand(**kwargs):
    params  = [eval(x) if not x.isalpha() else x for x in kwargs['params'].split()]
    pid     = kwargs['playerid']
    cmd     = kwargs['command']
    
    if (cmd == 'heal'):
        g2o.setPlayerHealth(pid, g2o.getPlayerMaxHealth(pid))
        g2o.sendMessageToPlayer(pid, 0, 255, 0, 'Healed')
        
    if (cmd == 'sprint'):
        if(PlayerList[pid].sprintEnabled):
            g2o.removePlayerOverlay(pid, g2o.Mds.id('HUMANS_SPRINT.MDS'))
            g2o.sendMessageToPlayer(pid, 255, 0, 0, 'Sprint disabled')
        else:
            g2o.applyPlayerOverlay(pid, g2o.Mds.id('HUMANS_SPRINT.MDS'))
            g2o.sendMessageToPlayer(pid, 0, 255, 0, 'Sprint enabled')
        
        PlayerList[pid].toggleSprint()
        
    if (cmd == 'virt'):
        if (len(params) == 1 and type(params[0]) == int):
            g2o.sendMessageToPlayer(pid, 255, 0, 0, f'Virtual world was set to: {params[0]}')
            g2o.setPlayerVirtualWorld(pid, params[0])
        else:
            g2o.sendMessageToPlayer(pid, 255, 0, 0, 'Type: /virt id')
            
    if (cmd == 'gd'):
        g2o.setPlayerWorld(pid, 'OLDWORLD\\OLDWORLD.ZEN')
    if (cmd == 'kh'):
        g2o.setPlayerWorld(pid, 'NEWWORLD\\NEWWORLD.ZEN')
    if (cmd == 'jr'):
        g2o.setPlayerWorld(pid, 'ADDON\\ADDONWORLD.ZEN')
        
    if (cmd == 'help'):
        g2o.sendMessageToPlayer(pid, 0, 255, 0, 'Commands:')
        g2o.sendMessageToPlayer(pid, 0, 255, 0, '/heal Restores health')
        g2o.sendMessageToPlayer(pid, 0, 255, 0, '/sprint Enable/Disable sprint')
        g2o.sendMessageToPlayer(pid, 0, 255, 0, '/gd Teleport to Mining Valley')
        g2o.sendMessageToPlayer(pid, 0, 255, 0, '/kr Teleport to Khorinis')
        g2o.sendMessageToPlayer(pid, 0, 255, 0, '/jr Teleport to Jarkendar')