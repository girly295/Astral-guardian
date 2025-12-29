import discord
from discord.ext import commands
from discord import app_commands
import os

# 1. Setup Permissions (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class AstralBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        self.waiting_room = []

    async def setup_hook(self):
        # This makes your /match and /leave commands show up in Discord
        await self.tree.sync()
        print("✨ Astral Commands Synced!")

bot = AstralBot()

@bot.event
async def on_ready():
    print(f'🌌 Astral Guardian is Online as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Watching the Stars 🌌"))

# --- UPDATED MATCH COMMAND ---
@bot.tree.command(name="match", description="Find a random star to chat with!")
async def match(interaction: discord.Interaction):
    user = interaction.user
    
    # 1. Safety Check: Don't let the same person join twice
    if user in bot.waiting_room:
        await interaction.response.send_message("🌟 You are already searching the galaxy! Please wait for a partner.", ephemeral=True)
        return

    # 2. If nobody is waiting, add them to the queue
    if not bot.waiting_room:
        bot.waiting_room.append(user)
        await interaction.response.send_message("🌌 You've entered the Astral Queue. Waiting for a connection...", ephemeral=True)
    
    # 3. If someone IS waiting, pair them up!
    else:
        partner = bot.waiting_room.pop(0)
        
        # 4. Final Safety: Ensure you didn't match with yourself
        if partner.id == user.id:
            bot.waiting_room.append(user) # Put you back in
            await interaction.response.send_message("🛰️ Still searching for a partner...", ephemeral=True)
            return

        # Create the thread
        thread = await interaction.channel.create_thread(
            name=f"✨ Match: {user.name} & {partner.name}",
            type=discord.ChannelType.private_thread,
            auto_archive_duration=10080
        )
        
        await thread.add_user(user)
        await thread.add_user(partner)
        
        await interaction.response.send_message(f"✅ Connection Found! {thread.mention}", ephemeral=True)
        await thread.send(f"🌌 **The stars have aligned.**\n{user.mention} ⟷ {partner.mention}")

# --- LEAVE COMMAND ---
@bot.tree.command(name="leave", description="Close the current star portal.")
async def leave(interaction: discord.Interaction):
    # Only works if they are inside a Match thread
    if isinstance(interaction.channel, discord.Thread) and "Match:" in interaction.channel.name:
        await interaction.response.send_message("☄️ Closing the portal... Goodbye, stars.")
        await interaction.channel.delete()
    else:
        await interaction.response.send_message("❌ You are not in an active match thread!", ephemeral=True)

# 2. Running the Bot 
# This looks for the 'DISCORD_TOKEN' you put in the Replit Secrets (padlock icon)
TOKEN = os.environ.get('DISCORD_TOKEN')
bot.run(TOKEN)
