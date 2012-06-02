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
The canonical player of our game. Just subclass and implement make_move
in order to modify behavior or write AI players. This class depends on
the io module in order to get the player's move from the command-line.
"""

import io

class Player:
  def __init__(self, symbol):
    self.symbol = symbol

  def make_move(self, game):
    game.make_move(io.get_move(), self.symbol)
