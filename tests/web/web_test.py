
import time
from tests.web.test_base import WebBase
import time
from tests.web.pages.register_page import RegisterPage
from tests.web.pages.calculation import Calculate
from tests.web.pages.history_check import HistoryCheck
import random
import string
from assertpy import assert_that
        
class TestScenarios(WebBase):
    """test the different scenarios for e2e tests"""
    
    def generate_random_username(self, length=8):
        """generate a random username to acoid issues with tests in dev"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
        
     
    
    def test_register(self):
        """Test registration functionality & verify successful reg"""
        
        rp = RegisterPage(self.driver)
        unigue_name = self.generate_random_username()
        rp.click_register()
        
        rp.register(unigue_name, 'toji', 'toji')
        time.sleep(3)
        assert_that()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # LoginPage(self.driver).page_elements['register'].click()
        # LoginPage(self.driver).page_elements['username'].set('Toji')
        # LoginPage(self.driver).page_elements['password'].set('zenin999')
        # LoginPage(self.driver).page_elements['password-verify'].set('zenin999')
        # LoginPage(self.driver).page_elements['register'].click()
        # time.sleep(3)
       
        # assert LoginPage(self.driver).page_elements['logout'].text == 'Logout'
        # LoginPage(self.driver).page_elements['logout'].click()
        # time.sleep(2)
        
    def test_calculation(self):
        """execute calculations and verify the assertions"""
        #login
        
        
        Calculate(self.driver).page_elements['username'].set('Toji')
        Calculate(self.driver).page_elements['password'].set('zenin999')
        Calculate(self.driver).page_elements['login'].click()
        time.sleep(2)
        
        #verify the login
        assert LoginPage(self.driver).page_elements['logout'].text == 'Logout'
        
        
        #addtion calculations and check
        Calculate(self.driver).page_elements['choice1'].click()
        Calculate(self.driver).page_elements['add'].click()
        Calculate(self.driver).page_elements['choice2'].click()
        Calculate(self.driver).page_elements['sum'].click()
        assert Calculate(self.driver).page_elements['result'].value == '8'
        
        
        #subtract calculations and check
        Calculate(self.driver).page_elements['choice1'].click()
        Calculate(self.driver).page_elements['sub'].click()
        Calculate(self.driver).page_elements['choice2'].click()
        Calculate(self.driver).page_elements['sum'].click()
        assert Calculate(self.driver).page_elements['result'].value == '4'
        
        #multiplication calculations and check
        Calculate(self.driver).page_elements['choice1'].click()
        Calculate(self.driver).page_elements['multi'].click()
        Calculate(self.driver).page_elements['choice2'].click()
        Calculate(self.driver).page_elements['sum'].click()
        assert Calculate(self.driver).page_elements['result'].value == '12'
        
        #division calculations and check
        Calculate(self.driver).page_elements['choice1'].click()
        Calculate(self.driver).page_elements['div'].click()
        Calculate(self.driver).page_elements['choice2'].click()
        Calculate(self.driver).page_elements['sum'].click()
        assert Calculate(self.driver).page_elements['result'].value == '3'
        
        
        LoginPage(self.driver).page_elements['logout'].click()
        assert Calculate(self.driver).page_elements['login'].text == 'Login'
        time.sleep(2)
        
    def test_history(self):
        """implement a scenario that verfies the history feature of the calculator"""
        
        # Login
        HistoryCheck(self.driver).page_elements['username'].set('Toji')
        HistoryCheck(self.driver).page_elements['password'].set('zenin999')
        HistoryCheck(self.driver).page_elements['login'].click()
        time.sleep(2)
       
        #verify the login
        assert LoginPage(self.driver).page_elements['logout'].text == 'Logout'
        
        
        # Perform calculations
        
        #addtion calculations and check
        HistoryCheck(self.driver).page_elements['choice1'].click()
        HistoryCheck(self.driver).page_elements['add'].click()
        HistoryCheck(self.driver).page_elements['choice2'].click()
        HistoryCheck(self.driver).page_elements['sum'].click()
        assert HistoryCheck(self.driver).page_elements['result'].value == '8'
        
        
        # Open the history by clicking the '>>'-button
        
        
        
        # Verify previous calculations are shown
    
    
    

        
        
        
    
        
        
        
        

        
        
