
import g2o
from scripts.player import Player

PlayerList = []

for i in range(0, g2o.getMaxSlots()):
    PlayerList.append(Player())