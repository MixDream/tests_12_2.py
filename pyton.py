import unittest
from pypyfile import Runner
from pypyfile import Tournament
class TournamentTest(unittest.TestCase):
    all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @classmethod
    def tearDownClass(cls):
        for i, result in sorted(cls.all_results.items()):
            print(f"{i}: {result}")
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)
        self.all_results = {}
    def test_usain_nick_race(self):
        tournament = Tournament(90, self.usain, self.nick)
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")
    def test_andrey_nick_race(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")
    def test_usain_andrey_nick_race(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results.update(tournament.start())
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")
if __name__ == "__main__":
    unittest.main()
