#Monaco Bot is a Discord bot that adds and removes the Playing Monaco role.
#Copyright (C) 2018 Manik Sinha

import os
import random
import discord
from discord.ext import commands
#import asyncio
TOKEN = os.environ['TOKEN']

PREFIX = '!'

MonacoBot = commands.Bot(
    command_prefix = commands.when_mentioned_or(PREFIX),
    activity = discord.Game("Logging in")
    )

MonacoBot.remove_command("help")

@MonacoBot.event
async def on_ready():
    game = discord.Game(f"@Monaco Bot help or !help")
    await MonacoBot.change_presence(activity = game)

@MonacoBot.command()
async def help(ctx):
    message = (
        "```\n"
        f"Use @Monaco Bot or {PREFIX} before a command.\n\n"
        f"{PREFIX}help            Shows this message.\n"
        f"{PREFIX}roulette        Picks a random thief.\n"
        f"{PREFIX}roulette blonde Picks a random thief including blonde.\n"
        "```\n")
    await ctx.send(message)

@MonacoBot.command()
async def roulette(ctx, blonde = ""):
    """Pick a random thief (use !roulette blonde to include blonde)"""
    thieves = (
        'Lookout',
        'Locksmith',
        'Pickpocket',
        'Cleaner',
        'Gentleman',
        'Redhead',
        'Hacker',
        'Mole')
    if blonde.lower() == "blonde":
        thieves = thieves + ("Blonde",)
    thief = random.choice(thieves)
    emoji = await commands.EmojiConverter().convert(ctx, thief)
    await ctx.send(f"{emoji} {thief}")

@MonacoBot.event
async def on_member_update(before, after):
    if before.activity != after.activity:
        if str(after.activity) == "Monaco":
            role = discord.utils.get(after.guild.roles, name="Playing Monaco")
            await after.add_roles(role)
        elif str(before.activity) == "Monaco":
            role = discord.utils.get(before.guild.roles, name="Playing Monaco")
            await after.remove_roles(role)

MonacoBot.run(TOKEN)
