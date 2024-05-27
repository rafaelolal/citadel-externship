def splatter(matrix):
    zeros = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    for zero in zeros:
        for i in range(len(matrix)):
            if i == zero[0]:
                continue
            matrix[i][zero[1]] += 1

        for j in range(len(matrix[0])):
            if j == zero[1]:
                continue
            matrix[zero[0]][j] += 1

    return matrix


print("\n".join(map(str, splatter([[1, 0, 3],
                                   [0, 0, 6],
                                   [7, 0, 7]]))))
