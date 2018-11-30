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
async def help(ctx, message_type=""):
    if message_type != "short":
        message = (
            f"**Use @Monaco Bot or {PREFIX} before a command.**\n\n"
            f"**{PREFIX}help**\n"
            "```Shows this message.```\n"
            f"**{PREFIX}help short**\n"
            "```Shows a shorter help message.```\n"
            f"**{PREFIX}roulette**\n"
            "```Picks a random thief.```\n"
            f"**{PREFIX}roulette blonde**\n"
            "```Picks a random thief including blonde.```\n"
            f"**{PREFIX}map**\n"
            "```Picks a random map.```\n"
            f"**{PREFIX}map N**\n"
            "```Picks a random map and N playable characters.\n"
            "N can be: 0, 1, 2, 3, or 4```\n"
            f"**{PREFIX}map N CAMPAIGN**\n"
            "```Picks a random map from CAMPAIGN and N playable characters.\n"
            "CAMPAIGN can be: locksmith, pickpocket, origins, fin, pvp, or all```")
    else:
        message = (
            "```\n"
            f"Use @Monaco Bot or {PREFIX} before a command.\n\n"
            f"{PREFIX}help            Shows a longer help message\n\n"
            f"{PREFIX}help short      Shows this message.\n\n"
            #f"{PREFIX}help command    Shows help about a specific command.\n"
            f"{PREFIX}roulette        Picks a random thief.\n\n"
            f"{PREFIX}roulette blonde Picks a random thief including blonde.\n\n"
            f"{PREFIX}map             Picks a random map.\n\n"
            f"{PREFIX}map N           Picks a random map and N playable characters.\n"
            "                 N can be: 0, 1, 2, 3, or 4\n\n"
            f"{PREFIX}map N CAMPAIGN  Picks a random map from CAMPAIGN and N playable characters.\n"
            "                 CAMPAIGN can be:\n"
            "                 locksmith, pickpocket, origins, fin, pvp, or all\n"
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

@MonacoBot.command(name='map')
async def random_level(ctx, players = 0, campaign = "all"):
    """Pick a random level."""
    #Limit players to range 0, 4.
    players = max(0, min(players, 4))
    allchars = ("Redhead", "Hacker", "Gentleman", "Mole", "Locksmith", "Lookout", "Pickpocket", "Cleaner")
    levels_dict = {
        "The Prison Break":("Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Hijack at the Hairpin":("Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "The Lebanese Embassy":("Mole","Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Banque Albert":("Mole","Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Manoir Moucharder":("Mole","Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Le Port de la Condamine":("Gentleman", "Mole", "Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Scorpion and the Frog":("Gentleman", "Mole", "Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Centre Hospitalier":("Gentleman", "Mole", "Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Securitech Corp.":("Hacker", "Gentleman", "Mole", "Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Musée Océanographique":("Hacker", "Gentleman", "Mole", "Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Discothèque Rouge":("Hacker", "Gentleman", "Mole", "Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Quartier Diamant":allchars,
        "Galerie D'Art":allchars,
        "Place du Palais":allchars,
        "Casino de Monte Carlo":allchars,
        "Hôtel de Monaco":("Mole", "Gentleman", "Hacker", "Redhead"),
        "Épilogue":("Mole", "Gentleman", "Hacker", "Redhead"),
        "The Sound of Violence":("Redhead", "Hacker", "Gentleman", "Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Foreign Affairs":allchars,
        "Liquidity":allchars,
        "Turf War":allchars,
        "Contraband":allchars,
        "Drowned Rats":allchars,
        "False Teeth":allchars,
        "Devil's Trick":allchars,
        "Scent of a Rival":allchars,
        "The Red Carpet":allchars,
        "The Prestige":allchars,
        "Pearls Before Swine":allchars,
        "Royal Flush":allchars,
        "One Last Job":allchars,
        "Au Revoir":allchars,
        "Identity":("Locksmith", "Lookout", "Pickpocket", "Cleaner"),
        "Prologue: The Mole":("Mole", "Mole", "Mole", "Mole"),
        "Prologue: The Lookout":("Lookout", "Lookout", "Lookout", "Lookout"),
        "Prologue: The Locksmith":("Locksmith", "Locksmith", "Locksmith", "Locksmith"),
        "Prologue: The Pickpocket":("Pickpocket", "Pickpocket", "Pickpocket", "Pickpocket"),
        "Prologue: The Hacker":("Hacker", "Hacker", "Hacker", "Hacker"),
        "Prologue: The Gentleman":("Gentleman", "Gentleman", "Gentleman", "Gentleman"),
        "Prologue: The Blonde":("Blonde", "Blonde", "Blonde", "Blonde"),
        "Epilogue: The Cleaner":("Cleaner", "Cleaner", "Cleaner", "Cleaner"),
        "After the Fire":allchars,
        "Cache":allchars,
        "From Whence He Came":allchars,
        "Scentimentality":allchars,
        "Escape From Monaco":allchars,
        "Lyon's Den":allchars,
        "Hidden in Squalor":allchars,
        "Paris, Forever":allchars,
        "Passport Denied":("Mole", "Lookout", "Cleaner", "Redhead"),
        "Corpse Flower":("Mole", "Lookout", "Cleaner", "Redhead"),
        "Dark and Stormy":("Mole", "Lookout", "Cleaner", "Redhead")}
    levels = [
        "The Prison Break",
        "Hijack at the Hairpin",
        "The Lebanese Embassy",
        "Banque Albert",
        "Manoir Moucharder",
        "Le Port de la Condamine",
        "Scorpion and the Frog",
        "Centre Hospitalier",
        "Securitech Corp.",
        "Musée Océanographique",
        "Discothèque Rouge",
        "Quartier Diamant",
        "Galerie D'Art",
        "Place du Palais",
        "Casino de Monte Carlo",
        "Hôtel de Monaco",
        "Épilogue",
        "The Sound of Violence",
        "Foreign Affairs",
        "Liquidity",
        "Turf War",
        "Contraband",
        "Drowned Rats",
        "False Teeth",
        "Devil's Trick",
        "Scent of a Rival",
        "The Red Carpet",
        "The Prestige",
        "Pearls Before Swine",
        "Royal Flush",
        "One Last Job",
        "Au Revoir",
        "Identity",
        "Prologue: The Mole",
        "Prologue: The Lookout",
        "Prologue: The Locksmith",
        "Prologue: The Pickpocket",
        "Prologue: The Hacker",
        "Prologue: The Gentleman",
        "Prologue: The Blonde",
        "Epilogue: The Cleaner",
        "After the Fire",
        "Cache",
        "From Whence He Came",
        "Scentimentality",
        "Escape From Monaco",
        "Lyon's Den",
        "Hidden in Squalor",
        "Paris, Forever",
        "Passport Denied",
        "Corpse Flower",
        "Dark and Stormy"]
    level_ranges = {
        "all":(0, 51),
        "locksmith":(0, 16),
        "pickpocket":(17, 32),
        "origins":(33, 40),
        "fin":(41, 48),
        "pvp":(49, 51)}
    #level = random.choice(list(levels_dict.keys()))
    campaign = campaign.lower()
    if campaign != "pvp":
        #If campaign is not in ranges.keys() then we use "all" as the key.
        level_range = level_ranges.get(campaign, level_ranges["all"])
        level = random.choice(levels[level_range[0]:(level_range[1] + 1)])
    elif campaign == "pvp":
        pvp_levels = (
            "Épilogue",
            "Passport Denied",
            "Corpse Flower",
            "Dark and Stormy")
        level = random.choice(pvp_levels)

    thieves = random.sample(levels_dict[level], players)
    get_emojis = commands.EmojiConverter().convert
    emojis = [await get_emojis(ctx, thief) for thief in thieves]
    message = "**" + str(level) + "**"
    for i in range(len(thieves)):
        message += "\n" + str(emojis[i]) + " " + str(thieves[i])
    await ctx.send(message)

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
