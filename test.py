import discord
from discord.ext import commands
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
secret = os.g---------etenv("SECRET")

token = secret


# Initialisation du bot avec les intents nécessaires
intents = discord.Intents.default()
intents.messages = True  # Active l'écoute des messages
intents.message_content = True  # Nécessaire pour lire le contenu des messages (important pour les commandes)


bot = commands.Bot(command_prefix="!", intents=intents)


events = []


# Commande pour créer un sondage
@bot.command()
async def sondage(ctx, question: str, date: str , heure : str):

    try:
        event_datetime = datetime.strptime( f"{date} {heure}","%Y-%m-%d %H:%M")
        if event_datetime < datetime.now():
            await ctx.send(" Date à choisir")
            return

        message = await  ctx.send(f"**Sondage**: {question}\n\nRéagir avec ✅ pour **Oui** ou ❌ pour **Non**.")
        await message.add_reaction("✅")
        await message.add_reaction("❌")

        events.append({
            "question": question,
            "datetime": event_datetime,
            "message": message,
        })

        await ctx.send("Sondage crée")
    except ValueError:
        await ctx.send("Format error ")

# Lancer le bot
bot.run(token)
