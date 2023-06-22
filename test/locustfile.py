import json
from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_workflow(self):
        # Step 1: Make a request with a JSON payload
        payload = {"input": {"prompt": "a picture of a women in the red dress"}}
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer R2Q5CV66I43LLYTAKU98NMNVRZSW5D9M2O3XHQ4T"
            }
        response = self.client.post("/v2/cpkvel2irtq8l7/runsync", data=json.dumps(payload), headers=headers)

        response_json = response.json()
        print(response_json)