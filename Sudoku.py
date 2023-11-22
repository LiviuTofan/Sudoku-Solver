matrix = []
newmatrix = []

for i in range(9):
    row = input()
    row_list = [int(x) for x in row.split()]
    matrix.append(row_list)


# daca pe rand lipseste un element il punem
def rand():
    for i in range(9):
        miss = 0
        sum = 0
        index = 0
        change = 0
        for j in range(9):
            if matrix[i][j] == 0:
                miss += 1
                index = j
        if miss == 1:
            for k in matrix[i]:
                sum += k
            matrix[i][index] = 45 - sum
            change = 1
            continue


# daca pe coloana lipseste un element il punem
def coloana():
    for i in range(9):
        miss = 0
        sum = 0
        index = 0
        change = 0
        for j in range(9):
            if matrix[j][i] == 0:
                miss += 1
                index = j
            sum += matrix[j][i]
        if miss == 1:
            matrix[index][i] = 45 - sum
            change = 1
            continue


# daca in matrice 3x3 lipseste un element il adaugam
def bucati():
    miss, x, y, m, n = 0, 0, 0, 3, 3
    newmatrix = []
    while (miss != 9):
        change, sum, index, counter = 0, 0, 0, 0
        submatrices = []
        for i in range(y, n):
            for j in range(x, m):
                submatrices.append(matrix[i][j])
        for k in range(len(submatrices)):
            sum += submatrices[k]
            if submatrices[k] == 0:
                counter += 1
                index = k
        if counter == 1:
            submatrices[index] = 45 - sum
            change = 1
        miss += 1
        if m != 9:
            m += 3
            x += 3
        else:
            n += 3
            y += 3
            m = 3
            x = 0
        newmatrix.append(submatrices)
    return newmatrix


newmatrix = bucati()

change = 1
if change:
    rand()
    coloana()
    bucati()
for row in newmatrix:
    print(row)

kounter = 1
for row in newmatrix:
    print("Randul", kounter)
    missing = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    indecele, xaxis, yaxis, index, xax, yax = None, None, None, None, None, None
    dictionar = {}
    missdictionar = {}

    for i in range(9):
        if row[i] != 0:
            missing.discard(row[i])  # vedem care lipsesc
        else:
            indecele = i
            if indecele <= 2:
                xaxis = 1
            elif indecele > 2 and indecele <= 5:
                xaxis = 2
            else:
                xaxis = 3
            if indecele == 0 or indecele == 3 or indecele == 6:
                yaxis = 1
            elif indecele == 1 or indecele == 4 or indecele == 7:
                yaxis = 2
            else:
                yaxis = 3
            # dictionar cu cheia = indecele necunoscutei in rand (0), axa x si axa y a acestuia.
            dictionar[indecele] = (xaxis, yaxis)
    print("Necunoscutele:")
    for key, value in dictionar.items():
        print("Cheie:", key, "Valoare:", value)
    print("Missing:")
    for val in missing:
        axaX = []  # pentru a adauga axele x
        axaY = []  # pentru a adauga axele y
        if kounter == 1:
            if val in newmatrix[1]:  # pe x
                index = newmatrix[1].index(val)
                if index <= 2:
                    xax = 1
                elif index > 2 and index <= 5:
                    xax = 2
                else:
                    xax = 3
                axaX.append(xax)
            if val in newmatrix[2]:  # pe x
                index = newmatrix[2].index(val)
                if index <= 2:
                    xax = 1
                elif index > 2 and index <= 5:
                    xax = 2
                else:
                    xax = 3
                    axaX.append(xax)
            if val in newmatrix[3]:  # pe y
                index = newmatrix[3].index(val)
                if index == 0 or index == 3 or index == 6:
                    yax = 1
                elif index == 1 or index == 4 or index == 7:
                    yax = 2
                else:
                    yax = 3
                axaY.append(yax)
            if val in newmatrix[6]:  # pe y
                index = newmatrix[6].index(val)
                if index == 0 or index == 3 or index == 6:
                    yax = 1
                elif index == 1 or index == 4 or index == 7:
                    yax = 2
                else:
                    yax = 3
                axaY.append(yax)
            missdictionar[val] = (axaX, axaY)
    for k, v in missdictionar.items():
        print("Cheie:", k, "Valoare:", v)

    kounter += 1
