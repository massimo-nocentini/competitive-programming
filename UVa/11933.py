
import fileinput
from contextlib import contextmanager

@contextmanager
def line_bind(line, *ctors, splitter=lambda l: l.split(' '), do=None):
    '''
    Split `line` argument producing an iterable of mapped elements, in the sense of `ctors`.

    Keyword argument `splitter` splits the given `line` respect `space` (' ')
    character; however, it is possible to provide the desired behavior providing
    a custom lambda expression of one parameter, eventually instantiated with `line`.
    The iterable produced by `splitter` should match argument `ctors` in length;
    if this holds, an iterable of mapped elements is produced, composed of elements
    built by application of each function in `ctors` to element in the split, pairwise.
    On the other hand, mapping happens according to the rules of `zip` if lengths differ.

    Keyword argument `do` is an higher order operator, defaults to `None`: if
    given, it should be a function that receive the generator, which is returned, otherwise.

    Moreover, the returned iterable object is a generator, so a linear scan of the line
    *is not* performed, hence there is no need to consume an higher order operator to
    be applied during the scan, this provide good performances at the same time.
    '''
    g = (c(v) for c, v in zip(ctors, splitter(line)))
    yield do(g) if do else g

@contextmanager
def stdin_input(getter=lambda: fileinput.input(), raw_iter=False):
    '''
    Produces a way to fetch lines by a source.

    Keyword argument `getter` should be a thunk that produces an iterable, call it `i`;
    by default, it produces the iterator which reads from standard input.

    Keyword argument `raw_iter` is a boolean. If it is `True`, that iterator `i` is 
    returned as it is; otherwise, a thunk is returned which wraps the application `next(i)`.
    '''
    iterable = getter()
    yield iterable if raw_iter else (lambda: next(iterable))

#________________________________________________________________________

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
    m = map(int, bin(n)[2:])
    return tuple(m if coding == 'big' else reversed(list(m)))

def ones(S):
    """
    Returns the positions of bits 1 in S, seen as a mask.

    The returned iterable can be interpreted as the set of 
    elements for which *predicate* `S` holds among `S.bit_length()`
    objects; eventually, it identifies a subset.

    Examples
    ========

    >>> ones(12)
    [2, 3]

    >>> ones(int(0b1000101010))
    [1, 3, 5, 9]

    """

    mask = as_mask(S, coding='little')
    return [i for i, m in enumerate(mask) if m]

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

#________________________________________________________________________


with stdin_input() as next_line:

    while True:

        with line_bind(next_line(), int) as (n,):

            if not n: break
            
            a, b = 0, 0
            for i, m in enumerate(ones(n)):
                a, b = (a, set_bit(b, m)) if i % 2 else (set_bit(a, m), b)
                #print("{} {}".format(a, b))

            print("{} {}".format(a, b))
    
    
    
    
    
    
    
            
