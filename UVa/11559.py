
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=2595

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

        try:

            inf = float("+inf")
            cheaper = inf 

            with line_bind(next(f), int, int, int, int) as (n, b, h, w):

                for _ in range(h):

                    with line_bind(next(f), int) as (p,), \
                         line_bind(next(f), *([int] * w)) as beds:

                        cost = n * p

                        if cost > b or all(map(lambda bs: n > bs, beds)): continue
                        
                        cheaper = min(cheaper, cost)

            print("stay home" if cheaper == inf else str(cheaper))

        except StopIteration as e: break





