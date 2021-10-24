import discord
import time
import random
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands,tasks



import json



# discord settings 
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!'  , intents = intents)



#ban



#when bot starts up
@client.event 
async def on_ready():     
  for guild in client.guilds:
      print(f"__________________{guild.name}____________________")

#creating database

      try:
        with open(f"{guild.id}.json","r"):
          print("database already made")
      except:
        print("we need to make a db")
        with open(f"{guild.id}.json","a") as file:
          file.write("{}")

      #adding users to database
      with open(f"{guild.id}.json" , 'r') as file: 
        database = json.load(file)
      with open(f"{guild.id}.json" , 'a') as file: 
        for user in guild.members:
          print({user.name})
          if user.name in database:
            print("true")
          else:
            print("false")
            database[user.name] = 'p0gchamp'

      print(database)

      # go through every channel item
      found = False
      for x in range(0,len(guild.channels),1):
        if "join-log" in  guild.channels[x].name :
          found = True
      if found:
        print("aLrEaDy ThErE")
      else:
        print("ADD JOIN LOG HERE!!!!!")
        await guild.create_text_channel('join-log')



    # create server database files
  for guild in client.guilds:
      print(guild.name)




      # print user data
      for member in guild.members:
        if member.bot:
          continue
        print(member.name,member.created_at,member.joined_at)
      print()


#when bot joins server
@client.event
async def on_guild_join(guild):
    print ("joined... " + str (guild.id))
#when bot leaves server



@client.event
async def on_guild_remove(guild):
    print ("left... " + str (guild.id))















#finds all messages
@client.event
async def on_message(message):
  # if bot detects own message then do nothing
  if message.author == client.user:
    return

  if message.content.startswith("HELP ME"):
    await message.channel.send(".spam,.showgames,.weirdwords1,.weirdwords2 and .weirdwords3 are the current commands") 



  if message.content.startswith(".spam"):
    for x in range (0,50,5):
      await message.channel.send("spam ") 
      time.sleep (0.1)
  
  if message.content.startswith(".weirdwords1"):
    await message.channel.send("dopesy frank")

  if message.content.startswith(".weirdwords2"):
    await message.channel.send("oopsie babies")

  if message.content.startswith(".weirdwords3"):
    await message.channel.send("oopsie poo")


  if message.content.startswith(".showgames"):
    await message.channel.send("in this server we play minecraft and roblox mostly")




  if message.content.startswith(".hack"):
    await message.channel.send("hacking account...\nhacking through firewall...\ntaking account...\nstealing passwords...\nusing funds...\nthrowing minecraft diamonds in lava...\nusing fortnite vbucks...\nusing robux...\nThe government has been hacked!")
    
  if message.content.startswith(".help"):
    await message.channel.send(".spam,.showgames,.weirdwords1,.weirdwords2 and .weirdwords3 are the current commands")











@client.event
async def on_member_join(member):
  print(str(member) + " joined")
  with open("database.json" , "a") as file:
    pass

  # send message to join logs
  channel = discord.utils.get(member.guild.text_channels,name = "join-log")


  await channel.send ( f"{member} has joined")
  await member.send('Welcome! . is the command prefix.say .help for commands')























@client.event
async def on_member_remove(member):
  print(str(member) + " is the worst because they left")


















#always be at bottom

client.run("ODQwOTkxNjU3NDE4OTQ4NjQ4.YJgQgw.lToC1Rf_S39mM9xHaxDY5JzYDeU")









'''
NOTES
{

  "username" :
  {
    "id" : "8537657353",
    "messages" : [6,9,0,],
    "money" : 0.00,
    "time_in_server" : 0}
  }




'''