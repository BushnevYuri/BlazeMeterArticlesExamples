from locust import HttpLocust, TaskSet, task
import logging, sys

USER_CREDENTIALS = [
    ("LocustPerformanceUser5@gmail.com", "5678901"),
    ("LocustPerformanceUser4@gmail.com", "456789"),
    ("LocustPerformanceUser3@gmail.com", "345678"),
    ("LocustPerformanceUser2@gmail.com", "234567"), 
    ("LocustPerformanceUser1@gmail.com", "123456")
]

class LoginWithUniqueUsersSteps(TaskSet):
    email = "NOT_FOUND"
    password = "NOT_FOUND"

    def on_start(self):
            if len(USER_CREDENTIALS) > 0:
                self.email, self.password = USER_CREDENTIALS.pop()

    @task
    def login(self):
        self.client.post("/login", {
            'email': self.email, 'passowrd': self.password
        })
        logging.info('Login with %s email and %s password', self.email, self.password)

class LoginWithUniqueUsersTest(HttpLocust):
    task_set = LoginWithUniqueUsersSteps
    host = "http://blazedemo.com"
    sock = None

    def __init__(self):
        super(LoginWithUniqueUsersTest, self).__init__()
