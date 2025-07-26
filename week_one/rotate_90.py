# NOT SOLVED!!!!

def rotate_90(matrix):
    """
    (col_index + row_index, len(matrix)-1-row_index)
    """

    n = len(matrix)
    rotated = [[0]*len(matrix) for _ in range(len(matrix[0]))]
    origin = 0
    ops = n-1

    directions = {"RIGHT": (0, 1), "DOWN": (
        1, 0), "LEFT": (0, -1), "UP": (-1, 0)}
    next_direction = {"RIGHT": "DOWN",
                      "DOWN": "LEFT", "LEFT": "UP", "UP": "RIGHT"}

    cur = (0, 0)
    while ops > 0:
        for direction in directions:
            for i in range(ops):

                primary_index = non_zero_index(directions[direction])
                new_primary_pos = cur[primary_index] + \
                    directions[direction][primary_index]*(n - origin)

                secondary_direction = next_direction[direction]
                secondary_index = non_zero_index(
                    directions[secondary_direction])
                new_secondary_pos = cur[secondary_index] + \
                    directions[direction][secondary_index]*i

                rotated[new_primary_pos][new_secondary_pos] = matrix[cur[0]][cur[1]]

        origin += 1
        ops -= 2


def non_zero_index(t):
    for i in range(len(t)):
        if t[i] != 0:
            return i


l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotate_90(l)
print(l)
