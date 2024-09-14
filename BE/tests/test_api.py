import requests as req
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse

class TestCalculatorAPI:
    def test_calculate_add(self):
        url = "http://localhost:5000/calculate"

        payload = {
            "operation": "add",
            "operand1": 1,
            "operand2": 1,
        }
        response = req.post(url, json=payload)
        response.status_code == 200
        
    def test_generated_code_test(self):
        client = Client("http://localhost:5000")
        calculated_value = calculate.sync(client=client, body=Calculation(Opertions.ADD, operand1=1, operand2=5))
        assert isinstance(calculated_value, ResultResponse)
        assert calculated_value.result == 6