from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class RegisterPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            
            'register': Element('//*[@id="register"]', self), #i just use this twice
            'username': Element('//*[@id="username"]', self),
            'password': Element('//*[@id="password1"]', self),
            'password_verify': Element('//*[@id="password2"]', self),
            'name_check': Element('//*[@id="user-name"]', self),
            'logout': Element('//*[@id="logout-button"]', self)
        }

        self.elements = munchify(self.page_elements)

    def register(self, username, password, password_verify):
        self.elements.username.set(username)
        self.elements.password.set(password)
        self.elements.password_verify.set(password_verify)
        self.elements.register.click()
        
    def click_register(self):
        self.elements.register.click()
        

