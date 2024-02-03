import asyncio
import websockets

# Defines the WebSocket server address and port
WEBSOCKET_SERVER_ADDRESS = 'localhost'
WEBSOCKET_SERVER_PORT = 8765

# List to store WebSocket clients
clients = set()

# WebSocket server logic
async def server(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the received message to all clients
            for client in clients:
                await client.send(message)
    finally:
        clients.remove(websocket)

# Start the WebSocket server
start_server = websockets.serve(server, WEBSOCKET_SERVER_ADDRESS, WEBSOCKET_SERVER_PORT)

# Run the WebSocket server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
