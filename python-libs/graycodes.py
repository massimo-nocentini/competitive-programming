
from bits import set_all, is_on

def gray_code(k): 
    """

    Examples
    ========

    >>> bin(gray_code(0b101100110))
    '0b111010101'

    """
    g = k ^ (k >> 1)
    return g

def gray_position(g):
    """

    Examples
    ========

    >>> bin(gray_position(0b111010101))
    '0b101100110'

    """
    k=0
    for i in reversed(range(g.bit_length())):
        k ^= set_all(i+1) * is_on(g, i)
    return k

def gray_codes(length=None, justified=False):
    """
    It is a generator of Gray codes, in particular reflected binary.

    If keyword `length` is a given integer, than the generator stops
    when it finds the first code exceeding the desired length.

    Moreover, if both keywords `length` and `justified` are truth positive, 
    then right justified strings representations of codes are generated.
    
    Examples
    ========

    Generates all codes of length 5:
    >>> [bin(g) for g in gray_codes(5)]
    ['0b0', '0b1', '0b11', '0b10', '0b110', '0b111', '0b101', '0b100', '0b1100', '0b1101', '0b1111', '0b1110', '0b1010', '0b1011', '0b1001', '0b1000', '0b11000', '0b11001', '0b11011', '0b11010', '0b11110', '0b11111', '0b11101', '0b11100', '0b10100', '0b10101', '0b10111', '0b10110', '0b10010', '0b10011', '0b10001', '0b10000']

    Generate right justified representations:
    >>> list(gray_codes(5, justified=True))
    ['0b00000', '0b00001', '0b00011', '0b00010', '0b00110', '0b00111', '0b00101', '0b00100', '0b01100', '0b01101', '0b01111', '0b01110', '0b01010', '0b01011', '0b01001', '0b01000', '0b11000', '0b11001', '0b11011', '0b11010', '0b11110', '0b11111', '0b11101', '0b11100', '0b10100', '0b10101', '0b10111', '0b10110', '0b10010', '0b10011', '0b10001', '0b10000']
         
    """

    from itertools import count

    for c in count():
        g = gray_code(c)
        if length and g.bit_length() > length: 
            raise StopIteration
        yield ('0b' + bin(g)[2:].rjust(length, '0')) if length and justified else g 


def high(codes, on, off, redux, full_tuple=False):
    
    from itertools import tee
    from math import log2, floor

    original, shifted = tee(codes)
    first = next(shifted)

    for o, s in zip(original, shifted):
        toggle_position = floor(log2(o ^ s))
        t = (o, s, toggle_position, redux) if full_tuple else (toggle_position, redux)
        redux = on(*t) if o < s else off(*t)
        yield (o, s, toggle_position, redux)


#_______________________________________________________________________
