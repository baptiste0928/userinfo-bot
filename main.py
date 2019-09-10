import json
import discord
from discord.ext import commands
import glob
import os

with open('config.json', 'r') as f:
    config = json.load(f)

bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(config.get("prefix", ".")))
bot.remove_command("help")
bot.config = config

modules = []
for file in glob.glob("cogs/*.py"):
    modules.append(file.replace(os.path.sep, '.').replace('.py', ''))

if __name__ == '__main__':
    for extension in modules:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("Failed to load extension {} : {}".format(extension, e))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(status=discord.Status.idle, name=config["activity"],
                                                        type=discord.ActivityType.watching), )
    print("Connected as {}".format(bot.user))
    print("Ready !")

bot.run(config.get("token"))
