
#_________________________________________________________________________

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

    Moreover, the returned iterable object is a generator, so a linear scan of the line
    *is not* performed, hence there is no need to consume an higher order operator to
    be applied during the scan, this provide good performances at the same time.
    '''
    g = (c(v) for c, v in zip(ctors, splitter(line)))
    yield do(g) if do else g

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

#________________________________________________________________________

with stdin_input(raw_iter=False) as next_line:
    with line_bind(next_line(), int) as (tests,):
        for t in range(1, tests+1):
            with    line_bind(next_line(), int) as (n,),\
                    line_bind(next_line(), *([int] * n), do=list) as ps,\
                    line_bind(next_line(), *([int] * n), do=list) as qs:
                for i in range(n):
                    gallons = 0
                    for j in range(n):
                        index = (i+j)%n
                        gallons += ps[index]-qs[index] 
                        if gallons < 0:
                            break
                    else:
                        print("Case {}: Possible from station {}".format(t, i+1))
                        break
                else:
                    print("Case {}: Not possible".format(t))




