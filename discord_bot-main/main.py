import discord
from discord.ext import commands
import random as r
from settings import *
from bot_logic import gen_pass
from bot_logic import random_funfact
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='@', intents=intents)
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
#client = discord.Client(intents=intents)

smieci = {
    "papier": "pojemnika na papier",
    "szkło": "pojemnika na szkło",
    "plastik": "pojemnika na plastik",
    "bio": "pojemnika na bio",
}
rozkladd = {
    "papier": "od nawet kilku tygodni do około pół roku.",
    "szkło": "około 4000 lat",
    "plastik": "około 500 lat",
    "bio": "od 1 do 6 miesięcy",
}
szkodliwosci_papieru = [
    "Produkcja papieru często wiąże się z wycinką drzew. Jeśli nie jest prowadzona w sposób zrównoważony, może prowadzić do wylesienia i zniszczenia siedlisk.",
    "Proces produkcji papieru wymaga znacznej ilości energii i wody, co przyczynia się do wyczerpywania zasobów i emisji gazów cieplarnianych.",
    "Przemysł papierniczy używa różnych substancji chemicznych do rozdrabniania masy drzewnej i bielenia papieru, co może prowadzić do zanieczyszczenia wód, jeśli nie są one odpowiednio oczyszczane.",
    "Odpady papierowe mogą trafiać na wysypiska, jeśli nie są recyklingowane lub kompostowane, co zajmuje miejsce i prowadzi do emisji metanu, potężnego gazu cieplarnianego."
]
szkodliwosci_szkla = [
    "Proces produkcji szkła wymaga dużej ilości energii, co przyczynia się do emisji gazów cieplarnianych.",
    "Szkło jest ciężkie i wymaga więcej energii do transportu niż niektóre inne opakowania.",
    "Uszkodzone szkło może stanowić zagrożenie w procesie recyklingu."
]
szkodliwosci_plastiku = [
    "Produkcja plastiku opiera się na ropie naftowej, co ma negatywny wpływ na środowisko i prowadzi do emisji gazów cieplarnianych.",
    "Plastik jest trudny do rozkładu i może zanieczyszczać glebę i wody, tworząc tzw. plastikowe śmieci.",
    "Plastikowe odpady w oceanach stanowią poważne zagrożenie dla ekosystemów morskich i organizmów."
]
szkodliwosci_bio = [
    "Odpady biodegradowalne, takie jak jedzenie, wciąż mogą stanowić problem, jeśli nie są odpowiednio utylizowane w kompostowni.",
    "Niewłaściwie skompostowane odpady biodegradowalne mogą wytwarzać metan, potężny gaz cieplarniany.",
    "W przypadku braku właściwej infrastruktury do kompostowania, odpady bio mogą trafiać na wysypiska, przyczyniając się do problemów związanych z odpadami."
]

szkodliwosci = {
    "papier": szkodliwosci_papieru,
    "szklo": szkodliwosci_szkla,
    "plastik": szkodliwosci_plastiku,
    "bio": szkodliwosci_bio
}
@bot.event
async def on_ready():
    print(f'You got logged into: {bot.user}')
@bot.command()
async def sort(ctx, item):
    # Check if the item is in the dictionary
    if item in smieci:
        response = f"Wrzuć to do {smieci[item]}."
    else:
        response = "Wrzuć to do kategorii 'inne'."

    # Send the response to the user
    await ctx.send(response)
@bot.command()
async def rozklad(ctx, item):
    # Check if the item is in the dictionary
    if item in rozkladd:
        response = f" rozklada sie {rozkladd[item]}."
    else:
        response = "niezbyt możemy to obliczyć :sad:."

    # Send the response to the user
    await ctx.send(response)

@bot.command()
async def problemy(ctx, item):
    # Check if the item is in the dictionary
    if item in smieci:
        response = f" problemy związanie z {item}: {szkodliwosci[item]}."
    else:
        response = "niezbyt możemy to obliczyć :sad:."

    # Send the response to the user
    await ctx.send(response)
#list_of_commands=[
#    "help", #0
#    "hello", #1
#    "are_you_here", #2
#    "give_me_random_funfact", #3
#    "generate_password", #4
#    "add_numbers" #5
#]
#@bot.command()
#async def hello(ctx):
#    await ctx.send(f'Cześć')
#@bot.command()
#async def heh(ctx, count=5):
#    for i in range(count):
#        await ctx.send('he')
    
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith("."):
#        if message.content.startswith(list_of_commands[0]):
#            await message.channel.send("List of commands:")
#            print("writing command:", list_of_commands[0])
#            
#            for i in range(len(list_of_commands)):
#                await message.channel.send(list_of_commands[i])
#                
#        elif message.content.startswith(list_of_commands[1]):
#            await message.channel.send("Hello!")
#            print("writing command:", list_of_commands[1])
#            
#        elif message.content.startswith(list_of_commands[2]):
#            await message.channel.send("Yes I'am Here :laughing:")
#            print("writing command:", list_of_commands[2])
#            
#        elif message.content.startswith(list_of_commands[3]):
#            await message.channel.send(random_funfact())
#            await message.channel.send("how cool is that :sunglasses:")
#            print("writing command:", list_of_commands[3])
#        elif message.content.startswith(list_of_commands[4]):
#            await message.channel.send('your password:')
#            await message.channel.send(gen_pass(25))
#        elif message.content.startswith(list_of_commands[5]):
#                pass

bot.run("MTE2NTU3MzAxOTMzNTM5NzQyNg.GmBJIz.Kf40BbN8lTaeBT86zGiLgTYeEfrhqh-i2HfqQs")
