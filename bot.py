import os
import random
import asyncio
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

# Puedes poner varios IDs separados por comas:
# DISCORD_CHANNEL_IDS=123456789,987654321,555555555
# También se mantiene DISCORD_CHANNEL_ID por compatibilidad si solo quieres uno.
raw_channel_ids = os.getenv("DISCORD_CHANNEL_IDS", "").strip()

if raw_channel_ids:
    try:
        CHANNEL_IDS = [
            int(channel_id.strip())
            for channel_id in raw_channel_ids.split(",")
            if channel_id.strip()
        ]
    except ValueError:
        raise RuntimeError(
            "DISCORD_CHANNEL_IDS debe contener IDs numéricos separados por comas."
        )
else:
    single_channel_id = os.getenv("DISCORD_CHANNEL_ID", "").strip()

    if single_channel_id:
        try:
            CHANNEL_IDS = [int(single_channel_id)]
        except ValueError:
            raise RuntimeError("DISCORD_CHANNEL_ID debe ser un ID numérico.")
    else:
        CHANNEL_IDS = []


MESSAGES = [
    "dejadme en paz joeee!!",
    "Parad ya!!!",
    "no os metáis conmigo!!",
]

# Tiempo aleatorio entre mensajes (en segundos).
MIN_DELAY = 15 * 60
MAX_DELAY = 60 * 60

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def mensajes_aleatorios():
    await client.wait_until_ready()

    if not CHANNEL_IDS:
        print("Falta DISCORD_CHANNEL_IDS (o DISCORD_CHANNEL_ID).")
        return

    canales = []

    for channel_id in CHANNEL_IDS:
        canal = client.get_channel(channel_id)

        if canal is None:
            print(
                f"No encuentro el canal {channel_id}. "
                "Comprueba el ID y los permisos del bot."
            )
            continue

        canales.append(canal)

    if not canales:
        print("No se encontró ningún canal válido.")
        return

    print(f"Canales configurados: {len(canales)}")

    while not client.is_closed():
        await asyncio.sleep(random.randint(MIN_DELAY, MAX_DELAY))

        mensaje = random.choice(MESSAGES)

        for canal in canales:
            try:
                await canal.send(mensaje)
                print(f"Mensaje enviado a #{canal.name} ({canal.id}).")
            except discord.Forbidden:
                print(
                    f"No tengo permisos para escribir en #{canal.name} ({canal.id})."
                )
            except discord.HTTPException as error:
                print(
                    f"Error enviando mensaje a #{canal.name} ({canal.id}): {error}"
                )


@client.event
async def on_ready():
    print(f"Katia Vidal está conectada como {client.user}.")

    if not hasattr(client, "_mensajes_task"):
        client._mensajes_task = asyncio.create_task(mensajes_aleatorios())


if not TOKEN:
    raise RuntimeError(
        "Define la variable de entorno DISCORD_TOKEN antes de iniciar el bot."
    )

client.run(TOKEN)
