import signal
from contextlib import contextmanager
from itertools import cycle

from django.test import TestCase
from model_bakery import baker

from issues.models import Issue, Task


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException()

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


class ORMTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        issue_set = baker.make(Issue, _quantity=10000)
        root_task_set = baker.make(Task, issue=cycle(issue_set), _quantity=10000)
        baker.make(Task, issue=cycle([task.issue for task in root_task_set]), parent=cycle(root_task_set), _quantity=20000)

    def test_issue_query(self):
        pass
