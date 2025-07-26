def rotated_is_increasing(lst, k):
    i = k
    for _ in range(len(lst) - 1):
        ni = (i + 1) % len(lst)
        if lst[i] > lst[ni]:
            return False

        i = ni

    return True


print(rotated_is_increasing([1, 2, 3, 4, 5], 1))
print(rotated_is_increasing([1, 2, 3, 4, 5], 0))
print(rotated_is_increasing([5, 1, 2, 3, 4], 1))
