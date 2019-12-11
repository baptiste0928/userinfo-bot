import datetime

import discord
from discord.ext import commands


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(5, 60, type=commands.BucketType.user)
    async def userinfo(self, ctx, user_str: str = None):

        if user_str:
            try:
                user = await commands.UserConverter().convert(ctx, user_str)
            except commands.BadArgument:
                try:
                    user = await self.bot.fetch_user(int(user_str))
                except discord.NotFound:
                    await ctx.send(":mag: **Utilisateur introuvable**")
                    return
        else:
            user = ctx.author

        if ctx.guild and ctx.guild.get_member(user.id):
            user = ctx.guild.get_member(user.id)

        embed = discord.Embed(color=0x36393f)

        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Création du compte", value=f"Le {user.created_at.strftime('%d/%m/%Y')} (il y a {(datetime.datetime.now() - user.created_at).days} jours)")

        if isinstance(user, discord.Member):
            embed.add_field(name="Membre de ce serveur", value=f"A rejoint le {user.joined_at.strftime('%d/%m/%Y')} (il y a {(datetime.datetime.now() - user.joined_at).days} jours)")

        embed.set_footer(text=f"ID : {user.id} | 👨‍💻 Créé par baptiste0928#0001")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UserInfo(bot))
