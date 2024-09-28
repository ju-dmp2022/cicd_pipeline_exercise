from locust import HttpUser, task, constant, tag
import random
import json

class CalculatorUser(HttpUser):
    
    wait_time = constant(2)

    def on_start(self):
        pass

    @task
    @tag('add')
    def add(self):
        data = [[1, 2, 3], [2, 5, 7]]
        data_insertion = random.choice(data)
        add = {
            "operation": "add",
            "operand1": data_insertion[0], 
            "operand2": data_insertion[1]
        }
        
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == data_insertion[2]:
                response.failure(f"Expected result to be 2 but was {response_data['result']}")
         
    @task    
    @tag('subtract')   
    def subtract(self):
        subtract = {
            "operation": "subtract",
            "operand1": 1, 
            "operand2": 1
        }
        
        with self.client.post("/calculate", catch_response=True, name='subtract', json=subtract) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 0:
                response.failure(f"Expected result to be 0 but was {response_data['result']}")

if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
