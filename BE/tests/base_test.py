
from BE.calculator_helper import CalculatorHelper

# GP = Good Practice
class base_calculator_test:
    
    #this will set the calculator up for each func
    def setup_method(self):
        print('はじめる...')
        self.calculator = CalculatorHelper()
    
    def teardown_method(self):
        print('まって.')
        del self.calculator  #this will delete the insatnce