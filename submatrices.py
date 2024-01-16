# If only one element is missing in a 3x3 piece, update it
def pieces(matrix):
    counter, x, y, m, n = 0, 0, 0, 3, 3
    while (counter != 9):
        sum, yindex, xindex, miss = 0, 0, 0, 0
        for i in range(y, n):
            for j in range(x, m):
                sum += matrix[i][j]
                if (matrix[i][j] == 0):
                    miss += 1
                    yindex = i
                    xindex = j

        if miss == 1:
            matrix[yindex][xindex] = 45 - sum

        # Move to next 3x3 piece
        counter += 1
        if m != 9:
            m += 3
            x += 3
        else:
            n += 3
            y += 3
            m = 3
            x = 0

