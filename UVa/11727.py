

import fileinput

with fileinput.input() as f:
    t = int(next(f))
    for i in range(t):
        line = next(f)
        a, b, c = sorted(map(int, line.split(' ')))
        print('Case {}: {}'.format(i+1, b))
