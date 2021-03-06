
# ___declarations in `utilities.py`___
# do update in `utilities.py` if you do any change
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

def python_code(*objs, markdown=True, remove_comments=False, docstring_delimiter=r'"""'):

    import inspect

    def cleaner(obj):
        src = inspect.getsource(obj)
        if remove_comments and inspect.getdoc(obj):
            # the followoing could be done more clearly using regex, but for now...
            start = src.index(docstring_delimiter, 0)
            end = src.index(docstring_delimiter, start+len(docstring_delimiter))
            removing_src = list(src)
            del removing_src[start:end+len(docstring_delimiter)]
            src = "".join(removing_src)
        return src

    src = "\n".join(map(cleaner, objs))
    
    if markdown:
        from IPython.display import Markdown
        src = Markdown('```python\n{0}\n```'.format(src))
    
    return src

#________________________________________________________________________


