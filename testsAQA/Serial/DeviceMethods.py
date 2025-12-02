import serial.tools.list_ports
import serial


ports = serial.tools.list_ports.comports() #список доступных com-портов

for port in ports:
    print(port.device)


def try_to_connect(port, baudrate):  # Метод подключения к указанному порту
    try:
        deviceSerial = serial.Serial(port=port, baudrate=baudrate)
        return("Connect")
    except:
        return("noConnect")
        

def send_serial_request(port, baudrate, message):  #Отправка сообщения и получение ответа
    deviceSerial = serial.Serial(port=port, baudrate=baudrate)
    deviceSerial.write(message)
    responce = deviceSerial.readline()
    deviceSerial.close()
    return responce