

import fileinput

with fileinput.input() as f:
    while True:
        t = int(next(f))
        if t == 0: break

        x, y = map(int, next(f).split(' '))
        for i in range(t):
            line = next(f)
            a, b = map(int, line.split(' '))
            if a == x or b == y: print('divisa')
            elif a > x: print('NE' if b > y else 'SE')
            else: print('NO' if b > y else 'SO')

