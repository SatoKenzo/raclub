import discord
from discord.ext import commands
import os

# Получаем токен из переменной окружения
token = os.getenv('DISCORD_BOT_TOKEN')

# Создаем бота с префиксом команд "!"
bot = commands.Bot(command_prefix='!')

# Событие, которое срабатывает при успешном подключении бота
@bot.event
async def on_ready():
    print(f'{bot.user} успешно подключился к Discord!')

# Команда "!hello", на которую бот будет отвечать "Hello!"
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Запускаем бота
bot.run(token)
