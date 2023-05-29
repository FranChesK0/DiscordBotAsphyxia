import nextcord
from nextcord.ext import commands


class __MusicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @nextcord.slash_command()
    async def clear(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def lyrics(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def now_playing(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def pause(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def play(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def queue(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def repeat_queue(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def repeat_track(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def resume(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def shuffle(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def skip(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def skip_to(self, interaction: nextcord.Interaction):
        pass

    @nextcord.slash_command()
    async def volume(self, interaction: nextcord.Interaction):
        pass


def register_music_cogs(bot: commands.Bot) -> None:
    bot.add_cog(__MusicCog(bot))
