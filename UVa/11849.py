

import fileinput
from contextlib import contextmanager
from heapq import heappop

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

with stdin_input(raw_iter=True) as next_line:

    while True:
            
        line = next(next_line).split(' ')
        n, m = map(int, line)

        if not n and not m: break

        jack = [int(next(next_line)) for _ in range(n)] # it is already a heap
        
        commons = 0
        for _ in range(m): 

            j = int(next(next_line)) 

            while jack and jack[0] < j: heappop(jack)

            if not jack: 
                break

            commons += (j == jack[0])

        print(commons)


