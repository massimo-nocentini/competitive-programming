
import fileinput
from contextlib import contextmanager
from collections import deque

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


class teamqueue(object):
    """
    I represent a "team" queue, in the sense of UVa540.
    """

    def __init__(self, *teams):

        self.queue = deque()
        self.membership = {teammate:team for team in teams 
                                         for teammate in team}
        self.teams_queues = {team:deque() for team in teams}

    def appendleft(self, teammate):

        team = self.membership[teammate]
        team_queue = self.teams_queues[team]
        if not team_queue:
            self.queue.appendleft(team)
        team_queue.appendleft(teammate)

    def pop(self):

        team = self.queue[-1]
        team_queue = self.teams_queues[team]
        teammate = team_queue.pop()
        if not team_queue:
            self.queue.pop()
        return teammate

#________________________________________________________________________

with stdin_input() as next_line:

    scenario = 0

    while True:

        scenario += 1

        with line_bind(next_line(), int) as (n,):
            
            if not n: break

            print('Scenario #{}'.format(scenario))

            teams = []
            for _ in range(n):
                team_line = next_line()
                t, *team = team_line.split(' ')
                teams.append(tuple(map(int, team)))

            queue = teamqueue(*teams)

            while True:

                command = next_line()

                if command == 'STOP\n': break

                message, *teammates = command.split(' ')
                if message == 'DEQUEUE\n':
                    print(queue.pop())
                else:
                    queue.appendleft(int(teammates.pop()))

            print()

    print()


















