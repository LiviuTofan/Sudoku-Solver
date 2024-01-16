# If only one element is missing in a column, update it
def column_function(matrix):
    for i in range(9):
        miss, index, sum = 0, 0, 0
        for j in range(9):
            sum += matrix[j][i]
            if matrix[j][i] == 0:
                miss += 1
                index = j
        if miss == 1:
            matrix[index][i] = 45 - sum