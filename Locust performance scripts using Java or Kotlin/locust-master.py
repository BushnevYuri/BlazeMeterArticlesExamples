from locust import Locust, TaskSet, task

class DummyTask(TaskSet):
    @task(1)
    def dummy(self):
        pass

class Dummy(Locust):
    task_set = DummyTask