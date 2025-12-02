import websocket
import json

class WebSocketClient:
    def __init__(self, url="ws://localhost:8765"): #инициализируем переменные
        self.url = url
        self.ws = None

    def connect(self): #подключаемся к серверу
        self.ws = websocket.WebSocket()
        self.ws.connect(self.url)
        print("connected")

    def send_ws_request(self, cmd): #отправка запроса

        request = {"CMD": cmd}
        self.ws.send(json.dumps(request))
        
        print(request)

        responce_string = self.ws.recv()
        responce = json.loads(responce_string)

        print(responce)
        return responce




