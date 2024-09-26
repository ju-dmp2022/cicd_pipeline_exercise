import requests as req
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse
from base_test import BaseAPICalculatorTest
import pytest
from assertpy import assert_that

# GP = Good Practice
class TestCalculatorAPI(BaseAPICalculatorTest):
    """use the imported BaseAPICalculatorTest to pass in dynamic values to each function/test"""
    
    # (GP)
    @pytest.fixture
    def dynamic_input_value(self):
         """Provides a dictionary of operands for tests."""
         return {'a': 33, 'b': 0}
    
    # (GP)
    def payload(self, dynamic_input_value, operation):
        """Return a payload for all operations"""
        a = dynamic_input_value['a']
        b = dynamic_input_value['b']
        
        return {
            "operation": operation,
            "operand1": a,
            "operand2": b,
        }
    
    # (GP)
    def test_calculate_add(self, dynamic_input_value):
        """test POST to do add calculation"""

          # Arrange
        inserted_operation = "add"
        payload = self.payload(dynamic_input_value, inserted_operation)
        
        # Act
        response = self.make_calculation(payload)
        status = response.status_code
        calculated_value = response.json()
        
        # Assert and assert_that
        assert calculated_value['result'] == 33
        assert_that(status).is_equal_to(200)
        
    
    # exception test
    def test_calculate_divison(self, dynamic_input_value):
        """test POST to do divide calculation"""
        
        # Arrange
        inserted_operation = "divide"
        payload = self.payload(dynamic_input_value, inserted_operation)
        
        # Act
        response = self.make_calculation(payload)
        calculated_value = response.json()
        
        
        #assertion
        assert calculated_value['result'] is ZeroDivisionError
    
    
    # (GP)
    def make_calculation(self, payload):
        """Make a POST request to the calculate endpoint"""
        
        url = self.base_url + "/calculate"
        return req.post(url, json=payload)
    
    # (GP)
    def test_generated_code_test(self, dynamic_input_value):
        """take the dynamic value and run the sync function in the BE/tests/calculator_client/api/actions/calculate.py"""
        
        
        # Arrange
        a = dynamic_input_value['a']
        b = dynamic_input_value['b']
        operation = Opertions.SUBTRACT
        client = Client(self.base_url)
        
        # Act
        calculated_value = calculate.sync(client=client, body=Calculation(operation, operand1=a, operand2=b))
        
        # Assert
        assert isinstance(calculated_value, ResultResponse)
        assert calculated_value.result == 33
        
    