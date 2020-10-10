"""
We're going to create and solve a given Sudoku, in the form of an array, using backtracking.
"""


# First, a function to print the given board in the form of an array.


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(" ", str(b[i][j]))
            else:
                print(" ", str(b[i][j]), " ", end=" ")


def solve(bo):
    index = is_empty(bo)
    if index == [-1, -1]:
        return True
    row = index[0]
    column = index[1]
    for i in range(1, 10):
        if is_valid(row, column, bo, i):
            bo[row][column] = i
            if solve(bo):
                return True
            bo[row][column] = 0
    return False


# Now, we'll check for the empty spaces.


def is_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return [i, j]
    return [-1, -1]


# checking for all three constraints.


def is_valid(r, c, b, val):
    b_row = r - r % 3
    b_col = c - c % 3
    if check_row(r, b, val) and check_col(c, b, val) and check_three(b_row, b_col, val, b):
        return True
    return False


# function to check unique values in a row.


def check_row(row, b, val):
    for i in range(len(b[0])):
        if b[row][i] == val:
            return False
    return True


# function to check unique values in a column.


def check_col(col, b, val):
    for i in range(len(b[0])):
        if b[i][col] == val:
            return False
    return True


# function to check unique values in a 3x3 boxes.


def check_three(row, col, val, b):
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if b[i][j] == val:
                return False
    return True


bo = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
      [5, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 7, 0, 0, 0, 0, 3, 1],
      [0, 0, 3, 0, 1, 0, 0, 8, 0],
      [9, 0, 0, 8, 6, 3, 0, 0, 5],
      [0, 5, 0, 0, 9, 0, 6, 0, 0],
      [1, 3, 0, 0, 0, 0, 2, 5, 0],
      [0, 0, 0, 0, 0, 0, 0, 7, 4],
      [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print("The given board is:")
print_board(bo)
solve(bo)
print("\t")
print("After adding values, the board is:")
print_board(bo)
