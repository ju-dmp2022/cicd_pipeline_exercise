from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'screen': Element('//input[@id="calculator-screen"]', self),
            'add': Element('//button[@id="key-add"]', self),
            'subtract': Element('//button[@id="key-subtract"]', self),
            'multiply': Element('//button[@id="key-multiply"]', self),
            'divide': Element('//button[@id="key-divide"]', self),
            'equals': Element('//button[@id="key-equals"]', self),
            'history_button': Element('//button[@id="toggle-button"]', self),
            'history': Element('//textarea[@id="history"]', self),
            'username': Element('//label[@id="user-name"]', self),
            'logout': Element('//button[@id="logout-button"]', self)
        }

        self.elements = munchify(self.page_elements)

    # For the number buttons
        for i in range(0, 10):
            self.page_elements[f'key-{i}'] = Element(f'//button[@id="key-{i}"]', self)

        self.elements = munchify(self.page_elements)

    def perform_operation(self, operation, operand1, operand2):
        # Set operand1 and operand2 by clicking the number buttons
        for digit in str(operand1):
            self.elements[f'key-{digit}'].click()

        if operation == 'add':
            self.elements.add.click()
        elif operation == 'subtract':
            self.elements.subtract.click()
        elif operation == 'multiply':
            self.elements.multiply.click()
        elif operation == 'divide':
            self.elements.divide.click()

     
        for digit in str(operand2):
            self.elements[f'key-{digit}'].click()

     
        self.elements.equals.click()

    def open_history(self):
        self.elements.history_button.click()

    def get_history(self):
        return self.elements.history.value

    def get_result(self):
        return self.elements.screen.value
    
    def logout(self):
        self.elements.logout_button.click() 