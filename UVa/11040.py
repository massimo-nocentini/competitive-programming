
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

    with line_bind(next_line(), int) as (n,):
    
        for _ in range(n):
            
            matrix, r = {}, 1

            for i in range(1, 6):
                c = 1
                with line_bind(next_line(), *([int] * i)) as coeffs:
                    for coeff in coeffs: 
                        matrix[r,c] = coeff
                        if c > 1 and r > 1:
                            matrix[r, c-1] = (matrix[r-2, c-2]-matrix[r,c-2]-matrix[r,c]) >> 1  
                            matrix[r-1, c-2] = matrix[r, c-2] + matrix[r, c-1]
                            matrix[r-1, c-1] = matrix[r, c-1] + matrix[r, c]
                        c += 2
                    r += 2

            for r in range(1, 10):
                print(' '.join(map(str, [matrix[r,c] for c in range(1, r+1)])))
            
                






