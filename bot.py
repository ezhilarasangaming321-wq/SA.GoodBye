import discord
from discord.ext import commands

# Step 1: Enable all intents so the bot can track member join/leave events
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Step 2: Event that triggers when the bot successfully connects to Discord
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("------ Bot is Online and Ready! ------")

# Step 3: Event that triggers when a member leaves the server
@bot.event
async def on_member_remove(member):
    # Find the specific channel to send the goodbye message
    # Replace 'goodbye' with your actual channel name, or use an ID
    channel = discord.utils.get(member.guild.text_channels, name="𐏓🍁』ʙyᴇ")
    
    if channel:
        # Get the total number of remaining members in the server
        member_count = member.guild.member_count
        
        # Create the message mentioning their name and count
        goodbye_text = f"Goodbye {member.mention}! You left us as member number {member_count + 1}. Have a good life, Good Boy!"
        
        # Link to a Goodbye GIF (You can replace this URL with any GIF link you like)
        gif_url = "https://media.giphy.com/media/26u4b45b8KlgAB7iM/giphy.gif"
        
        # Create an Embed to neatly display the text and the GIF together
        embed = discord.Embed(
            description=goodbye_text,
            color=discord.Color.red()
        )
        embed.set_image(url=gif_url)
        
        # Send the message to the channel
        await channel.send(embed=embed)

# Step 4: Run the bot with your unique token
# PASTE YOUR DISCORD BOT TOKEN INSIDE THE QUOTES BELOW
bot.run("MTUxNDg1MTk0ODc5MTMzNzA1MA.GbuRL-.JtPFcO87yg6i4IIiLLrNF53dFN8eosg_icrA1Q")
