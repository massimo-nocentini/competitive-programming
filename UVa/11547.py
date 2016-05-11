

import fileinput

with fileinput.input() as f:
    t = int(next(f))
    for i in range(t):
        n = int(next(f))
        print(abs(315*n + 36962) // 10 % 10) # coeffs after simplify steps in the request
