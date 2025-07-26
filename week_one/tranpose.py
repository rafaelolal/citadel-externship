import random


def transpose(matrix):
    transposed = [[0]*len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):  # if not rectangular 0 -> i
            transposed[j][i] = matrix[i][j]

    return transposed


def generate_random_2d_array(rows, cols):
    return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]


random_2d_array = generate_random_2d_array(3, 6)
# print(random_2d_array)

print("\n".join(map(str, random_2d_array)))
print("\n".join(map(str, transpose(random_2d_array))))
