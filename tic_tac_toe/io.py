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
This module handles all display for the game. It depends on class Game
in order to display the game board. Change this class to make the
game look prettier.
"""

import sys
import os

QUIT_STRINGS = ['quit', 'exit', 'bye']

def _print_file(filename):
  try:
    f = open(filename, "r")
    try:
      string = f.read()
      print string
    finally:
      f.close()
  except IOError:
    pass

def init():
  os.system('clear')
  _print_file('images/banner.txt')
  print 'Please make your move by entering a number from the movement key.'
  print "Type '%s' to exit the game." % QUIT_STRINGS[0]

def game_over():
  print
  _print_file('images/game_over.txt')

def winner():
  _print_file('images/winner.txt')

def loser():
  _print_file('images/loser.txt')

def game_tied():
  _print_file('images/game_tied.txt')

def invalid():
  print "Invalid move. Please use the movement key or type '%s'." % QUIT_STRINGS[0]

def get_move():
  reply = raw_input('\nMake your move: ')
  if reply in QUIT_STRINGS:
    raise KeyboardInterrupt
  return reply

def print_board(game):
  print '\nBoard:%sMovement Key:' % (' '*(2 * game.size + 9))
  for y in list(range(game.size)):
    row = ''
    for x in list(range(game.size)):
      if x != 0:
        row += '|'
      row += '%1s' % game.board[y][x]
    row += ' '*16
    for x in list(range(game.size)):
      if x != 0:
        row += '|'
      string = '%' + str(len(str(game.size ** 2))) + 'd'
      row += string % (y * game.size + x + 1)
    print row
