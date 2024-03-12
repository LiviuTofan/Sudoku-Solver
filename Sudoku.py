from row import row_function
from column import column_function
from submatrices import pieces
from solver import algorithm

matrix = []

# Input sudoku
for i in range(9):
    row = input()
    row_list = [int(x) for x in row.split()]
    matrix.append(row_list)

# Execute functions to solve the sudoku
def do_sudoku(matrix):
    while True:
        initial_matrix = [row[:] for row in matrix]
        column_function(matrix)
        row_function(matrix)
        pieces(matrix)
        algorithm(matrix)

        if initial_matrix == matrix:
            break

do_sudoku(matrix)
if any(0 in row for row in matrix):
    print("Not done")
else:
    for row in matrix:
        print(row)