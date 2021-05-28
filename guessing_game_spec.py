import unittest
from guessing_game import GuessingGame

class GuessingGameTestCase(unittest.TestCase):
    """Tests for guessing_game.py"""
    def test_one(self):
        game = GuessingGame(10)
        self.assertEqual(game.solved(), False)
        self.assertEqual(game.guess(5), "low")
        self.assertEqual(game.guess(20), "high")
        self.assertEqual(game.solved(), False)
        self.assertEqual(game.guess(10), "correct")
        self.assertEqual(game.solved(), True)