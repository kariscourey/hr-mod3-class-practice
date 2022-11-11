def is_safe(board, row_index, column_index, size):
    # Check the row for other queens
    row = board[row_index]
    for index, value in enumerate(row):
        if value == 1:
            return False

    # Check the diagonals
    for index in range(1, size - column_index + 1):
        try:
            if board[row_index - index][column_index + index] != 0:
                return False
        except IndexError:
            pass
        try:
            if board[row_index + index][column_index + index] != 0:
                return False
        except IndexError:
            pass


    for index in range (column_index - 1, -1, -1):
        try:
            if board[row_index - index][column_index - index] != 0:
                return False
        except IndexError:
            pass
        try:
            if board[row_index + index][column_index - index] != 0:
                return False
        except IndexError:
            pass
    return True


def place_queen_in_column(board, column_index, size):
    if column_index >= size:
        return True
    for row_index in range(size):
        if is_safe(board, row_index, column_index, size):
            board[row_index][column_index] = 1
            if place_queen_in_column(board, column_index + 1, size):
                return True
            board[row_index][column_index] = 0
    return False


def n_queens(size):
    board = []
    for i in range(size):
        row = [0] * size
        board.append(row)

    place_queen_in_column(board, 0, size)

    return board

N = 8
print(n_queens(N))
