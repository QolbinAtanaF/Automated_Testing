from locust import HttpUser, task, between

class QuickTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_root(self):
        response = self.client.get("/")
        print(response.status_code)