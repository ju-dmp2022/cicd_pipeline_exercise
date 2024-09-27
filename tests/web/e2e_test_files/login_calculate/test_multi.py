

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


class TestForMulti(WebBase):

        def calculate_multi(self):
                """test the multiplication functionality of the GUI"""
                
                #add variables
                first_factor_id = "key-7"
                second_factor_id = "key-3"
                equal_button_id = "key-equals"
                multi_icon_id = "key-multiply"
                result_screen_id = "calculator-screen"
                
                
                #find the elements + click
                first_multi_button = self.driver.find_element(By.ID, first_factor_id)
                first_multi_button.click()
                
                multi_button = self.driver.find_element(By.ID, multi_icon_id)
                multi_button.click()
                
                second_multi_button = self.driver.find_element(By.ID, second_factor_id)
                second_multi_button.click()
                
                sum_button = self.driver.find_element(By.ID, equal_button_id)
                sum_button.click()
                
                
                # Get the result from the calculator screen
                result_screen = self.driver.find_element(By.ID, result_screen_id)
                result_value = result_screen.get_attribute("value")  # Extract the value displayed
                
                # Assert that the result is "10"
                assert_that(result_value).is_equal_to("21")
                print(result_value)