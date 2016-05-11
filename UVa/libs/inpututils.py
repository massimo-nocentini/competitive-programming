
# ___declarations in `utilities.py`___
# do update in `utilities.py` if you do any change
#_________________________________________________________________________

import fileinput
from contextlib import contextmanager

@contextmanager
def line_bind(line, *ctors, splitter=lambda l: l.split(' ')):
    '''
    Split `line` argument producing an iterable of mapped elements, in the sense of `ctors`.

    Keyword argument `splitter` splits the given `line` respect `space` (' ')
    character; however, it is possible to provide the desired behavior providing
    a custom lambda expression of one parameter, eventually instantiated with `line`.
    The iterable produced by `splitter` should match argument `ctors` in length;
    if this holds, an iterable of mapped elements is produced, composed of elements
    build by application of each function in `ctors` to element in the split, pairwise.
    On the other hand, mapping happens according to the rules of `zip` if lengths differ.
    '''
    yield (c(v) for c, v in zip(ctors, splitter(line)))

@contextmanager
def stdin_input(getter=lambda: fileinput.input(), raw_iter=True):
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
