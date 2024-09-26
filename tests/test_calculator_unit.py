import pytest
from base_test import BaseCalculatorTest


# GP = Good Practice
class TestCalculatorHelper(BaseCalculatorTest):
    """
    use the imported 'BaseCalculatorTest' 
    and use the fixture data to add 
    fynamic values for the pytests
    """
        
    #fixture to provide data (GP)
    @pytest.fixture
    def value(self):
        return {'a': 33, 'b': -3}
    
    
        
    #(GP)
    def test_add(self, value):
        
        #arrange
        a = value['a']
        b = value['b']
        
        #act
        add = self.calculator.add(a, b)
        
        #assert
        assert add == 30
        
    #(GP)
    def test_subtract(self, value):

        a = value['a']
        b = value['b']
        
        sub = self.calculator.subtract(a, b)
        
        assert sub == 36
        
    #(GP)
    def test_multiply(self, value):

        a = value['a']
        b = value['b']
        
        multi = self.calculator.multiply(a, b)
        
        assert multi == -99
        
    #(GP)
    def test_division(self, value):

        a = value['a']
        b = value['b']
        
        divide = self.calculator.divide(a, b)
        
        assert divide == -11
        
    # exception
    def test_division_by_zero(self):
        """return None as exception when dividing by zero"""
        
        # Arrange
        a = 33
        b = 0
        
        #act
        divide_zero = self.calculator.divide(a, b)
        
        #assert
        assert divide_zero == ZeroDivisionError
        

        

        

  


