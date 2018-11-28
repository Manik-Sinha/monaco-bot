#Monaco Bot is a Discord bot that adds and removes the Playing Monaco role.
#Copyright (C) 2018 Manik Sinha

import os
import discord
#import asyncio
TOKEN = os.environ['TOKEN']

class MonacoBot(discord.Client):
    #Possible improvement:
    #Add code to add role Playing Monaco if it doesn't exist.
    async def on_member_update(self, before, after):
        if before.activity != after.activity:
            if str(after.activity) == "Monaco":
                role = discord.utils.get(after.guild.roles, name="Playing Monaco")
                #print(f"Adding role {role}")
                await after.add_roles(role)
            elif str(before.activity) == "Monaco":
                role = discord.utils.get(before.guild.roles, name="Playing Monaco")
                #print(f"Removing role {role}")
                await after.remove_roles(role)

client = MonacoBot()
client.run(TOKEN)
