
# ___declarations in `utilities.py`___
# do update in `utilities.py` if you do any change
#_________________________________________________________________________

import fileinput
from contextlib import contextmanager

@contextmanager
def line_bind(line, *args, splitter=' '):
    yield (c(v) for c, v in zip(args, line.split(splitter)))

@contextmanager
def stdin_input(raw_iter=True):
    fi = fileinput.input()
    yield fi if raw_iter else (lambda: next(fi))
#_________________________________________________________________________

with stdin_input(raw_iter=False) as next_line:

    with line_bind(next_line(), int) as (n,):
        
        print('Lumberjacks:') 
        types = [int] * 10

        for _ in range(n):

            with line_bind(next_line(), *types) as (a, b, c, d, e, f, g, h, i, j):

                asc = a < b < c < d < e < f < g < h < i < j
                # former `asc` bypass `des` computation if already ascending ordered
                des = asc or a > b > c > d > e > f > g > h > i > j
                
                print('Ordered' if asc or des else 'Unordered')
                    



