import requests as req
from BE.calculator_helper import CalculatorHelper

# GP = Good Practice
class BaseCalculatorTest:
    
    #this will set the calculator up for each func
    def setup_method(self):
        print('はじめる...')
        self.calculator = CalculatorHelper()
    
    def teardown_method(self):
        print('まって.')
        del self.calculator              #this will delete the insatnce
        
        
class BaseAPICalculatorTest:
    
    def setup_method(self):
        """Setup resources before each test method"""
        self.base_url = "http://localhost:5000"  
        print('はじめる...')
        self.client = req.Session()      # Persistent session setup

    def teardown_method(self):
        """Tear down resources after each test method"""
        print('まって.')
        self.client.close()              # Close the session after tests