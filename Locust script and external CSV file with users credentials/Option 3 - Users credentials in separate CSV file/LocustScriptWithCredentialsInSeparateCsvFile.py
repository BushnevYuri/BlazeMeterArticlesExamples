import time
import random
import logging, sys
import csv
from locust import HttpUser, TaskSet, task, between

# Global variable to load test data from csv
USER_CREDENTIALS = None

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://www.microsoft.com"

    @task
    def main_page(self):
        self.client.get("/")
        
        # Check Mobile number to use for login
        if (self.mobile == "NO_MORE_USER"):
            print("NO MORE MOBILE")
        else:
            print("Mobile number: ", self.mobile, " otp: ", self.otp )
        self.stop()

    def on_start(self):
        global USER_CREDENTIALS

        # Load test data from csv file
        if (USER_CREDENTIALS == None):
            print("open file")
            with open('credentials.csv', 'r') as f:
                reader = csv.reader(f)
                USER_CREDENTIALS = list(reader)
        
        # Load top record from dataset and mark for processed
        if len(USER_CREDENTIALS) > 0:
            self.mobile, self.otp = USER_CREDENTIALS.pop()
        else:
            self.mobile = "NO_MORE_MOBILE"
            self.otp = "N/A"
