from nextcord.ext.commands import Bot

from admin import register_admin_cogs
from user.other import register_other_cogs
from user import register_user_cogs


def register_all_cogs(bot: Bot) -> None:
    cogs = (
        register_user_cogs,
        register_admin_cogs,
        register_other_cogs,
    )
    for cog in cogs:
        cog(bot)
