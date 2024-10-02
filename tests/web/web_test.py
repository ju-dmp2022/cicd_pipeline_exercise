import pytest
import time
from assertpy import assert_that
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.calculator_page import CalculatorPage
from tests.web.pages.register_page import RegisterPage
import random
import string

class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).login('admin', 'test1234')
        assert_that(CalculatorPage(self.driver).elements.username.text).is_equal_to('admin')


    def generate_random_username(self, length=8):
        """Generate a random username to avoid conflicts."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
      
        

    def test_register(self):
        login_page = LoginPage(self.driver)
        login_page.click_register()

        register_page = RegisterPage(self.driver)
        unique_username = self.generate_random_username()
        register_page.register_user(unique_username, 'test123', 'test123')
        time.sleep(5)
        assert_that(CalculatorPage(self.driver).elements.username.text).is_equal_to(unique_username)


      
    
    @pytest.mark.parametrize("operation, operand1, operand2, expected_result", [
        ('add', 5, 3, '8'),
        ('subtract', 10, 3, '7'),
        ('multiply', 4, 5, '20'),
        ('divide', 8, 2, '4'),
    ])
    def test_calculation(self, operation, operand1, operand2, expected_result):
        LoginPage(self.driver).login('admin', 'test1234')
        calculator_page = CalculatorPage(self.driver)
        calculator_page.perform_operation(operation, operand1, operand2)
        assert_that(calculator_page.get_result()).is_equal_to(expected_result)
 

    
    def test_history(self):
        LoginPage(self.driver).login('admin', 'test1234')
        calculator_page = CalculatorPage(self.driver)
        calculator_page.perform_operation('add', 5, 3)
        calculator_page.perform_operation('subtract', 10, 3)
        calculator_page.open_history()
        time.sleep(5)
        calculator_page.get_history()
        history_text = calculator_page.get_history()
        assert_that(history_text).contains('5+3=8')
        assert_that(history_text).contains('10-3=7')