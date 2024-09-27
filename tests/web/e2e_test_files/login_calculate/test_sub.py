

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


class TestForSub(WebBase):

        def calculate_sub(self):
                """test the subtract functionality GUI"""
                
                #add variables
                first_term_id = "key-7"
                second_term_id = "key-3"
                equal_button_id = "key-equals"
                sub_icon_id = "key-subtract"
                result_screen_id = "calculator-screen"
                
                
                #find the elements + click
                first_term_button = self.driver.find_element(By.ID, first_term_id)
                first_term_button.click()
                
                add_button = self.driver.find_element(By.ID, sub_icon_id)
                add_button.click()
                
                second_term_button = self.driver.find_element(By.ID, second_term_id)
                second_term_button.click()
                
                sum_button = self.driver.find_element(By.ID, equal_button_id)
                sum_button.click()
                
                # Get the result from the calculator screen
                result_screen = self.driver.find_element(By.ID, result_screen_id)
                result_value = result_screen.get_attribute("value")  # Extract the value displayed
                
                # Assert that the result is "10"
                assert_that(result_value).is_equal_to("4")
                print(result_value)