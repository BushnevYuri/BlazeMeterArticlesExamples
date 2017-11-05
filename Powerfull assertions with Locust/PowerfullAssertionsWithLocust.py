import re
from locust import HttpLocust, TaskSet, task

class BrowseDocumentation(TaskSet):
    HOME_PAGE_TITLE_REGEX = re.compile(".*Welcome to the Simple Travel Agency!.*")

    @task(10)
    def index_page_with_regex_assertion(self):
        r = self.client.get("/")
        assert self.HOME_PAGE_TITLE_REGEX.search(r.text) is not None, \
            "Expected title has not been found!"

class AwesomeUser(HttpLocust):
    task_set = BrowseDocumentation
    host = "http://blazedemo.com"
    min_wait = 1 * 1000
    max_wait = 5 * 1000