import re
from locust import HttpLocust, TaskSet, task
from lxml import html

class BrowseDocumentation(TaskSet):
    HOME_PAGE_TITLE_REGEX = re.compile(".*Welcome to the Simple Travel Agency!.*")
    HOME_PAGE_TITLE_XPATH = "//h1[contains(text(),'Welcome to the Simple Travel Agency!')]";
    HOME_PAGE_TITLE_CSS = ".jumbotron h1";

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

    @task
    def index_page_with_css_assertion(self):
        r = self.client.get("/")
        tree = html.fromstring(r.text)
        assert len(tree.cssselect(self.HOME_PAGE_TITLE_CSS)) == 1, \
            "Title element is not unique"
        assert tree.cssselect(self.HOME_PAGE_TITLE_CSS)[0].text == "Welcome to the Simple Travel Agency!", \
            "Expected title has not been found!"

class AwesomeUser(HttpLocust):
    task_set = BrowseDocumentation
    host = "http://blazedemo.com"
    min_wait = 1 * 1000
    max_wait = 5 * 1000