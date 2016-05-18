
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

def dispatch(*args, table, default=lambda k, e: k):
    '''
    Dispatch behavior in *even* positions within `args` against mapping `table`.

    It accepts a variable list of arguments, however of even length, where
    *hashable* objects in *even* positions are used in the key for dispatching against
    logic container `table`, namely a mapping of functions; in parallel, objects
    in *odd* positions within `args` are used as values, respectively.

    Keyword argument `default` is a function that consumes two arguments:
    the former is the key not found in the dispatch `table`; the latter one
    is the caught exception, if re-raising would be performed. Its default
    behavior is to return the key as it is.
    '''
    key = tuple([args[e] for e in range(0, len(args), 2)])
    values = [args[o] for o in range(1, len(args), 2)]
    try:
        method = table[key]
        return method(*values)
    except KeyError as e:
        return default(key, e)
#________________________________________________________________________

with stdin_input() as f:

    with line_bind(next(f), int) as (n,):

        stacks = [[i] for i in range(n)]
        positions = {i:(i,0) for i in range(n)}

        def restore(*args):
            for arg in args:
                s, i = positions[arg]
                stack = stacks[s]
                while stack[i+1:]:
                    j = stack.pop()
                    stacks[j].append(j)
                    positions[j] = j, len(stacks[j])-1

        def do(take, to):
            take_s, take_i = positions[take]
            to_s, to_i = positions[to]
            source, dest = stacks[take_s], stacks[to_s]
            length = len(dest)
            dest.extend(source[take_i:])
            del source[take_i:] 
            for i in range(length, len(dest)):
                positions[dest[i]] = to_s, i   

        methods = { ('move', 'onto'): lambda a,b: restore(a, b),
                    ('move', 'over'): lambda a,b: restore(a),
                    ('pile', 'onto'): lambda a,b: restore(b),
                    ('pile', 'over'): lambda a,b: ..., }
        
        while True:
            
            line = next(f).strip()

            if line == 'quit': break

            with line_bind(line, str, int, str, int) as (act, a, placing, b):

                if a == b or positions[a][0] == positions[b][0]: continue

                dispatch(act, a, placing, b, table=methods)
                do(take=a, to=b)

        for i, s in enumerate(stacks):
            print("{}:{}{}".format(i, " " if s else "", " ".join(map(str, s))))





