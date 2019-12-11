import discord
from discord.ext import commands


class GlobalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h','info'])
    @commands.cooldown(3, 60, type=commands.BucketType.channel)
    async def help(self, ctx):
        join_logs = ctx.guild.get_channel(self.bot.config.get("join_logs_chan", None))

        embed = discord.Embed(title="Aide", description="""
**Commandes**
`{0}userinfo [@utilisateur]`: Affiche les informations sur l'utilisateur mentionné.
`{0}ping`: Affiche la latence du bot.
`{0}help | {0}info`: Affiche l'aide sur le bot.

**Logs des nouveaux membres**
Le bot vous offre la possibilité d'afficher des informations sur les utilisateurs qui rejoingnent votre serveur.
Rendez-vous sur le dépôt GitHub pour plus d'informations.
> **Statut :** {1}

**Informations**
Ce robot est créé par baptiste0928#0001, et est disponible sous [license MIT](https://github.com/baptiste0928/userinfo-bot/blob/master/LICENSE).

[Site internet de l'auteur](https://baptiste0928.net/)
[Dépôt GitHub](https://github.com/baptiste0928/userinfo-bot/)
""".format(self.bot.config.get("prefix", "."), "Activé ({})".format(join_logs.mention) if join_logs else "Désactivé")
                              , color=0x36393f)
        embed.set_footer(text="Made with ❤ by baptiste0928#0001")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(2, 60, type=commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f"Pong ! :ping_pong: `{round(self.bot.latency * 1000)}ms`")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        try:
            self.bot.reload_extension(extension)
        except Exception as e:
            await ctx.send(f"**:warning: Impossible de recharger l'extension `{extension}` : `{str(e)}`**")
        else:
            await ctx.send(f"**:information_source: Extension `{extension}` rechargée !**")


def setup(bot):
    bot.add_cog(GlobalCommands(bot))
