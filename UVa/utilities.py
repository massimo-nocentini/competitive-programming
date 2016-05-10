
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

#________________________________________________________________________

# Look at [1] and [2]:
# [1]:http://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not
# [2]:http://stackoverflow.com/questions/12734178/determine-if-a-list-is-in-descending-order

def is_non_increasing(l):
    for i, el in enumerate(l[1:], start=1):
        if el >= l[i-1]: return False
    return True

def is_non_decreasing(l):
    return all(x <= y for x,y in zip(l, l[1:]))





