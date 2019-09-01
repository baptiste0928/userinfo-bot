import discord
from discord.ext import commands
import datetime


class JoinLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join_logs = member.guild.get_channel(self.bot.config.get("join_logs_chan", None))

        if join_logs is None:
            return

        embed = discord.Embed(description="""**{} vient de rejoindre le serveur.**
        Son compte a été créé le {}, soit il y a {} jours.
        """.format(member.mention, member.created_at.strftime('%d/%m/%Y'),
                   (datetime.datetime.now() - member.created_at).days), timestamp=datetime.datetime.now())
        embed.set_footer(text="ID : {} | 👨‍💻 Créé par baptiste0928#0001".format(member.id))

        embed.set_author(name="{}#{}".format(member.name, member.discriminator), icon_url=member.avatar_url)

        await join_logs.send(embed=embed)


def setup(bot):
    bot.add_cog(JoinLogs(bot))
