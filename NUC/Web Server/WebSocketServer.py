import asyncio
import websockets
import netifaces as ni

nucIP = ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
print("NUC IP is: " + nucIP)

try:
    rpiWS = websockets.WebSocket()
    rpiWS.connect("ws://10.163.149.122")
    rpiWS.send(nucIP)
except:
    print("connection to raspberry pi failed")
 
# create handler for each connection
data = ""

async def handler(websocket, path):
    while(True):
        data = await websocket.recv()
        reply = f"Data recieved as:  {data}"
        print(reply)
        await websocket.send(reply)
 
start_server = websockets.serve(handler, "localhost", 8000)
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()