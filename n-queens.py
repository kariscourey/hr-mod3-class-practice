def filter_available_squares(candidate_squares, queen):
    available_squares = []
    for square in candidate_squares:
        # check columns
        if square[1] != queen[1]:
            # check rows
            if square[0] != queen[0]:
                # check positive diag
                if square != (queen[0] + 1, queen[1] + 1):
                    # check negative diag
                    if square != (queen[0] + 1, queen[1] - 1):
                        available_squares.append(square)
    return available_squares


N = 5

# available_squares = [
#     (0,0),
#     (0,1),
#     (0,2),
#     (0,3),
#     (1,0),
#     (1,1),
#     (1,2),
#     (1,3),
#     (2,0),
#     (2,1),
#     (2,2),
#     (2,3),
#     (3,0),
#     (3,1),
#     (3,2),
#     (3,3),
# ]

# n-queens: for each column, do this
for i in range(N):

    queens = []
    available_squares = [(r,c) for r in range(N) for c in range(N)][i:]

    while len(available_squares) > 0:
        # get queen from avail squares
        queen = available_squares[0]
        # add queen to list of queens
        queens.append(queen)
        # elim squares
        available_squares = filter_available_squares(available_squares, queen)

    if len(queens) == N:
        break



# verify queens
print(len(queens) == N)
print(queens)
