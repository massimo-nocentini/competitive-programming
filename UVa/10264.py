
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

def forever_read_until_event(doer, reader=lambda: stdin_input(), event=StopIteration):
    '''
    Runs forever a `doer` function reading a source, until an event happens.

    An iterable, provided by the `reader` thunk, is read infinitely until `event`
    is raised. By defaults, `reader` reads from standard input and `event` is `StopIteration`.
    '''
    with reader() as f:
        while True:
            try: doer(f)
            except event: break

#________________________________________________________________________

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
#________________________________________________________________________


def doer(next_line):
    
    with line_bind(next_line(), int) as (n,):

        weights = []
        for i in range(1 << n):
            with line_bind(next_line(), int) as (w,): 
                weights.append(w)

        potencies = []
        neighbours = []
        for i in range(len(weights)):
            s = 0
            i_neighbours = []
            for j in range(n):
                neigh = toggle_bit(i, j)
                i_neighbours.append(neigh)
                s += weights[neigh]
            neighbours.append(i_neighbours)
            potencies.append(s)     

        pot = -1
        for p, neighs in zip(potencies, neighbours):
            pot = max(pot, *[p + potencies[neigh] for neigh in neighs])

        # the following is the exploded version, a bit redundant:
        # with the above code we avoid to redo bitwise toggling for finding neighbours.
        #for i in range(len(weights)):
            #for j in range(n):
                #pot = max(pot, potencies[i] + potencies[toggle_bit(i, j)]) 
        
        print(pot)

forever_read_until_event(doer)

