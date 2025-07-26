def k_rot(lst, k):
    for _ in range(k):
        lst.insert(0, lst.pop())

    return lst


print(k_rot([1, 2, 3, 4, 5], 1))
print(k_rot([1, 2, 3, 4, 5], 2))
print(k_rot([1, 2, 3, 4, 5], 3))
