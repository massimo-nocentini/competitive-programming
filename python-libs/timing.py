
from contextlib import contextmanager
from time import time
from datetime import timedelta

@contextmanager
def timing(f):

    start = time()
    try:
        r = f()
    except Exception as e:
        r = e
    finally:
        end = time()

    yield r, timedelta(seconds=end-start)

#________________________________________________________________________
