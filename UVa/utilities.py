
# ___declarations in `utilities.py`___
# do update in `utilities.py` if you do any change
#_________________________________________________________________________

import fileinput
from contextlib import contextmanager

@contextmanager
def line_bind(line, *args, splitter=' '):
    yield (c(v) for c, v in zip(args, line.split(splitter)))

@contextmanager
def stdin_input():
    yield fileinput.input()

def forever_read_until_event(fn, event=StopIteration):
    with stdin_input() as f:
        while True:
            try: fn(f)
            except event: break





