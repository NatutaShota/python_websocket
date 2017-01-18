import sys
from websocket import create_connection
ws = create_connection("ws://localhost:8080/ws")
 
if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = 'hello world!'
 
ws.send(message)
ws.recv()
 
ws.close()