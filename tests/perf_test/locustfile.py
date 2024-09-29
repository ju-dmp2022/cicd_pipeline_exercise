from locust import HttpUser, task, between, tag
import random
import json
import logging
import time


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CalculatorUser(HttpUser):
    """use 3rd party library locust elements to make execute Load tests for the /calculate endpoint"""
    # time_data = [2, 3, 4]
    # chosen_time_to_wait = random.choice(time_data)
    wait_time = between(2, 4)   

    def on_start(self):
        logging.info("Starting a new user session.")

    @task
    @tag('add')
    def add(self):
        """take the payload and make a addition post requests twice using the for-loop and log the result & execution-time"""
        data = [[1, 2, 3], [2, 5, 7]]
        
            
        for _ in range(2):
            
            data_insertion = random.choice(data)
            add = { # this is actually where i will lose in performance but it wont affect the real application because these are just test and they are for me to learn
                    "operation": "add",
                    "operand1": data_insertion[0], 
                    "operand2": data_insertion[1]
            }
            start_time = time.time() # Start timing the req
            with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
                response_time = time.time() - start_time # Calculate response time
                response_data = json.loads(response.text)
                
                logging.info(f"Response time for add operation: {response_time:.2f}s")
                
                if response_data['result'] != data_insertion[2]:
                    response.failure(f"Expected result to be {data_insertion[2]} but was {response_data['result']}")
                    logging.error(f"Add operation failed: Expected {data_insertion[2]}, got {response_data['result']}")
                else:
                    logging.info(f"Add operation succeeded: {data_insertion[0]} + {data_insertion[1]} = {response_data['result']}")
                    
                
    
         
    @task    
    @tag('subtract')   
    def subtract(self):
        """take the payload and make a subtraction post requests and log the result & execution-time"""
        data = [[1, 2, -1], [13, 5, 8]]
        data_insertion = random.choice(data)
        subtract = {
            "operation": "subtract",
            "operand1": data_insertion[0], 
            "operand2": data_insertion[1]
        }
        start_time = time.time()  # Start timing the req
        with self.client.post("/calculate", catch_response=True, name='subtract', json=subtract) as response:
            response_time = time.time() - start_time
            response_data = json.loads(response.text)
            
            logging.info(f"Response time for subtract operation: {response_time:.2f}s")
            
            if response_data['result'] != data_insertion[2]:
                response.failure(f"Expected result to be {data_insertion[2]} but was {response_data['result']}")
                logging.error(f"Subtract operation failed: Expected {data_insertion[2]}, got {response_data['result']}")
            else:
                logging.info(f"Subtract operation succeeded: {data_insertion[0]} - {data_insertion[1]} = {response_data['result']}")
                
    @task    
    @tag('multiply') 
    
    def multi(self):
        data = [[1, 2, 2], [3, 5, 15]]
        data_insertion = random.choice(data)
        multi = {
            "operation": "multiply",
            "operand1": data_insertion[0], 
            "operand2": data_insertion[1]
        }
        
        with self.client.post("/calculate", catch_response=True, name='multiply', json=multi) as response:
            response_data = json.loads(response.text)
            if response_data['result'] != data_insertion[2]:
                response.failure(f"Expected result to be {data_insertion[2]} but was {response_data['result']}")
                
    @task    
    @tag('divide')   
    
    def divide(self):
        data = [[9, -3, -3], [15, 5, 3]]
        data_insertion = random.choice(data)
        division = {
            "operation": "divide",
            "operand1": data_insertion[0], 
            "operand2": data_insertion[1]
        }
        
        with self.client.post("/calculate", catch_response=True, name='divide', json=division) as response:
            response_data = json.loads(response.text)
            if response_data['result'] != data_insertion[2]:
                response.failure(f"Expected result to be {data_insertion[2]} but was {response_data['result']}")
                
                

if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
