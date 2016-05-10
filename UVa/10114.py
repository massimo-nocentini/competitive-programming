
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=1055

import collections
import fileinput
from contextlib import contextmanager

@contextmanager
def line_bind(line, *args, splitter=' '):
    yield (c(v) for c, v in zip(args, line.split(splitter)))

with fileinput.input() as f:

    while True:

        with line_bind(next(f), int, float, float, int) as (duration, down_pay, loan, depr_nel):

            if duration < 0: break

            deprs = [0] * (duration + 1)
            last = -1 
            for d in range(depr_nel):
                with line_bind(next(f), int, float) as (month, perc):
                    for i in range(last+1, month): deprs[i]=deprs[last]
                    deprs[month], last = perc, month
            for i in range(last+1, len(deprs)):
                deprs[i]=deprs[last]

            buyer_owes, payment = loan, loan / duration
            car_value = (loan + down_pay) * (1 - deprs[0])

            if loan < car_value:
                print('0 months')
                continue

            for month in range(1, len(deprs)):
                buyer_owes -= payment 
                car_value -= car_value*deprs[month]
                #print('month: {} buyer: {} car: {}'.format(
                    #month, buyer_owes, car_value))
                if buyer_owes < car_value: 
                    break

            print('{} month{}'.format(month, '' if month == 1 else 's'))



