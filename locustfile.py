from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(2)
    def hello_world(self):
        self.client.get('http://localhost:5000')
