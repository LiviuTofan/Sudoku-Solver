# Algorithm that solves logically the sudoku, it takes a 3x3 part, save all missing elements values, and indexes
def algorithm(matrix):
    counter, x, y, m, n = 0, 0, 0, 3, 3
    while (counter != 9):
        # Keys are consecutive numbers with values that first is index of row and second of column of missing element
        missing = {}
        # There will remain only missing elements
        elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Find missing elements in each 3x3 submatrix, and their indexes append to dictionary
        for i in range(y, n):
            for j in range(x, m):
                if (matrix[i][j] in elements):
                    elements.remove(matrix[i][j])
                else:
                    missing[len(missing)] = (i,j)
        # Call function that find in each 3x3 if some missing elements can be replaced
        replace_missing_elements_if_possible(matrix, elements, missing)
        # Move to next 3x3 submatrix
        counter += 1
        if m != 9:
            m += 3
            x += 3
        else:
            n += 3
            y += 3
            m = 3
            x = 0

# Try every missing element on all indexes, if it can be replaced only in one position, it means that it will be updated.
def replace_missing_elements_if_possible(matrix, elements, missing):
    lagunas = {}
    for element in elements:
        laguna, finalYindex, finalXindex = 0, 0, 0
        for value in missing.values():
            xindex, yindex = value
            for i in range(9):
                if matrix[xindex][i] == element or matrix[i][yindex] == element:
                    laguna += 1

                    break
            # Save the final indexes, that may be indexes of missing element
            else:
                finalYindex = yindex
                finalXindex = xindex
        # If missing element can be replaced only in one position in 3x3 piece, then replace it
        if (laguna == len(elements) - 1):
            matrix[finalXindex][finalYindex] = element