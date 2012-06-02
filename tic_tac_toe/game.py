# Copyright 2012 Chris Kline
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the class Game and some exceptions for game play.
The main methods for Game are make_move and check_winner needed for
game control. The method valid_moves is useful internally and also
for AI players.
"""

class InvalidMove(Exception):
  pass

class GameTied(Exception):
  pass

class Game:
  def __init__(self, size=3):
    """
    Initialize the game and some useful data structures.
    Send in the size of the board, defaults to 3x3. For now,
    all board will have the same number of rows and columns.

      size:    The size of the board
      board:   The actual game board (filled in at runtime)
      cells:   A dictionary where the key is an input (e.g. 1-9)
               and the value is the cell on the board. For example,
               key 1 => board[0][0], key 7 => board[2,0]. This
               will also be updated as moves are made.
    """
    self.size = size
    self.board = []
    self.cells = {}
    cnt = 0
    for y in list(range(size)):
      row = []
      for x in list(range(size)):
        cnt += 1
        row.append('')
        self.cells[cnt] = [y, x]
      self.board.append(row)

  def _check_array(self, array, symbol):
    """
    Return True if every element of the array == symbol
    False otherwise
    """
    for i in array:
      if i != symbol:
        return False
    return True

  def valid_moves(self):
    """
    Helper method to return array of valid moves. Useful for AI.
    """
    return self.cells.keys()

  def make_move(self, move, symbol):
    """
    Make a move on the board.
    Args:
      move:   The move to make (position on board)
      symbol: The symbol to put in that position
    Raises:
      InvalidMove if move cannot be made
    """
    try:
      move = int(move)
    except:
      raise InvalidMove
    else:
      if move in self.valid_moves():
        y, x = self.cells[move]
        self.board[y][x] = symbol
        del self.cells[move]
      else:
        raise InvalidMove
      
  def check_winner(self, symbol):
    """
    Check to see if the game is over and if the
    symbol passed in is the winner.
    Args:
      symbol: The player's symbol
    Returns:
      True:   Symbol is the winner
      False:  No winner and game is not over
    Raises:
      GameTied exception if game is over without winner
    """
    b = self.board
    sections = [] # An array of sections to check
    diag1 = []
    diag2 = []

    for y in list(range(self.size)):
      sections.append(b[y]) # Row y
      sections.append([r[y] for r in b]) # Col y
      for x in list(range(self.size)):
        if y == x:
          diag1.append(b[y][x])
        if y == (self.size - x - 1):
          diag2.append(b[y][x])

    sections.append(diag1)
    sections.append(diag2)
    for section in sections:
      if self._check_array(section, symbol):
        return True

    if len(self.valid_moves()) == 0:
      raise GameTied

    return False
