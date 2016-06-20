
from bits import set_all, is_on, toggle_bit

def graycode_unrank(k): 
    """
    Return the *graycode* in position `k` respect binary reflected construction.
    
    Of course, argument `k` should be a *non-negative* integer.

    Examples
    ========

    >>> bin(graycode_unrank(0b101100110))
    '0b111010101'

    """
    g = k ^ (k >> 1)
    return g

def graycode_rank(g):
    """
    Returns the *position* (namely *ranking*) of graycode `g` respect binary reflected construction.

    Examples
    ========

    >>> bin(graycode_rank(0b111010101))
    '0b101100110'

    """
    k=0
    for i in reversed(range(g.bit_length())):
        k ^= set_all(i+1) * is_on(g, i)

    return k

def binary_reflected_graycodes(length=None, justified=False):
    """
    It is a generator of Binary Reflected Gray Codes.

    If keyword `length` is a given integer, than the generator stops
    when it finds the first code exceeding the desired length.

    Moreover, if both keywords `length` and `justified` are truth positive,
    then right justified strings representations of codes are generated.
    
    Examples
    ========

    Generates all codes of length 5:
    >>> [bin(g) for g in binary_reflected_graycodes(5)]
    ['0b0', '0b1', '0b11', '0b10', '0b110', '0b111', '0b101', '0b100', '0b1100', '0b1101', '0b1111', '0b1110', '0b1010', '0b1011', '0b1001', '0b1000', '0b11000', '0b11001', '0b11011', '0b11010', '0b11110', '0b11111', '0b11101', '0b11100', '0b10100', '0b10101', '0b10111', '0b10110', '0b10010', '0b10011', '0b10001', '0b10000']

    Generate right justified representations:
    >>> list(binary_reflected_graycodes(5, justified=True))
    ['0b00000', '0b00001', '0b00011', '0b00010', '0b00110', '0b00111', '0b00101', '0b00100', '0b01100', '0b01101', '0b01111', '0b01110', '0b01010', '0b01011', '0b01001', '0b01000', '0b11000', '0b11001', '0b11011', '0b11010', '0b11110', '0b11111', '0b11101', '0b11100', '0b10100', '0b10101', '0b10111', '0b10110', '0b10010', '0b10011', '0b10001', '0b10000']
         
    """

    from itertools import count

    for c in count():
        g = graycode_unrank(c)
        if length and g.bit_length() > length: 
            raise StopIteration
        yield ('0b' + bin(g)[2:].rjust(length, '0')) if length and justified else g 


def binary_reflected_graycodes_reduce(codes, 
                                      on=lambda p, r: r, 
                                      off=lambda p, r: r, 
                                      redux=None, 
                                      full_tuple=False):
    """
    An *operator* over graycodes which consumes `lambda` expressions to plug bit-changes hooks.

    It consider every codes *pairwise*, computing the position of the (single) changing bit
    among them, and calls callable `on` or `off` if such bit become 1 or 0, respectively;
    moreover, an additional value `redux` is given in order to allow step by step construction
    of a value of interest (it resemble the behavior of `reduce` in the standard library).

    Arguments:
    - `codes` has to be an iterable of graycodes;
    - `on` and `off` should be callable objects which accept:
      - two arguments, the position of the changing bit and the reduced value so far, 
        if argument `full_tuple` is a truth positive;
      - four arguments, two consecutive codes plus position and redux as above, otherwise.
    - `redux` is the initial value for the reducing mechanism, 
      it resembles `initialize` of usual `reduce` function.

    """
    
    from itertools import tee
    #from math import log2, floor

    original, shifted = tee(codes)
    first = next(shifted)

    def changingbit_position(o, s):
        return (o ^ s).bit_length() - 1 # more mathematically: floor(log2(o ^ s))

    for s, o in zip(shifted, original): # since `shifted` is shorter, it appears first in `zip`
                                        # to not consume `original`, necessary for last step
        toggle_position = changingbit_position(o, s)
        t = (o, s, toggle_position, redux) if full_tuple else (toggle_position, redux)
        redux = on(*t) if o < s else off(*t)
        yield (o, s, toggle_position, redux)

    last = next(original) # to be complete, we close the cicle
    yield (last, -1, changingbit_position(last, first), redux)
#_______________________________________________________________________

def graycodes_direct(n):
    """
    Returns an iterable of Gray codes of length `n`, each paired with changing-bit positions.

    """
    code = 0

    def gen(i):
        nonlocal code
        if i > -1:
            yield from gen(i-1)
            code = toggle_bit(code, i)
            yield code, i
            yield from gen(i-1)
             

    yield code, -1
    yield from gen(n-1)


def rightmost_zeroes_in_binary_counting(n):
    """
    I'm a generator of positions of *rightmost zeroes* in binary counting up to `2**n -1`.

    This implements the loopless algorithm designed by Frank Ruskey; it is more
    efficient than natural counting and scanning for rightmost zeroes, which is CAT however.

    Examples
    ========

    Generate the transition sequence to solve the Hanoi tower problem with 3 disks:
    >>> list(rightmost_zeroes_in_binary_counting(3))
    [0, 1, 0, 2, 0, 1, 0]
    
    according to the result, we have to move first disk 0, then disk 1, then disk 0 again,
    then disk 2, next disk 0, next disk 1 and, finally, disk 0; obviously, recipient peg
    is according to the rule of the game.

    """
    tau = list(range(n+1))

    while tau[0] != n:
        yield tau[0]
        i = tau[0]
        tau[0], tau[i], tau[i+1] = 0, tau[i+1], i+1

def graycodes_by_transition_sequence(positions):
    """
    I'm a generator of graycodes, flipping bits according to transitions sequence `positions`.

    """

    graycode = 0

    yield graycode, -1

    for p in positions:
        graycode = toggle_bit(graycode, p)
        yield graycode, p











