import discord
import sportsreference
from sportsreference.nfl.roster import Player
from sportsreference.nfl.teams import Teams
from sportsreference.nfl.player import AbstractPlayer

pl = {}

async def on_fb(message):
    target = message.content[3: ]
    returnmessage = ''

    if target.startswith('.player'):
        target = message.content.split(' ', 1) #splits into ['.player', 'fname lname']
        iname = target[1]
        target = target[1].split(' ', 1) #['fname', 'lname']
        while len(target[1]) < 4: #if too short add 'x' to id ('til 4 for last, 2 for first)
            target[1] += 'x'
        while len(target[0]) < 2:
            target[0] += 'x'
        idsuffix = ['00','20','99','01'] #need to check everytime
        appendsuffix = ['02','03','21'] #append to idsuffix if '00' or '20', used to mitigate trips to url
        samenameplayers = []
        playID = []
        for suffix in idsuffix: #check all suffixes for a match
            playerid = (target[1].capitalize())[ :4] + (target[0].capitalize())[ :2] + suffix
            playID.append(playerid)
            newplayer = Player(playerid) #create new player based on id
            if newplayer.name != 'None':
                if idsuffix.index(suffix) < 2 and idsuffix[-1] != '21':
                    idsuffix.extend(appendsuffix)
                if newplayer.name == iname: #due to id being truncated, check if equal to inputted name
                    samenameplayers.append(newplayer)
                    
            
        if not samenameplayers:
            returnmessage = '```Could not find player by that name! Please try again.```'
            await message.channel.send(returnmessage)
        else:
            #pl = []
            returnmessage += '```' + 'Use the number reactions (1️⃣) to choose which player\n'
            for player in samenameplayers:
                #pl.append(player)
                returnmessage += player.name + ' ' + player.birth_date[ :4] + '\n'
            returnmessage += '```' 
            await message.channel.send(returnmessage)
            setList(samenameplayers,playID)

def getStats(playID):
    print(playID)
    player = Player(playID)
    print(str(player.passing_yards))
    return "done"

def setList(plist,playID):
    pl.clear()
    i = 0
    for player in plist:
        pl[player.name] = [playID[i]]
        i += 1

def setPlayer(reaction):
    msg = ''
    name = ''
    player = ''
    print(reaction)
    if reaction == '1️⃣':
        name = list(pl)[0]
        player = pl[name]
    if reaction == '2️⃣':
        name = list(pl)[1]
        player = pl[name]
    if reaction == '3️⃣':
        name = list(pl)[2]
        player = pl[name]
    if reaction == '4️⃣':
        name = list(pl)[3]
        player = pl[name]
    if reaction == '5️⃣':
        name = list(pl)[4]
        player = pl[name]
    if reaction == '6️⃣':
        name = list(pl)[5]
        player = pl[name]
    if reaction == '7️⃣':
        name = list(pl)[6]
        player = pl[name]
    if reaction == '8️⃣':
        name = list(pl)[7]
        player = pl[name]
    if reaction == '9️⃣':
        name = list(pl)[8]
        player = pl[name]
    if str(reaction) == ':keycap_ten:':
        name = list(pl)[9]
        player = pl[name]
    print(player)
    msg = '```Player has been set```'
    return msg,player
    










