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
            return await ctx.send(":warning: **Le paramètre `{}` est manquant !**".format(error.param.name))
        elif isinstance(error, commands.BadArgument):
            return await ctx.send(":warning: **Veuillez vérifier les paramètres de la commande et réessayer.**")
        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send(":warning: **Vous n'avez pas la permission d'effectuer cette commande.**")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(
                ":warning: **Le bot a besoin des permissions suivantes pour effectuer cette commande :** `{}`".format(
                    str(error.missing_perms)))
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            return await ctx.send(":warning: **Une erreur s'est produite.**")


def setup(bot):
    bot.add_cog(CommandsErrorHandler(bot))
