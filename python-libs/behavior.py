
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
