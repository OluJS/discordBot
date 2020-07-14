import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

'Initialising connection '
client = discord.Client()

'on_ready is an event handler '


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    '''
    discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    the find() function is looking for a guild with the same name i've stored as my DISCORD_GUILD variable
    when it's made that connection it will return the elements from that guild
   
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        
    )
 '''


@client.event
async def on_member_join(member):
    '''
    When a user joins a DM will be created and sent to them
    '''
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    movieQuotes = [
        'This is a disaster',
        'Welcome to my world',
        "Toto, I've a feeling we're not in Kansas anymore.",
        "Here's looking at you, kid.",
        "Go ahead, make my day.",
        "All right, Mr. DeMille, I'm ready for my close-up."
    ]

    if message.content == '!movieQuote':
        response = random.choice(movieQuotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.command
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command
async def getAvatar(ctx, member: discord.Member):
    await ctx.send('{}'.format(member.avatar_url))


client.run(TOKEN)
