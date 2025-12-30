from keep_alive import keep_alive
keep_alive()
import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# --- KEEP ALIVE ---
app = Flask('')

@app.route('/')
def home():
    return "Astral Guardian is Online and Guarding the Stars!"

def run():
  # We use port 8080 because Replit likes it best
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- BOT SETUP ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class AstralBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        self.waiting_room = []
    async def setup_hook(self):
        await self.tree.sync()
        print("✨ Commands Synced!")

bot = AstralBot()

# --- COMMANDS ---
@bot.tree.command(name="match", description="Find a partner!")
async def match(interaction: discord.Interaction):
    user = interaction.user
    if user in bot.waiting_room:
        await interaction.response.send_message("🌟 You're already in queue!", ephemeral=True)
        return
    if not bot.waiting_room:
        bot.waiting_room.append(user)
        await interaction.response.send_message("🌌 Searching the stars for a partner...", ephemeral=True)
    else:
        partner = bot.waiting_room.pop(0)
        thread = await interaction.channel.create_thread(
            name=f"✨ Match: {user.name} & {partner.name}",
            type=discord.ChannelType.private_thread
        )
        await thread.add_user(user)
        await thread.add_user(partner)
        await interaction.response.send_message(f"✅ Connection Found! {thread.mention}", ephemeral=True)
        await thread.send(f"🌌 **The stars have aligned.**\n{user.mention} ⟷ {partner.mention}")

@bot.tree.command(name="leave", description="Close the portal.")
async def leave(interaction: discord.Interaction):
    if isinstance(interaction.channel, discord.Thread) and "Match:" in interaction.channel.name:
        await interaction.response.send_message("☄️ Closing portal...")
        await interaction.channel.delete()
    else:
        await interaction.response.send_message("❌ Not in a match thread!", ephemeral=True)

# --- START ---
keep_alive()
TOKEN = os.environ.get('DISCORD_TOKEN')
bot.run(TOKEN)
