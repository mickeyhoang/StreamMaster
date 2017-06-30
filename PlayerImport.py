def givePlayers():
    fileLocation = 'SavedData/PlayerData.txt'
    with open(fileLocation) as f:
        playerList = f.readlines()
    return playerList

def addPlayer(pre, player):
    fileLocation = 'SavedData/PlayerData.txt'
    f = open(fileLocation, 'a')
    f.write(pre + ' ' + player + '\n')
    f.close()

def removePlayer(player):
    fileLocation = 'SavedData/PlayerData.txt'
    f = open(fileLocation, 'r')
    playerList = f.readlines()
    f.close()
    f = open(fileLocation, 'w')
    for line in playerList:
        if line != str(player):
            f.write(line)
    f.close()
