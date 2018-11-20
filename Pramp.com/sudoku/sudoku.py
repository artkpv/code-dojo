"""
https://www.pramp.com/challenge/O5PGrqGEyKtq9wpgw6XP

Sudoku Solver

Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns true. Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.

In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the nine 3x3 sub-boards that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board, which for a well-posed board has a unique solution. As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution. No need to return the actual numbers that make up a solution.

A sudoku board is represented as a two-dimensional 9x9 array of the characters ‘1’,‘2’,…,‘9’ and the '.' character, which represents a blank space. The function should fill the blank spaces with characters such that the following rules apply:

In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above. If the function succeeds in solving the sudoku board, it’ll return true (false, otherwise).

Example (more examples can be found here):

alt A typical Sudoku board setter

alt The same board with solution numbers marked in red

Write a readable an efficient code, explain how it is built and why you chose to build it that way.

"""


def get_candidates(board, r, c):
  candidates = list(str(i) for i in range(1,10))
  for i in range(9):
    if board[r][i] in candidates:
      candidates.remove(board[r][i])
  for i in range(9):
    if board[i][c] in candidates:
      candidates.remove(board[i][c])
  sq_first_r = (r // 3) * 3
  sq_first_c = (c // 3) * 3
  for i in range(9):
    sq_r = sq_first_r + (i // 3)
    sq_c = sq_first_c + (i % 3)
    if board[sq_r][sq_c] in candidates:
      candidates.remove(board[sq_r][sq_c])
  return candidates

def sudoku_solve(board):
  candidates = [str(i) for i in range(1,10)]
  min_row, min_col = None, None
  has_empty = False
  for row in range(9):
    for col in range(9):
      if board[row][col] != '.':
        continue
      has_empty = True
      current_candidates = get_candidates(board, row, col)
      if len(current_candidates) <= len(candidates):
        candidates = current_candidates
        min_row = row
        min_col = col
  if not has_empty or len(candidates) == 0:
    return not has_empty
  for c in candidates:
    board[min_row][min_col] = c
    if sudoku_solve(board):
      return True
    board[min_row][min_col] = '.'
  return False


def print_board(b):
    for r in range(9):
        print(' '.join(str(c) for c in b[r]))

#board = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
board  =[[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

print(sudoku_solve(board))
