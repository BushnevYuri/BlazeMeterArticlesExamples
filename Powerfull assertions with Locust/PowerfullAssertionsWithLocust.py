import re
from locust import HttpLocust, TaskSet, task
from lxml import html

class BrowseDocumentation(TaskSet):
    HOME_PAGE_TITLE_REGEX = re.compile(".*Welcome to the Simple Travel Agency!.*")
    HOME_PAGE_TITLE_XPATH = "//div[contains(@class, 'jumbotron')]//h1";

    @task
    def index_page_with_regex_assertion(self):
        r = self.client.get("/")
        assert self.HOME_PAGE_TITLE_REGEX.search(r.text) is not None, \
            "Expected title has not been found!"

    @task
    def index_page_with_regex_assertion(self):
        r = self.client.get("/")
        tree = html.fromstring(r.text)
        assert len(tree.xpath(self.HOME_PAGE_TITLE_XPATH)) == 1, \
                     "Expected title has not been found!"

class AwesomeUser(HttpLocust):
    task_set = BrowseDocumentation
    host = "http://blazedemo.com"
    min_wait = 1 * 1000
    max_wait = 5 * 1000