import unittest
from RPS_game import play, tima, mercy, dara, tim
from RPS import player


class UnitTests(unittest.TestCase):
    def test_player_vs_dara(self):
        print("Testing game against dara...")
        actual = play(player, dara, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat dara at least 60% of the time.')

    def test_player_vs_mercy(self):
        print("Testing game against mercy...")
        actual = play(player, mercy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat mercy at least 60% of the time.')

    def test_player_vs_tim(self):
        print("Testing game against tim...")
        actual = play(player, tim, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat tim at least 60% of the time.')

    def test_player_vs_tima(self):
        print("Testing game against tima...")
        actual = play(player, tima, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat tima at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()

