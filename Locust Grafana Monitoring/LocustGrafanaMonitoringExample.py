from locust import HttpLocust, TaskSet, task
import locust.events
import time
import socket
import atexit

class FlightSearchTest(TaskSet):
    @task
    def open_login_page(self):
        self.client.get("/login")

    @task
    def find_flight_between_Paris_and_Buenos_Aires(self):
        self.client.post("/reserve.php", {
            'fromPort': 'Paris', 'toPort': 'Buenos+Aires'
        })

    @task
    def purchase_flight_between_Paris_and_Buenos_Aires(self):
        self.client.post("/purchase.php", {
            'fromPort': 'Paris', 'toPort': 'Buenos+Aires',
            'airline': 'Virgin+America','flight': 43,
            'price': 472.56
        })

class MyLocust(HttpLocust):
    task_set = FlightSearchTest
    host = "http://blazedemo.com"
    sock = None

    def __init__(self):
        super(MyLocust, self).__init__()
        self.sock = socket.socket()
        self.sock.connect( ("localhost", 2003) )
        locust.events.request_success += self.hook_request_success
        locust.events.request_failure += self.hook_request_fail
        atexit.register(self.exit_handler)


    def hook_request_success(self, request_type, name, response_time, response_length):
        self.sock.send("%s %d %d\n" % ("performance." + name.replace('.', '-'), response_time,  time.time()))

    def hook_request_fail(self, request_type, name, response_time, exception):
        self.request_fail_stats.append([name, request_type, response_time, exception])

    def exit_handler(self):
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()