
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

with stdin_input() as f:

    with line_bind(next(f), int) as (n,):

        stacks = [[i] for i in range(n)]
        positions = {i:(i,0) for i in range(n)}

        def restore(arg):
                s, i = positions[arg]
                stack = stacks[s]
                while stack[i+1:]:
                    j = stack.pop()
                    stacks[j].append(j)
                    positions[j] = j, len(stacks[j])-1

        def do(take, to):
            take_s, take_i = positions[take]
            to_s, to_i = positions[to]
            source = stacks[take_s]
            dest = stacks[to_s]
            length = len(dest)
            dest.extend(source[take_i:])
            del source[take_i:] 
            for i in range(length, len(dest)):
                positions[dest[i]] = to_s, i   

        while True:
            
            line = next(f)
            if line.strip() == 'quit': 
                break

            with line_bind(line, str, int, str, int) as (act, a, placing, b):

                a_stack, a_index = positions[a]
                b_stack, b_index = positions[b]

                if a == b or a_stack == b_stack: continue

                if act == 'move' and placing == 'onto':
                    restore(a)
                    restore(b)
                elif act == 'move' and placing == 'over':
                    restore(a)      
                elif act == 'pile' and placing == 'onto':
                    restore(b)      
                elif act == 'pile' and placing == 'over':
                    pass

                do(take=a, to=b)
                #print('\n')
                #for i, s in enumerate(stacks):
                    #print("{}: {}".format(i, " ".join(map(str, s))))
                #print(positions)


        #print('\n')
        for i, s in enumerate(stacks):
            print("{}:{}{}".format(i, " " if s else "", " ".join(map(str, s))))





