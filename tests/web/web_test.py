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

from tests.web.e2e_test_files.test_login import login 
from tests.web.e2e_test_files.test_add import calculate_add

class TestWeb(WebBase):
    
    
    def test_login_and_calculate(self):
        """pass in the login data and login, then assert a destination element"""
        
        
        login(self)
        time.sleep(2)
        
        calculate_add(self)
        time.sleep(2)
        

        
        
        
    
        
        
        
    
        
        
        
        
        
        
