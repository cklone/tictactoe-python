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
A command-line game of tic-tac-toe written in python 2.7.

Main objects are Game for game control, Player for player moves
(including AIPlayer for computer play), and io to handle
everything related to display and input.
"""

from tic_tac_toe.game import Game, GameTied, InvalidMove
from tic_tac_toe.player import Player
from tic_tac_toe.ai_player import AIPlayer
from tic_tac_toe import io
import sys

# Initialize objects
game = Game(3)
players = [Player('X'), AIPlayer('O')]
playing = True # Main loop control needed to break out of multiple levels
io.init()

# Main game loop
while playing:
  io.print_board(game)
  try:
    for player in players:
      player.make_move(game)
      if game.check_winner(player.symbol):
        io.print_board(game)
        if players.index(player) == 0:
          io.winner()
        else:
          io.loser()
        playing = False
        break

  except InvalidMove:
    io.invalid()

  except GameTied:
    io.print_board(game)
    io.game_tied()
    break

  except KeyboardInterrupt:
    io.game_over()
    break
