from nextcord.ext.commands import Bot

from bot.cogs.admin import register_admin_cogs
from bot.cogs.user.other import register_other_cogs
from bot.cogs.user import register_user_cogs
from bot.cogs.user.music import register_music_cogs


def register_all_cogs(bot: Bot) -> None:
    cogs = (
        register_admin_cogs,
        register_user_cogs,
        register_music_cogs,
        register_other_cogs,
    )
    for cog in cogs:
        cog(bot)
