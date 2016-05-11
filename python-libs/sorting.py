
# Look at [1] and [2]:
# [1]:http://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not
# [2]:http://stackoverflow.com/questions/12734178/determine-if-a-list-is-in-descending-order

def is_non_increasing(l):
    for i, el in enumerate(l[1:], start=1):
        if el >= l[i-1]: return False
    return True

def is_non_decreasing(l):
    return all(x <= y for x,y in zip(l, l[1:]))





#________________________________________________________________________

