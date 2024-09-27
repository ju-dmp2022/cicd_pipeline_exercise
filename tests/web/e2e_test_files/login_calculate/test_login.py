
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


class TestForLogin(WebBase):
    
    def login(self):
        """login using the variables and input value using 'send_keys' """
        
        #login variables
        username_id = "username"
        password_id = "password"
        login_id = "login"
        username = "admin"
        password = "test1234"
        logout_button_id = "logout-button"
    
        
        # wait for the driver to load the elemnts
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, username_id))
        )
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, password_id))
        )
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, login_id))
        )
        
        
        # fidn the elements
        username_input = self.driver.find_element(By.ID, username_id)
        password_input = self.driver.find_element(By.ID, password_id)
        login_button   = self.driver.find_element(By.ID, login_id)  

        time.sleep(1)

        #type the credentials & clcik login button
        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(1)
        login_button.click()
        
        
        #wait for the logout button to load
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, logout_button_id))  
        )
        
        #find the logout button
        logout_button = self.driver.find_element(By.ID, logout_button_id)

        #testing the 
        assert_that(logout_button.is_displayed()).is_true()