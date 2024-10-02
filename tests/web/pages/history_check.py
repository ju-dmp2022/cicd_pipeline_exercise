from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class HistoryCheck(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)
        

        self.page_elements = {
            #credentials
            'username': Element('//*[@id="username"]', self),
            'password': Element('//*[@id="password"]', self),
            
            #log in & out
            'login': Element('//*[@id="login"]', self),
            'logout': Element('//*[@id="logout-button"]', self),
            
            #methods
            'add': Element('//*[@id="key-add"]', self),
            'sub': Element('//*[@id="key-subtract"]', self),
            'div': Element('//*[@id="key-divide"]', self),
            'multi': Element('//*[@id="key-multiply"]', self),
            'sum': Element('//*[@id="key-equals"]', self),
            
            # values
            'choice1': Element('//*[@id="key-6"]', self),
            'choice2': Element('//*[@id="key-2"]', self),
            
            #calculate value check
            'result': Element('//*[@id="calculator-screen"]', self) 
        }
        self.elements = munchify(self.page_elements)


