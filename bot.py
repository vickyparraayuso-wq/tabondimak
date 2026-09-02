import os
import random
import asyncio
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", "0"))

MESSAGES = [
    "dejadme en paz joeee!!",
    "Parad ya!!!",
    "no os metáis conmigo!!",
]

# Tiempo aleatorio entre mensajes (en segundos).
MIN_DELAY = 60
MAX_DELAY = 5 * 60

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def mensajes_aleatorios():
    await client.wait_until_ready()

    if not CHANNEL_ID:
        print("Falta DISCORD_CHANNEL_ID.")
        return

    canal = client.get_channel(CHANNEL_ID)
    if canal is None:
        print("No encuentro el canal. Comprueba el ID y los permisos del bot.")
        return

    while not client.is_closed():
        await asyncio.sleep(random.randint(MIN_DELAY, MAX_DELAY))
        await canal.send(random.choice(MESSAGES))

@client.event
async def on_ready():
    print(f"Katia Vidal está conectada como {client.user}.")
    if not hasattr(client, "_mensajes_task"):
        client._mensajes_task = asyncio.create_task(mensajes_aleatorios())

if not TOKEN:
    raise RuntimeError("Define la variable de entorno DISCORD_TOKEN antes de iniciar el bot.")

client.run(TOKEN)
