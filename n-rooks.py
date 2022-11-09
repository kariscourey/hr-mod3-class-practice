def filter_available_squares(candidate_squares, rook):
    available_squares = []
    for square in candidate_squares:
        # check columns
        if square[1] != rook[1]:
            # check rows
            if square[0] != rook[0]:
                available_squares.append(square)
    return available_squares


N = 4
rooks = []
available_squares = [(r,c) for r in range(N) for c in range(N)]

# stop here
while len(available_squares) > 0:

    # get rook from avail squares
    rook = available_squares[0]

    # add rook to list of rooks
    rooks.append(rook)

    # elim squares
    available_squares = filter_available_squares(available_squares, rook)


print(rooks)

# verify
print(len(rooks) == N)
