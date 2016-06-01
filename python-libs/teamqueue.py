
from collections import deque

class teamqueue(object):
    """
    I represent a "team" queue, in the sense of UVa540.
    """

    def __init__(self, *teams):

        self.queue = deque()
        self.membership = {teammate:team for team in teams for teammate in team}
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
