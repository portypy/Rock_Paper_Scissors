import unittest
from app.modules.player import Player
from app.modules.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_r = Player("player_r","rock")
        self.player_s = Player("player_s","scissors")
        self.player_p = Player("player_p","paper")

        self.game = Game()


    def test_rock_vs_paper_wins_paper(self):
        self.assertEqual("paper wins over rock",self.game.game(self.player_r.choice,self.player_p.choice))

    def test_paper_vs_rock_wins_paper(self):
        self.assertEqual("paper wins over rock",self.game.game(self.player_p.choice,self.player_r.choice))

    def test_scissors_vs_rock_wins_rock(self):
        self.assertEqual("rock wins over scissors",self.game.game(self.player_s.choice,self.player_r.choice))

    def test_rock_vs_scissors_wins_rock(self):
        self.assertEqual("rock wins over scissors",self.game.game(self.player_r.choice,self.player_s.choice))

    def test_paper_vs_scissors_wins_scissors(self):
        self.assertEqual("scissors wins over paper",self.game.game(self.player_p.choice,self.player_s.choice))

    def test_scissors_vs_paper_wins_scissors(self):
        self.assertEqual("scissors wins over paper",self.game.game(self.player_s.choice,self.player_p.choice))

