"""Copyright (C) 2016  Jbdo99

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import asyncio
import discord
import logging
import os
import subprocess
import time
import sys
import youtube_dl
from discord import opus
logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='log.txt',level=logging.INFO)
client = discord.Client()
servers = list(client.servers)

if (os.name=="posix"):
    SPE="LMAC"
elif (os.name=="nt"):
    SPE="WIN"
else:
    print("Systeme non reconnu, merci de poser une issue sur le github")

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def opus.load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
        	print(OSError)
            pass

def is_me(m):
    return m.author == client.user

is_c_co = False

@client.event
async def my_background_task():
	await client.wait_until_ready()
	counter = 0
	channel = discord.Object(id='178882236324642816')
	while not client.is_closed:
		await asyncio.sleep(300) # task runs every 30 Minutes
		counter += 10
		await client.send_message(channel,'Active for : '+str(counter)+' Minutes')

@client.async_event
def on_ready():
    print('Connected on discord')
    print(client.user.name)
    print("id : ",client.user.id)
    yield from client.change_presence(game=discord.Game(name="Ready"))
    print ('Ready')
    return

@client.async_event
def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.content.split()[0]=="Join":
        global is_c_co
        global voice
        voice = yield from client.join_voice_channel(message.author.voice.voice_channel)
        yield from client.delete_message(message)
        is_c_co=True

    if message.content.split()[0]=="Play":
        global is_c_co
        global voice
        global player
        if is_c_co==True:
            player = yield from voice.create_ytdl_player(message.content.split()[1])
            player.start()
        else:
            voice = yield from client.join_voice_channel(message.author.voice.voice_channel)
            player = yield from voice.create_ytdl_player(message.content.split()[1])
            player.start()




client.run('MjQ4ODg0MDQ4NDgxNjE1ODcz.Cw-O2g.k6AWKhixwgkqnBX-CDOlMu59iso')



