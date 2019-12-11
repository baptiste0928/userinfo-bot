import sys
import traceback

from discord.ext import commands


class CommandsErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, (commands.CommandNotFound, commands.DisabledCommand, commands.NotOwner)):
            return
        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.send(":warning: **Cette commande ne peut pas être utlisée en message privé.**")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction("⏰")
        elif isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f":warning: **Le paramètre `{error.param.name}` est manquant !**")
        elif isinstance(error, commands.BadArgument):
            return await ctx.send(":warning: **Veuillez vérifier les paramètres de la commande et réessayer.**")
        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send(":warning: **Vous n'avez pas la permission d'effectuer cette commande.**")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(
                f":warning: **Le bot a besoin des permissions suivantes pour effectuer cette commande :** `{str(error.missing_perms)}`")
        else:
            print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            return await ctx.send(":warning: **Une erreur s'est produite.**")


def setup(bot):
    bot.add_cog(CommandsErrorHandler(bot))
