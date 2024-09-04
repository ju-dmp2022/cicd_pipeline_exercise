import logging   #check readme file for more info
import os        #check readme file for more info

# Global logger configuration
log_file = 'BE/information.log'
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(message)s')

def configure_logging(log_file):
    """Configure logging for the application."""
    
    # Ensure the directory exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set root logger level to DEBUG

    # File handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode='w')  # 'w' mode to overwrite file each time
    file_handler.setLevel(logging.DEBUG)  # Set level for file handler
    file_handler.setFormatter(formatter)

    # Stream handler for logging to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


configure_logging(log_file)

class CalculatorHelper:
    log_properties = {
        'custom_dimensions': {
            'userId': 'ali_kouravand'
        }
    }

    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._user_list = []
            self._current_user = None
            admin = self.User('admin', 'test1234')
            self._user_list.append(admin)
            self._is_initialized = True
            self.logger = logging.getLogger(__name__)

    class User:
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            self.logger.exception('Tried division by zero')
        else:
            return result

def perform_and_log_calculations(calculator, a, b):
    """Perform calculations and log the results in information.log you create with the script."""
    
    add_result = calculator.add(a, b)
    calculator.logger.debug('add: {} + {} = {}'.format(a, b, add_result))

    sub_result = calculator.subtract(a, b)
    calculator.logger.debug('sub: {} - {} = {}'.format(a, b, sub_result))

    multi_result = calculator.multiply(a, b)
    calculator.logger.debug('multiply: {} * {} = {}'.format(a, b, multi_result))

    div_result = calculator.divide(a, b)
    calculator.logger.debug('divide: {} / {} = {}'.format(a, b, div_result))

# Create an instance of CalculatorHelper
calculator = CalculatorHelper()

# set the values of numbers which we want to calculate
number_a = 49
number_b = 0

# Perform calculations and log the results
perform_and_log_calculations(calculator, number_a, number_b)
