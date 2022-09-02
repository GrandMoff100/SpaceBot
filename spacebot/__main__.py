import nextcord

from spacebot.const import GUILD_IDS, TOKEN
from spacebot.space import Space


class SpaceClient(nextcord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")

    @nextcord.slash_command(guild_ids=GUILD_IDS)
    async def space(self, ctx: nextcord.SlashContext, length: int = 1000):
        await ctx.send(Space.generate(length))


if __name__ == "__main__":
    client = SpaceClient()
    client.run(TOKEN)
