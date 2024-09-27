

import pytest
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from assertpy import assert_that

class TestForDivide(WebBase):
        
        
        def calculate_divide(self):
                """test the divison functionality of GUI"""
                
                #add variables
                numerator_id = "key-9"
                denominator_id = "key-3"
                calc_tab_id = "toggle-button"
                equal_button_id = "key-equals"
                divide_icon_id = "key-divide"
                result_screen_id = "calculator-screen"
                
                
                #find the elements + click
                first_divide_button = self.driver.find_element(By.ID, numerator_id)
                first_divide_button.click()
                
                divide_button = self.driver.find_element(By.ID, divide_icon_id)
                divide_button.click()
                
                second_divide_button = self.driver.find_element(By.ID, denominator_id)
                second_divide_button.click()
                
                sum_button = self.driver.find_element(By.ID, equal_button_id)
                sum_button.click()
                
                time.sleep(1)
                
                #close the history tab
                tab_button = self.driver.find_element(By.ID, calc_tab_id)
                tab_button.click()
                
                history = self.driver.find_element(By.ID, "history").get_attribute("value").strip()
                print(history)
                
                # Assert that the history content is not equal to the placeholder text
                placeholder = "The history is empty..."
                assert_that(history).is_not_equal_to(placeholder)
                
                # Get the result from the calculator screen
                result_screen = self.driver.find_element(By.ID, result_screen_id)
                result_value = result_screen.get_attribute("value")  # Extract the value displayed
                
                assert_that(result_value).is_equal_to("3")
                print(result_value)