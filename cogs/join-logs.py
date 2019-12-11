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

        embed = discord.Embed(description=f"""**{member.mention} vient de rejoindre le serveur.**
        Son compte a été créé le {member.created_at.strftime('%d/%m/%Y')}, soit il y a {(datetime.datetime.now() - member.created_at).days} jours.
        """, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"ID : {member.id} | 👨‍💻 Créé par baptiste0928#0001")

        embed.set_author(name=member, icon_url=member.avatar_url)

        await join_logs.send(embed=embed)


def setup(bot):
    bot.add_cog(JoinLogs(bot))
