import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)
version = "1.0.0"

env = {
    "BOT_TOKEN": os.environ['BOT_TOKEN'],
    "YOUTUBE_KEY": os.environ['YOUTUBE_KEY'],
    "REDDIT_ID": os.environ['REDDIT_ID'],
    "REDDIT_SECRET_KEY": os.environ['REDDIT_SECRET_KEY'],
    "REDDIT_PW": os.environ['REDDIT_PW']
}

cogs = ["cogs.music",
        "cogs.soup",
        "cogs.wiki",
        "cogs.reddit",
        "cogs.help"
        ]

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)


@bot.event
async def on_guild_join(guild):
    sys_channel = guild.system_channel
    welcome_embed = discord.Embed(description="▶ **Merhaba! Ben egegl Bot v2.** Beni Discord sunucunuza eklediğiniz "
                                              "için teşekkürler!\n\n▶ **!help** komutu ile işlevlerim hakkında bilgi "
                                              "edinebilirsiniz :)", color=discord.Color.blue())
    await sys_channel.send(embed=welcome_embed)


@bot.command()
async def ping(ctx):
    await ctx.send("version **" + version + "**")


bot.run(env["BOT_TOKEN"])
