from interactions import Client, Intents
from interactions.ext import prefixed_commands as prefixed
from interactions.ext import hybrid_commands as hybrid

bot = Client(intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT | Intents.GUILD_MESSAGES | Intents.GUILD_MEMBERS)
prefixed.setup(bot, default_prefix="!")
hybrid.setup(bot)

bot.load_extension("wiki")
bot.load_extension("listeners")
bot.load_extension("hidden")
bot.load_extension("vetting")
bot.start('BOT TOKEN HERE')