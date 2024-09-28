
import time


from tests.web.test_base import WebBase

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
from assertpy import assert_that

#these are for the login and calculate
from tests.web.e2e_test_files.login_calculate.test_login import TestForLogin 
from tests.web.e2e_test_files.login_calculate.test_add import TestForAdd
from tests.web.e2e_test_files.login_calculate.test_sub import TestForSub
from tests.web.e2e_test_files.login_calculate.test_multi import TestForMulti
from tests.web.e2e_test_files.login_calculate.test_divide import TestForDivide

#these are for the register test
# from tests.web.e2e_test_files.register.test_register import TestRegister


        
class TestReg(WebBase):
         
    def test_register(self):
        """Test registration functionality & verify it"""

        # Initialize the variables for the register
        register_id = "register"
        username_id = "username"
        password_id = "password1"
        password_repeat_id = "password2"
        logout_button_id = "logout-button"
        name = "Levi"
        password = "Ackermann"
        already_exist = "errormsg"

        # Wait for the register button to be clickable
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, register_id))
        )
        register_button = self.driver.find_element(By.ID, register_id)
        register_button.click()
        
        
        #Wait for the page to load by waiting on the username field to load 
        WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.ID, username_id))
        )
        
        username_input = self.driver.find_element(By.ID, username_id)
        username_input.send_keys(name)
        
        password_input = self.driver.find_element(By.ID, password_id)
        password_input.send_keys(password)
        
        password_input_repeat = self.driver.find_element(By.ID, password_repeat_id)
        password_input_repeat.send_keys(password)
        
        time.sleep(2)
        
        register_user = self.driver.find_element(By.XPATH, '//*[@id="register"]')
        register_user.click()
        time.sleep(2)
        
        try:
            logout_button = self.driver.find_element(By.ID, logout_button_id)
            assert_that(logout_button.text).is_equal_to("Logout")

        except NoSuchElementException:
            # If the logout button is not found, check for the error message
            try:
                error_message = self.driver.find_element(By.ID, already_exist)
                assert_that(error_message.text).is_equal_to("User already exists!")
            except NoSuchElementException:
                assert False, "Neither logout button nor error message found!"
        
        
        
class TestWeb(WebBase):
    
    
    def test_login_and_calculate(self):
        """pass in the login data and login, then assert a destination element such as add, sub, multiply & divide"""
        
        
        TestForLogin.login(self)
        time.sleep(2)
        
        TestForAdd.calculate_add(self)
        time.sleep(2)
        
        TestForSub.calculate_sub(self)
        time.sleep(2)
        
        TestForMulti.calculate_multi(self)
        time.sleep(2)
        
        TestForDivide.calculate_divide(self)
        time.sleep(2)

    
    
    

        
        
        
    
        
        
        
        

        
        
