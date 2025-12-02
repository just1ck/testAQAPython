from UDP.WebSocketTester import WebSocketTester
import pytest

@pytest.fixture(scope="session") #фикстура с экземпляром класса клиента
def ws_tester():
    tester = WebSocketTester("ws://localhost:8765")
    tester.connect()
    yield tester

def test_connection_ping(ws_tester): #проверка подключения
    assert ws_tester.ping_test() == True

def test_get_voltage(ws_tester): #проверка вольтажа
    response = ws_tester.get_voltage()
    expected = {'cmd': 'GET_V', 'payload': 'V_12V'}
    assert response == expected

def test_get_ampers(ws_tester): #проверка ампер
    response = ws_tester.get_ampers()
    expected = {'cmd': 'GET_A', 'payload': 'A_1A'}
    assert response == expected

def test_get_serial(ws_tester): #проверка серийного номера
    response = ws_tester.get_ampers()
    expected = {'cmd': 'GET_S', 'payload': 'S_DSA123'}
    assert response == expected

def test_get_serial(ws_tester): #проверка некорректного запроса
    response = ws_tester.get_random("sffgrer")
    assert response == "Error"


