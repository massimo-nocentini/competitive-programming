
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=2307

# ___declarations in `utilities.py`___
# do update in `utilities.py` if you do any change

import fileinput
from contextlib import contextmanager

@contextmanager
def line_bind(line, *args, splitter=' '):
    yield (c(v) for c, v in zip(args, line.split(splitter)))

@contextmanager
def stdin_input():
    yield fileinput.input()
#_________________________________________________________________________

with stdin_input() as f:
    
    while True:

        with line_bind(next(f), int) as (n,):

            if not n: break

            while len(str(n)) > 1:
                n = sum(map(int, str(n)))

            print(n)
