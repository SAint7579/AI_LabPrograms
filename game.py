from TicTacToe_Environment import *
import copy
from math import inf as infinity
from random import choice
import platform
import time
import pdb
import copy

def set_move(x, y, player, env):
    if env.board[x,y] == 0:
        env.board[x][y] = player
        return True
    else:
        return False

def empty_cells(env):
    cells = []

    for x, row in enumerate(env.board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def minimax(env, depth, player):
    if player == env.o:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or env.game_over(force_recalculate=True):
        score = env.reward(env.o)
        return [-1, -1, score]

    for cell in empty_cells(env):
        x, y = cell[0], cell[1]
        env.board[x][y] = player
        score = minimax(env, depth - 1, -player)
        env.board[x][y] = 0
        score[0], score[1] = x, y

        if player == env.o:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best
def ai_turn(env):
    depth = len(empty_cells(env))
    if depth == 0 or env.game_over():
        return
    print('Computer turn')
    env.draw_board()

    if depth == 9:
        #Selecting a random action
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        #Playing minimax
        move = minimax(copy.deepcopy(env), depth, env.o)
        x, y = move[0], move[1]

    set_move(x, y, env.o,env)
    time.sleep(1)


def human_turn(env):
    depth = len(empty_cells(env))
    if depth == 0 or env.game_over():
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }
    print('Human turn')
    env.draw_board()

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], env.x, env)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


if __name__ == '__main__':

    env = Environment()
    first = ''  # if human is the first
    while first != 'Y' and first != 'N':
        try:
            first = input('Do you want to go first?[y/n]: ').upper()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(env)) > 0 and not env.game_over():
        if first == 'N':
            ai_turn(env)
            first = ''

        human_turn(env)
        ai_turn(env)

    #pdb.set_trace()
    # Game over message
    if env.game_over(force_recalculate= True):
        if env.winner == env.x:
            print('Human turn')
            env.draw_board()
            print('YOU WIN!')
        elif env.winner == env.o:
            print('Computer turn')
            env.draw_board()
            print('YOU LOSE!')
        elif env.winner == None:
            env.draw_board()
            print('DRAW!')

    exit()


'''
Do you want to go first?[y/n]: y
Human turn
-------------

-------------

-------------

-------------
Use numpad (1..9): 1
Computer turn
-------------
  x
-------------

-------------

-------------
Human turn
-------------
  x
-------------
      o
-------------

-------------
Use numpad (1..9): 9
Computer turn
-------------
  x
-------------
      o
-------------
          x
-------------
Human turn
-------------
  x   o
-------------
      o
-------------
          x
-------------
Use numpad (1..9): 8
Computer turn
-------------
  x   o
-------------
      o
-------------
      x   x
-------------
Human turn
-------------
  x   o
-------------
      o
-------------
  o   x   x
-------------
Use numpad (1..9): 3
Computer turn
-------------
  x   o   x
-------------
      o
-------------
  o   x   x
-------------
Human turn
-------------
  x   o   x
-------------
      o   o
-------------
  o   x   x
-------------
Use numpad (1..9): 4
-------------
  x   o   x
-------------
  x   o   o
-------------
  o   x   x
-------------
DRAW!
'''
