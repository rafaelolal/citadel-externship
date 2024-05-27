def sink_matrix_1(matrix):
    n = len(matrix)
    m = len(matrix[0])

    if n % 2 == 0 or m % 2 == 0:
        return None

    i = n//2
    j = m//2

    return matrix[i]
