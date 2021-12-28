import itertools

class Match(object):

    newid = itertools.count()

    def __init__(self, item):

        #automatically generated starting from 1
        self.new_id = next(Match.newid) + 1

        self.home_team = item["home_team"]
        self.away_team = item["away_team"]
        self.home_team_goals = item["home_team_goals"]
        self.away_team_goals = item["away_team_goals"]

        if not (isinstance(self.home_team , str)):
            raise TypeError("Expected string input")
        if not (isinstance(self.away_team , str)):
            raise TypeError("Expected string input")
        if not (isinstance(self.home_team_goals, int)):
            raise TypeError("Expected int input")
        if not (isinstance(self.away_team_goals, int)):
            raise TypeError("Expected int input")

    def __repr__(self):
        r = dict(self.__dict__)
        del r["new_id"]
        return "Match " + str(self.new_id) + " : " + str(r)




