
def all_on(i): 
    return (1 << i) - 1

def is_on(n, i, return_int=False): 
    res = n & (1 << i)
    return res if return_int else bool(res)

def gray_code(k): 
    g = k ^ (k >> 1)
    return g

def gray_position(g):
    k=0
    for i in reversed(range(g.bit_length())):
        k ^= all_on(i+1) * is_on(g, i)
    return k
