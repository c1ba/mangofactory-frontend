import asyncio
import json

import websockets

# Set to keep track of connected clients
connected_clients = set()


async def on_conection(websocket_client):
    # Register the new client
    connected_clients.add(websocket_client)
    try:
        while True:
            # Receive a message from the current client
            message = await websocket_client.recv()
            print(f"< Received: {message}")

            # Forward the message to other connected clients
            for client in connected_clients:
                if client != websocket_client:  # Don't send the message back to the sender
                    await client.send(message)
                    print(json.dumps(message))
                    print(f"< Forwarded: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")
    finally:
        # Unregister the client when it disconnects
        connected_clients.remove(websocket_client)


async def main():
    # Start the WebSocket server
    async with websockets.serve(on_conection, "localhost", 8765):
        await asyncio.Future()  # Run forever


# Run the server
asyncio.run(main())
