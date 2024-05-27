def find_k(lst):
    k = 0

    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return i+1

    return k


print(find_k([1, 2, 3, 4, 5]))
print(find_k([4, 5, 1, 2, 3]))
print(find_k([12, 14, 16, 1, 8, 11, 12]))
