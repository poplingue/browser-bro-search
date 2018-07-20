from locust import HttpLocust, TaskSet


def get(l):
    l.client.get("/search/1?query=typescript")


class UserBehavior(TaskSet):
    tasks = {get: 2}

    def on_start(self):
        get(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
