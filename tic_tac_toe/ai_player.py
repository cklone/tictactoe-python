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
An AI player of our game. Subclasses Player and implements the simplest
(i.e. dumbest) AI algorithm: make a move at random.
"""

import random
from player import Player

class AIPlayer(Player):
  def make_move(self, game):
    game.make_move(random.choice(game.valid_moves()), self.symbol)
