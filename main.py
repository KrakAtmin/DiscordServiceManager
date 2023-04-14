import discord
import subprocess
from embed import *
import os



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

CHANNEL = 'serverterminal'
users = ['VANILLUS#6709', 'Sixcess#2137']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event

async def on_message(message):
    if str(message.channel) != CHANNEL:
        return
    if message.author == client.user:
        return
    if str(message.author) not in users:
        return

    match message.content:
        
        case 'hello':
            await message.channel.send('https://tenor.com/view/kys-keep-yourself-safe-low-tier-god-gif-24664025')
        case 'valheim on':
            if await checkIfProcessRunning('valheim'):
                await message.channel.send('Valheim server is already running')
                return
            else:
                await message.channel.send('Starting Valheim server')
                subprocess.run(['/home/six/CustomServiceRunDiscordBot/valheim_on.sh'])
                return
        case 'valheim off':
            if await checkIfProcessRunning('valheim'):
                await message.channel.send('wylonczam walhajma')
                subprocess.run(['/home/six/CustomServiceRunDiscordBot/valheim_off.sh'])
                return
            else:
                await message.channel.send('Valheim server is not running')
                return
        case 'info' | 'commands' | 'help':
            await message.channel.send(embed=embedVar)
            return
        
async def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    status = subprocess.check_output("systemctl show -p ActiveState --value " + processName + 'server', shell=True)
    if "inactive" in str(status):
        return False
    else:
        return True
 

client.run(os.getenv('TOKEN'))