from keep_alive import keep_alive
import discord
import os
import json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = discord.Client()

# Data to be written
dictionary = {}

async def write_json(dictionary):
  # Serializing json 
  json_object = json.dumps(dictionary, indent = 4)
    
  # Writing to sample.json
  with open(dictionary['user']+'.json', 'w') as outfile:
    outfile.write(json_object)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!create-sheet'):
    dictionary['user'] = message.author.name
    print(dictionary)
    await write_json(dictionary)
    await message.channel.send('New sheet created!')

keep_alive()
client.run(os.getenv('TOKEN'))