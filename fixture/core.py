import random
from math import floor


class Fixture:
    def __init__(self, team_number: int = 3):
        self.team_number = team_number
        self.teams = []
        self.fixture = []
        self.template = []
        self.weekly_match_number = floor(self.team_number / 2)
        self.is_pass_team = self.team_number % 2
        self.week_number = self.team_number - 1

    def create_pass_team_fixture_template(self):
        for f in range(self.team_number):
            if f % 2:
                self.template.append([f, f+1])

        if self.is_pass_team:
            self.template.append([self.team_number])

    def create_odd_number_team_fixture_template(self):
        normal_list = [n+1 for n in range(self.weekly_match_number)]
        self.template = [[[*normal_list], [n+self.weekly_match_number for n in range(self.weekly_match_number)]]]

    def pass_team_fixture(self):
        fixture = [[*self.template]]
        for m in range(self.week_number):
            new_list = []
            new_pass_value = self.template[self.weekly_match_number-1][0]
            for match in range(self.weekly_match_number, 0, -1):
                if match == 0:
                    new_list.append([self.template[0][1], self.template[self.weekly_match_number-1][0]])
                else:
                    new_list.append([self.template[match-1][1], self.template[match-2][0]])

            new_list.append([new_pass_value])
            self.template = new_list
            non_last_index = new_list[:-1]
            random.shuffle(non_last_index)
            fixture.append([*non_last_index, new_list[len(new_list) - 1]])

        return fixture

    def odd_number_team_fixture(self):
        fixture = []

        template_line = self.template[0]
        m = 0
        while self.week_number > m:
            first_index_value = template_line[0][0]
            last_index = self.weekly_match_number - 1

            week_maths = []
            for match in range(self.weekly_match_number):
                if m % 2 == 0:
                    if match % 2 == 1 or match == 0:
                        week_maths.append([template_line[0][match], template_line[1][match]])
                    else:
                        week_maths.append([template_line[1][match], template_line[0][match]])
                else:
                    if match % 2 == 0:
                        week_maths.append([template_line[1][match], template_line[0][match]])
                    else:
                        week_maths.append([template_line[0][match], template_line[1][match]])

            random.shuffle(week_maths)
            fixture.append(week_maths)

            template_line[0] = template_line[0][1:]
            template_line[0].append(template_line[1][last_index])

            if m == 0:
                template_line[1] = template_line[1][:-1]
                template_line[1].insert(0, 1)
            else:
                template_line[1] = template_line[1][:-1]
                template_line[1].insert(0, 1)
                template_line[1][1] = first_index_value

            m += 1
        return fixture

    def reverse_fixture(self, fixture=None):
        reverse_fixture = []
        for week in fixture:
            reverse_week = []
            for match_index, match in enumerate(week):
                reverse_teams = match[::-1]
                reverse_week.append(reverse_teams)
            reverse_fixture.append(reverse_week)
        return reverse_fixture

    def auto_set_teams(self, teams: [str]):
        if len(teams) != self.team_number:
            return "Not Match Team Number and Length Of Teams"

        self.teams = teams
        random.shuffle(self.teams)
        for week_index, week in enumerate(self.fixture):
            for match_index, match in enumerate(week):
                for team_index, team in enumerate(match):
                    if str(self.fixture[week_index][match_index][team_index]).isdigit():
                        self.fixture[week_index][match_index][team_index] = self.teams[
                            int(self.fixture[week_index][match_index][team_index]) - 1]
        return self.fixture

    def create_fixture(self):

        if self.is_pass_team:
            self.create_pass_team_fixture_template()
            self.fixture = self.pass_team_fixture()
            self.fixture = [*self.fixture, *self.reverse_fixture(self.fixture)]
        else:
            self.create_odd_number_team_fixture_template()
            self.fixture = self.odd_number_team_fixture()
            self.fixture = [*self.fixture, *self.reverse_fixture(self.fixture)]

        return self.fixture
