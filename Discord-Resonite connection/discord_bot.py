import discord
import asyncio
import websockets
import logging
# Discord bot token
TOKEN = open("token.txt", "r").read()

# WebSocket server address
WEBSOCKET_SERVER_ADDRESS = 'ws://localhost:8765'  # Change this to your WebSocket server address


# Define your intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message events

# Create a Discord client
client = discord.Client(intents=intents)

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Event triggered when a message is received
@client.event
async def on_message(message):
   

    # Send the message content to the WebSocket server
    try:
        async with websockets.connect('ws://localhost:8765') as websocket:
            await websocket.send(message.content)
    except Exception as e:
        logging.error(f'Error connecting to WebSocket server: {e}')




# Run the Discord bot and receive messages from the WebSocket server concurrently
async def main():
    await asyncio.gather(
        client.start(TOKEN),
        
    )

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())