import discord
from discord.ext import commands

client = commands.Bot(command_prefix="v!")

LIST = ("WIP.")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="with fellow list grinders"))
  print('It works')

@client.command()
async def list(ctx):
    await ctx.send(LIST)


@client.command(pass_context=True)
@commands.has_role('moderator')
async def repeat(ctx, content):
    await ctx.send(content)

client.run("No Token For You >:)")

keep_alive.keep_alive()

# Finally, login the bot
bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
