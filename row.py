# If only one element is missing in a row, update it
def row_function(matrix):
    for i in range(9):
        miss, index, sum = 0, 0, 0
        for j in range(9):
            sum += matrix[i][j]
            if matrix[i][j] == 0:
                miss += 1
                index = j
        if miss == 1:
            matrix[i][index] = 45 - sum