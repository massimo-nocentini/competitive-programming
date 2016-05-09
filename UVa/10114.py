
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=1055

import fileinput

with fileinput.input() as f:

    while True:
        line = next(f).split(' ')
        duration, down_pay, load, depr_nel = int(line[0]), float(line[1]), float(line[2]), int(line[3])
        if duration < 0: 
            break

        deprs = [-1] * duration 
        last = -1 
        for d in range(depr_nel):
            line = next(f).split(' ')
            month, perc = int(line[0]), float(line[1])
            for i in range(last+1, month):
                deprs[i]=deprs[last]
            deprs[month]=perc
            last = month
        for i in range(last+1, len(deprs)):
            deprs[i]=deprs[last]

        print(deprs)
        buyer_owes = load + down_pay
        car_value = load + down_pay
        for month in range(0, duration):
            buyer_owes -= down_pay 
            car_value *= 1 - deprs[month]
            print('buyer: {} car: {}'.format(buyer_owes, car_value))
            if buyer_owes < car_value:
                print('1 month' if month == 1 else '{} months'.format(month))
                break
        else:
            print('buyer: {} car: {}'.format(buyer_owes, car_value))
             



