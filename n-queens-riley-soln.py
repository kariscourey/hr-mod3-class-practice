def queen_is_valid(queens, queen):
  row, col = queen
  if row in set([r for r, _ in queens]): return False
  if col in set([c for _, c in queens]): return False
  if (row + col) in set([r + c for r, c in queens]): return False
  if (row - col) in set([r - c for r, c in queens]): return False
  return True

def add_queen(queens, row, n):
  if row == n:
    return True

  for col in range(n):
    if queen_is_valid(queens, (row, col)):
      queens.add((row, col))

      if add_queen(queens, row + 1, n):
        return True

      queens.remove((row, col))
  return False

def solve_n_queens(n):
  queens = set()

  if add_queen(queens, 0, n):
    return queens
  return False

print(solve_n_queens(4))
