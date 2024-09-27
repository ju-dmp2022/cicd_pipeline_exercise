
# import pytest
# from tests.web.test_base import WebBase
# from tests.web.pages.login_page import LoginPage

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# import time

# from assertpy import assert_that

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class TestRegister(WebBase):

#     def test_register(self):
#         """Test registration functionality & verify it"""

#         # Initialize the variables for the register
#         register_id = "register"
#         username_id = "username"
#         password_id = "password1"
#         password_repeat_id = "password2"
#         logout_button_id = "logout-button"

#         # Wait for the register button to be clickable
#         WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((By.ID, register_id))
#         )
#         register_button = self.driver.find_element(By.ID, register_id)
#         register_button.click()
        
        
#         #Wait for the page to load by waiting on the username field to load 
#         WebDriverWait(self.driver, 5).until(
#             EC.presence_of_element_located((By.ID, username_id))
#         )
        
#         username_input = self.driver.find_element(By.ID, username_id)
#         username_input.send_keys("Baka")
        
#         password_input = self.driver.find_element(By.ID, password_id)
#         password_input.send_keys("Tokyo999")
        
#         password_input_repeat = self.driver.find_element(By.ID, password_repeat_id)
#         password_input_repeat.send_keys("Tokyo999")
        
#         time.sleep(2)
        
#         register_user = self.driver.find_element(By.XPATH, '//*[@id="register"]')
#         register_user.click()
#         time.sleep(2)
        
#         result_screen = self.driver.find_element(By.ID, logout_button_id)
#         assert_that(result_screen).is_equal_to
        

        
        
        
        
        

        
    
    
    