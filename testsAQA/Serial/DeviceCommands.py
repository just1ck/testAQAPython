import pytest

@pytest.fixture(scope="class")
def device_commands():
    return {
        "commands": {
            "voltage": "GET_V",
            "ampers": "GET_A",
            "serial": "GET_S"
        }
    }