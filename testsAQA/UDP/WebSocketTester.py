from UDP.WebSocketClient import *

class WebSocketTester:  #класс с методами отправки сообщений
    def __init__(self, server_url="ws://localhost:8765"): 
        self.client = WebSocketClient(server_url) #Экземпляр класса

    def connect(self): #подключаемся к серверу, метод из класса улиента
        self.client.connect()

    def is_connected(self): #проверка подключения
        return self.client.is_connected()

    def get_voltage(self): # отправка запроса с вольтажем
        return self.client.send_ws_request("GET_V")
    
    def get_ampers(self): #отправка запроса с амперами
        return self.client.send_ws_request("GET_A")
    
    def get_serial(self): #отправка запроса с серийным номером
        return self.client.send_ws_request("GET_S")
    
    def get_random(self, cmd): #отправка запроса с рандомным значением
        return self.client.send_ws_request(cmd)
    
    def ping_test(self): #ping сервера
        try:
            self.client.send_ws_request("ping")
            return True
        except:
            return False