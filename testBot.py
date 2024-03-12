import os
import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    scheduler = AsyncIOScheduler()
    scheduler.configure(timezone=pytz.timezone('Europe/Moscow'))
    scheduler.add_job(send_scheduled_message, 'cron', day_of_week='wed', hour=0, minute=55)
    scheduler.start()

async def send_scheduled_message():
    channel = bot.get_channel(1217120251712635000)  # Замените YOUR_CHANNEL_ID на ID вашего канала
    embed = discord.Embed(title="Дорогие гости, уже завтра мы приглашаем вас на наше мероприятие Dirty Суббота!",
                          description="**🕗 ВРЕМЯ МЕРОПРИЯТИЯ:**\nНачало в <t:1711220400:t>\n<@&875933871533858827><@&1173642253785378946><@&962391869730463835><@&962395636580372503><@&962473386301333524> - <t:1711218900:t>\n<@&874169841718792210>   - <t:1711219500:t>\n\nКидать реквесты <:1_:874956429520408576>  на **RaClub2**, мир только по приглашениям. Не присылайте запрос раньше времени, если вы будете спамить, вы рискуете попасть в черный список. \nВы можете добавить <:118:874956247374364702>  по ссылке: https://vrchat.com/home/user/usr_5f1695a1-356a-4362-9a4a-741b26a57ced\n\n❗Обязательные правила: \nㅤㅤ· Только 18+\nㅤㅤ· Не трогайте танцоров без их разрешения\nㅤㅤ· Когда вы войдете в мир или заранее - <:green:969335195230683146>  \nㅤㅤнаденьте оптимизированный аватар!\nㅤㅤ· Если у вас слабый компьютер, выключите \nㅤㅤв Safety все аватары, включите \nㅤㅤтанцоров отдельно. Это поможет уменьшить \nㅤㅤколичество лагов\nㅤㅤ· Пожалуйста, не покидайте свои места\nㅤㅤ на диванах без нужды\nㅤㅤ· Уважайте мероприятие, введите себя тише\nㅤㅤ во время танцев",
                          color=13192090)
    embed.set_author(name="Diraccoonr", icon_url="https://media.discordapp.net/attachments/1034855087375388754/1048660139416236093/Dira.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1057258202128982016/1217190509236191412/-32556.png")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1057258202128982016/1217198335207669903/Logo1.png")

    await channel.send(embeds=[embed])


bot.run(os.getenv('DISCORD_BOT_TOKEN'))
