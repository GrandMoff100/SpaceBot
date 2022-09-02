import nextcord

from spacebot.const import GUILD_IDS, TOKEN
from spacebot.space import Space


class SpaceClient(nextcord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")


client = SpaceClient()

@client.slash_command(guild_ids=GUILD_IDS)
async def space(interaction: nextcord.Interaction, length: int = 10000, chunk_size: int = 1900,):
    """Generate a space message."""
    space = Space.generate(length)
    message = await interaction.response.send_message("In progress...", ephemeral=True)
    for i in range(0, length, chunk_size):
        try:
            await interaction.channel.send("".join(space[i:i + chunk_size]))
        except nextcord.HTTPException:
            pass
    await message.edit(content="Done!", delete_after=10)

if __name__ == "__main__":
    client.run(TOKEN)
