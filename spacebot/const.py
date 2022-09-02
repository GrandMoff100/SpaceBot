import os

TOKEN = os.environ.get("TOKEN")
GUILD_IDS = list(map(int, os.environ.get("GUILD_IDS", "").split(",")))
