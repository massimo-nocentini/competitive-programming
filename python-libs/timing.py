
from contextlib import contextmanager

@contextmanager
def timing(f):

    from time import time

    start = time()
    try:
        r = f()
    except Exception as e:
        r = e
    finally:
        end = time()

    yield r, start, end

#________________________________________________________________________
