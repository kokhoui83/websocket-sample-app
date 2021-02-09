import asyncio
import websockets
import json

async def send_string(message):
    uri = "ws://echo.websocket.org"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        print(f"> sending string")

        response = await websocket.recv()
        print(f"echo received < {response}")

async def send_number(value):
    uri = "ws://echo.websocket.org"
    async with websockets.connect(uri) as websocket:        
        await websocket.send(str(value))
        print(f"> sending number")

        response = await websocket.recv()
        print(f"echo received < {response}")

async def send_json(filename):
    uri = "ws://echo.websocket.org"
    async with websockets.connect(uri) as websocket:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        await websocket.send(json.dumps(data))
        print(f"> sending JSON object")

        response = await websocket.recv()
        print(f"echo received < {response}")

asyncio.get_event_loop().run_until_complete(send_string('hello'))
asyncio.get_event_loop().run_until_complete(send_number(1234))
asyncio.get_event_loop().run_until_complete(send_json('another.json'))