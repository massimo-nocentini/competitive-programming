

import fileinput

with fileinput.input() as f:
    t = int(next(f))
    for line in f:
        a, b = map(int, line.split(' '))
        print('<' if a < b else ('>' if a > b else '='))

        
