#!/usr/bin/env python
# encoding: utf-8


import time
from rich.console import Console
from rich.traceback import install
from rich.progress import track
install()
start_time = time.time()
console = Console()

## DATA
filepath = "./input.txt"

## MAIN
number_list = []
board_list = []

# load data
board = []
line_count = 0
with open(filepath) as fp:
  for line in fp:
    if line_count == 0:
      number_list = line.strip().split(",")
    elif len(line.strip()) == 0:
      if board:
        board_list.append(board)
        board = []
    else:
      board.append(line.strip().split())
    line_count += 1

#print(number_list)
#print(board_list)

## part 1
def get_score(board,number):
  # compute score : sum of number in board * number
  board_sum = 0
  for x in range(0,5):
    for y in range(0,5):
      if board[x][y] != "*":
        board_sum += int(board[x][y])
  return board_sum * int(number)

def update_board(board,number):
  # if number in board, replace number with '*' and return board
  for x in range(0,5):
    for y in range(0,5):
      if board[x][y] == number:
        board[x][y] = "*"
  return board

def status_board(board):
  # board_status : W=won L=loose
  board_status = "L"
  # check lines
  for i in range(0,5):
    if (board[i][0] == "*" and board[i][1] == "*" and board[i][2] == "*" and board[i][3] == "*" and board[i][4] == "*"):
      board_status = "W"
      break
  # check columns
  for i in range(0,5):
    if (board[0][i] == "*" and board[1][i] == "*" and board[2][i] == "*" and board[3][i] == "*" and board[4][i] == "*"):
      board_status = "W"
      break
  return board_status

def check_board(board):
  # play numbers against a board and return :
  #  - status ("W" or "L")
  #  - rank (position of number in list)
  #  - score (when board won)
  board_status = "L"
  board_rank = 0
  board_score = 0
  i = 0
  while board_status == "L" and i < len(number_list):
    board = update_board(board,number_list[i])
    board_status = status_board(board)
    if board_status == "W":
      board_score = get_score(board,number_list[i])
      board_rank = i
    i += 1
  return board_status, board_rank, board_score

# check all boards one by one
board_result = []
for board in board_list:
  board_status, board_rank, board_score = check_board(board)
  board_result.append([board_status, board_rank, board_score])

#print(board_result)

# get best board
from operator import itemgetter
board_winner = min(board_result,key=itemgetter(1))

# score
print(board_winner[2])

## part 2
# get last board to win
board_lastwin = max(board_result,key=itemgetter(1))
# score
print(board_lastwin[2])

console.print('Duration : %.6f seconds' % (time.time() - start_time))

