import unittest
from tic_tac_toe.game import Game, GameTied, InvalidMove

class TestGame(unittest.TestCase):

  def setUp(self):
    self.game = Game()

  def testDefaultSize(self):
    self.assertEqual(self.game.size, 3)

  def testValidMovesInit(self):
    self.assertEqual(len(self.game.valid_moves()), self.game.size ** 2)

  def testValidMovesType(self):
    self.assertIs(type(self.game.valid_moves()), list)

  def testValidMovesAfterMove(self):
    self.game.make_move(1, 'X')
    self.assertEqual(len(self.game.valid_moves()), self.game.size ** 2 - 1)

  def testCells(self):
    self.assertIs(type(self.game.cells[1]), list)

  def testCheckArrayTrue(self):
    self.assertTrue(self.game._check_array(['X','X','X'], 'X'))

  def testCheckArrayFalse(self):
    self.assertFalse(self.game._check_array(['O','X','X'], 'X'))

  def testMakeMove(self):
    self.game.make_move(1, 'X')
    with self.assertRaises(InvalidMove):
      self.game.make_move(1, 'X')

  def testCheckWinnerWonRow(self):
    self.game.make_move(1, 'X')
    self.game.make_move(2, 'X')
    self.game.make_move(3, 'X')
    self.assertTrue(self.game.check_winner('X'))

  def testCheckWinnerWonCol(self):
    self.game.make_move(1, 'X')
    self.game.make_move(4, 'X')
    self.game.make_move(7, 'X')
    self.assertTrue(self.game.check_winner('X'))

  def testCheckWinnerWonDiag1(self):
    self.game.make_move(1, 'X')
    self.game.make_move(5, 'X')
    self.game.make_move(9, 'X')
    self.assertTrue(self.game.check_winner('X'))

  def testCheckWinnerWonDiag2(self):
    self.game.make_move(3, 'X')
    self.game.make_move(5, 'X')
    self.game.make_move(7, 'X')
    self.assertTrue(self.game.check_winner('X'))

  def testCheckWinnerTied(self):
    self.game.make_move(1, 'X')
    self.game.make_move(2, 'X')
    self.game.make_move(3, 'O')
    self.game.make_move(4, 'O')
    self.game.make_move(5, 'X')
    self.game.make_move(6, 'X')
    self.game.make_move(7, 'X')
    self.game.make_move(8, 'O')
    self.game.make_move(9, 'O')
    with self.assertRaises(GameTied):
      self.game.check_winner('X')

if __name__ == '__main__':
  unittest.main()
