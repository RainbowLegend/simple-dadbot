# Literally a fucking dad joke bot.
# Created by MystLegend https://github.com/RainbowLegend
# I want to fucking die.
# https://discordapp.com/oauth2/authorize?client_id=514286058285039616&scope=bot&permissions=3072

import discord
from discord.ext import commands
import aiohttp


bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('daddy, '))

bot.remove_command('help')


@bot.command()
async def help(ctx):
    """speds"""
    await ctx.send('my literal only command is `daddy, joke`.\nor maybe `daddy, invite` if ur lucky')


@bot.command()
async def joke(ctx):
    """Gives a fucking dad joke. Sped."""

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"}) as r:
            raw_joke = await r.json()
        j = raw_joke['joke']
        await ctx.send(f'{ctx.message.author.mention}, {j}')


@bot.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=514286058285039616&scope=bot&permissions=3072')


@bot.event
async def on_message(message):
    """I want to die, like seriously."""

    if message.author.id == bot.user.id:
        return

    if "i'm" in message.content.lower():
        res = message.content.lower().split("i'm")
        await message.channel.send(f'hi {res[1]} im dadbot')
      
    elif "im" in message.content.lower():
        res = message.content.lower().split("im")
        await message.channel.send(f'hi {res[1]} im dadbot')
        
    elif "i am" in message.content.lower():
        res = message.content.lower().split("i am")
        await message.channel.send(f'hi {res[1]} im dadbot')
    
    elif "i m" in message.content.lower():
        res = message.content.lower().split("i m")
        await message.channel.send(f'hi {res[1]} im dadbot')
        
    else:
        await bot.process_commands(message)


@bot.event
async def on_ready():
    print('yo estoy ready!')
    print('hi ready!')
    print(f'currently on {len(bot.guilds)}')
    print(f'think i can see {len(set(bot.get_all_members()))}')
    await bot.change_presence(activity=discord.Game(name='`daddy, joke`'))

bot.run('TOKEN')
