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
import time
import sys
import youtube-dl
from discord import opus
logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='log.txt',level=logging.INFO)
client = discord.Client()
servers = list(client.servers)

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            client.captureException()
            pass

@client.async_event
def on_ready():
    print('Connected on discord')
    print(client.user.name)
    print("id : ",client.user.id)
    yield from client.change_presence(game=discord.Game(name="Ready")
    print ('Ready')
    return



@client.async_event
def on_resumed():
    logging.info('Resumed')
    hard = discord.Object(id="178882236324642816")
    yield from client.send_message(hard, "Resumed")

@client.async_event
def on_member_remove(member):
    yield from client.send_message(member, 'Byeeeee ;)')

@client.async_event
def on_member_join(member):
    yield from client.send_message(member, 'Salut :)')


@client.async_event
def on_server_remove(server):
    logging.warning('un serveur a été supprimer de la liste des serveur')


