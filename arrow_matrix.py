from random import randint


def diff(x, y):
    d = x-y
    if d < 0:
        return -1
    elif d > 0:
        return 1
    return d


def arrow_matrix(n, r, c):
    matrix = [[None]*n for _ in range(n)]

    dict = {(0, 0): "0",
            (0, 1): "→",
            (0, -1): "←",
            (1, 0): "↓",
            (-1, 0): "↑",
            (1, 1): "↘",
            (1, -1): "↙",
            (-1, 1): "↗",
            (-1, -1): "↖"}

    for i in range(n):
        for j in range(n):
            rd = diff(r, i)
            cd = diff(c, j)

            matrix[i][j] = dict[(rd, cd)]

    return matrix


for i in range(5):
    n = randint(1, 7)
    r = randint(0, n-1)
    c = randint(0, n-1)

    print("\n".join(map(str, arrow_matrix(n, r, c))))

    print()
    print()
    print()
