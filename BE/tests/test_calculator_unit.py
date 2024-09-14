import pytest
from BE.calculator_helper import CalculatorHelper
from assertpy import assert_that as at


# GP = Good Practice
class TestCalculatorHelper():
        
    #fixture to provide data (GP)
    @pytest.fixture
    def value(self):
        return {'a': 33, 'b': 3}
    
    
    #this will set the calculator up for each func
    def setup_method(self):
        print('はじめる!')
        self.calculator = CalculatorHelper()
    
    def teardown_method(self):
        print('まって')
        del self.calculator  #this will delete the insatnce
        
    #(GP)
    def test_add(self, value):
        #arrange
        a = value['a']
        b = value['b']
        
        #act
        add = self.calculator.add(a, b)
        
        #assert
        assert add == 36
        
    #(GP)
    def test_subtract(self, value):

        a = value['a']
        b = value['b']
        
        sub = self.calculator.subtract(a, b)
        
        assert sub == 30
        
    #(GP)
    def test_multiply(self, value):

        a = value['a']
        b = value['b']
        
        multi = self.calculator.multiply(a, b)
        
        assert multi == 99
        
    #(GP)
    def test_division(self, value):

        a = value['a']
        b = value['b']
        
        divide = self.calculator.divide(a, b)
        
        assert divide == 11
        
    def test_division_by_zero(self):
        # Arrange
        a = 33
        b = 0
        
        #act
        divide_zero = self.calculator.divide(a, b)
        
        #assert
        assert divide_zero == None
        

        

        

  


