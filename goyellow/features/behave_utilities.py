from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


def wait_for(fun):
    start_time = time.time()
    while True:
        try:
            return fun()
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)


def wait_for_database_update(fun):
    start_time = time.time()
    while True:
        try:
            return fun()
        except AttributeError as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
