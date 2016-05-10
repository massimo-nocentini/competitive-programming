
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=608&page=show_problem&problem=1055

import fileinput

with fileinput.input() as f:

    while True:
        line = next(f).split(' ')
        duration, down_pay, load, depr_nel = int(line[0]), float(line[1]), float(line[2]), int(line[3])
        if duration < 0: 
            break

        buyer_owes = load
        line = next(f).split(' ')
        off_lot, off_lot_perc = int(line[0]), float(line[1])
        car_value = (load + down_pay) * (1 - off_lot_perc)

        deprs = [off_lot_perc] + ([0] * duration)
        last = 0 
        for d in range(depr_nel-1):
            line = next(f).split(' ')
            month, perc = int(line[0]), float(line[1])
            for i in range(last+1, month):
                deprs[i]=deprs[last]
            deprs[month]=perc
            last = month
        for i in range(last+1, len(deprs)):
            deprs[i]=deprs[last]
        deprs[0] = off_lot_perc

        #print(deprs)
        for month in range(1, len(deprs)):
            buyer_owes -= down_pay 
            car_value *= 1 - deprs[month]
            print('buyer: {} car: {}'.format(buyer_owes, car_value))
            if buyer_owes < car_value: 
                break

        print('{} month{}'.format(month, '' if month == 1 else 's'))



