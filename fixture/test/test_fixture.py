import unittest

from fixture.core import Fixture


class TestFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = Fixture(team_number=7)

    def test_create_fixture(self):
        teams = ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor", "Bursaspor", "Sakaryaspor", "Başakşehir"]
        fixture = self.fixture.create_fixture()
        print(fixture)
        test = self.fixture.auto_set_teams(teams=teams)
        print(test)

