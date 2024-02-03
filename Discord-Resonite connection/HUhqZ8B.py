import asyncio
import websockets
import discord

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

channelID = 283889214804852736 # insert channel id as an int 
token = open("token.txt", "r").read()

async def echo(websocket, path):
    async for message in websocket:
        channel = client.get_channel(channelID)
        await channel.send(message)

async def startSocket():
        async with websockets.serve(echo, "localhost", 8002):
            print("server started")
            await asyncio.Future()

async def startDCBot():
    await client.start(token)
    
async def main():
    await asyncio.gather(startSocket(), startDCBot())

if __name__ == "__main__":
    asyncio.run(main())