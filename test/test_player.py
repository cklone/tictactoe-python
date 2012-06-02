import unittest
from tic_tac_toe.player import Player

class TestPlayer(unittest.TestCase):
  def setUp(self):
    self.player = Player('X')

  def testPlayerInit(self):
    self.assertEqual(self.player.symbol, 'X')

if __name__ == '__main__':
  unittest.main()
