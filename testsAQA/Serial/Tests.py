from DeviceMethods import *
from DeviceCommands import *

import pytest

class Tests:

    port = "COM1" #порт к которому подключаемся
    baudrate = 9600 #скорость передачи данных

    def test_serial_connection(self): #Проверяем коннект к устройству
        connection_test = try_to_connect(port=self.port, baudrate=self.baudrate)
        assert connection_test == "Connect"

    def test_get_voltage(self, device_commands): #проверка получения вольтажа
        responce = send_serial_request(port=self.port, baudrate=self.baudrate, message=device_commands["commands"]["voltage"])
        assert responce is not None
        assert responce == "V_12V"

    def test_get_ampers(self, device_commands): #проверка получения ампер
        responce = send_serial_request(port=self.port, baudrate=self.baudrate, message=device_commands["commands"]["ampers"])
        assert responce is not None
        assert responce == "A_1A"

    def test_get_serial(self, device_commands): #проверка получения серийного номера
        responce = send_serial_request(port=self.port, baudrate=self.baudrate, message=device_commands["commands"]["serial"])
        assert responce is not None
        assert responce == "S_DSA123"

    def test_invalid_request(self): #проверка отправки невалидного запроса
        responce = send_serial_request(port=self.port, baudrate=self.baudrate, message="etldjsnf.dueybd")
        assert responce is not None
        assert responce == "Error Invalid Request!!"

    def test_invalid_request(self): #проверка отправки пустого запроса
        responce = send_serial_request(port=self.port, baudrate=self.baudrate, message="")
        assert responce is not None
        assert responce == "Error Empty Request!!"

    


