import unittest

from fixture.core import Fixture


class TestFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = Fixture(team_number=8)

    def test_create_fixture(self):
        fixture = self.fixture.create_fixture()
        print(fixture)

    def test_auto_set_teams(self):
        teams = ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor", "Bursaspor", "Sakaryaspor", "Başakşehir", "Samsunspor"]
        self.fixture.create_fixture()
        fixture_with_teams = self.fixture.auto_set_teams(teams=teams)
        print(fixture_with_teams)