import discord
import sportsreference

from sportsreference.nfl.roster import Player
from sportsreference.nfl.player import AbstractPlayer



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
        for suffix in idsuffix: #check all suffixes for a match
            playerid = (target[1].capitalize())[ :4] + (target[0].capitalize())[ :2] + suffix
            newplayer = Player(playerid) #create new player based on id
            if newplayer.name != 'None':
                if idsuffix.index(suffix) < 2 and idsuffix[-1] != '21':
                    idsuffix.extend(appendsuffix)
                if newplayer.name == iname: #due to id being truncated, check if equal to inputted name
                    samenameplayers.append(newplayer)
            
        if not samenameplayers:
            returnmessage = 'Could not find player by that name! Please try again.'
            await message.channel.send(returnmessage)
        else:
            for player in samenameplayers:
                returnmessage += player.name + ' ' + player.birth_date[ :4] + '\n'
            await message.channel.send(returnmessage)