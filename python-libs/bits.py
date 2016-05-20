

"""
The following set of functions allows us to use `int` objects as predicates,
namely they represent a set of boolean when we write them in binary.

Consider a predicate over six elements, true for those in position 1 and 5, 
namely the second and last elements, respectively.
>>> 0b100010
34

the other way, with `bin` we can take the set representation as a string object:
>>> bin(34)
'0b100010'

Multiply and divide by powers of 2, it is the same to insert and remove objects from 
the set or, in parallel, discard elements for which the predicate has no more sense:
>>> S = 0b100010
>>> S <<= 1
>>> S, bin(S)
(68, '0b1000100')
>>> S >>= 2
>>> S, bin(S)
(17, '0b10001')

"""


def from_mask(m, coding='big'):
    """
    Returns the integer represented by the bit mask `m`, given in `coding` scheme.

    Keyword argument `coding` represent the coding scheme used by mask `m`, it 
    resembles keyword `byteorder` in function `int.to_bytes`. If it is 'big', then
    a `big endian` scheme has been applied, namely bits at the *beginning* of `m` are the 
    most significant bits of the returned integer; otherwise a `little endian` scheme applies, 
    namely bits at the *end* of the given mask `m` are most significant bits of the
    returned integer.

    Examples
    ========

    >>> from_mask((1,1,0,0), coding='big')
    12

    >>> from_mask((0,0,1,1), coding='little')
    12

    """
    n = 0
    for i, b in enumerate(m if coding == 'little' else reversed(m)):
        n |= b * (1 << i)

    return n


def as_mask(n, coding='big'):
    """
    Returns `n` as a bit mask, namely an iterable of bits, according to `coding` scheme.

    Keyword argument `coding` represent the coding scheme used to build the mask, it 
    resembles keyword `byteorder` in function `int.to_bytes`. If it is 'big', then
    a `big endian` scheme is applied, namely most significant bits of `n` are at 
    the *beginning* of the returned mask; otherwise a `little endian` scheme applies, 
    namely most significant bits of `n` are at the *end* of the returned mask.

    Examples
    ========

    >>> as_mask(12, coding='big')
    (1, 1, 0, 0)

    >>> as_mask(12, coding='little')
    (0, 0, 1, 1)

    """
    m = [is_on(n, i, return_int=True) for i in range(n.bit_length())]
    return tuple(m if coding == 'little' else reversed(m))


def ones_of(S):
    """
    Returns the positions of bits 1 in S, seen as a mask.

    The returned iterable can be interpreted as the set of 
    elements for which *predicate* `S` holds among `S.bit_length()`
    objects; eventually, it identifies a subset.

    Examples
    ========

    >>> ones_of(12)
    [2, 3]

    >>> ones_of(int(0b1000101010))
    [1, 3, 5, 9]

    """

    mask = as_mask(S, coding='little')
    return [i for i, m in enumerate(mask) if m]

def from_ones(ones):
    """
    Returns an integer with bits set to 1 according to positions in `ones`. 

    >>> bin(from_ones([1, 3, 5, 9]))
    '0b1000101010'

    """ 
    n = 0
    for o in ones:
        n = set_bit(n, o)
    return n
    

def set_bit(S, j): 
    """
    Return a new set from set `S` with element in position `j` turned on.

    Examples
    ========

    Set/turn on the 3-th item of the set:
    >>> S = 0b100010
    >>> bin(set_bit(S, 3))
    '0b101010'

    """
    return S | (1 << j)

def is_on(S, j, return_int=False): 
    """
    Returns `True` if the `j`-th item of the set `S` is on.

    Examples
    ========

    Check if the 3-th and then 2-nd item of the set is on:
    >>> S = 0b101010
    >>> is_on(S, 3), is_on(S, 2)
    (True, False)

    """
    res = bool(S & (1 << j))
    return int(res) if return_int else res

def clear_bit(S, j):
    """
    Returns a new set from set `S` with the `j`-th item turned off.

    Examples
    ========

    Clear/turn off item in position 1 of the set:
    >>> S = 0b101010
    >>> bin(clear_bit(S, 1))
    '0b101000'

    """
    return S & ~(1 << j)

def toggle_bit(S, j):
    """
    Returns a new set from set `S` with the j-th item toggled (flip the status of).

    Examples
    ========

    Toggle the 2-nd item and then 3-rd item of the set
    >>> S = int('0b101000', base=2)
    >>> S = toggle_bit(S, 2)
    >>> S = toggle_bit(S, 3)
    >>> bin(S)
    '0b100100'

    """
    return S ^ (1 << j)

def low_bit(S): 
    return S & (-S)

def set_all(n):
    return (1 << n) - 1

def modulo(S, N):
    '''
    Returns S % N, where N is a power of 2
    '''
    return S & (N - 1)

def is_power_of_two(S):
    return False if S & (S - 1) else True

def nearest_power_of_two(S):

    import math
    return math.floor(2**(math.log2(S) + .5))

def turn_off_last_bit(S):
    return S & (S - 1)

def turn_on_last_zero(S): 
    return S | (S + 1)

def turn_off_last_consecutive_bits(S):
    return S & (S + 1)

def turn_on_last_consecutive_zeroes(S):
    return S | (S - 1)

#_______________________________________________________________________

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
    >>> [g for g in gray_codes(5, justified=True)]
    ['0b00000', '0b00001', '0b00011', '0b00010', '0b00110', '0b00111', '0b00101', '0b00100', '0b01100', '0b01101', '0b01111', '0b01110', '0b01010', '0b01011', '0b01001', '0b01000', '0b11000', '0b11001', '0b11011', '0b11010', '0b11110', '0b11111', '0b11101', '0b11100', '0b10100', '0b10101', '0b10111', '0b10110', '0b10010', '0b10011', '0b10001', '0b10000']
         
    """

    from itertools import count

    for c in count():
        g = gray_code(c)
        if length and g.bit_length() > length: 
            raise StopIteration
        yield ('0b' + bin(g)[2:].rjust(length, '0')) if length and justified else g 





