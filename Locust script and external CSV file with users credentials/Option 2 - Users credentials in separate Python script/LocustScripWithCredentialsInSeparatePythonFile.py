from credentials import *
from locust import HttpUser, TaskSet, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://www.microsoft.com"

    @task
    def main_page(self):
        self.client.get("/")
        #print("task created.")
        
        print("login by: ", self.email, " password: ", self.password )
        self.stop()


    def on_start(self):
        #print("Job started")
        if len(USER_CREDENTIALS) > 0:
            self.email, self.password = USER_CREDENTIALS.pop()
        else:
            self.email = "NO_MORE_USER"
            self.password = "N/A"
