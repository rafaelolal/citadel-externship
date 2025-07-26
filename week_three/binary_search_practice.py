def binary_search(lst, target, i, j):
    mid = (i + j) // 2
    if lst[mid] == target:
        return mid

    if i == j:
        return - 1

    elif lst[mid] < target:
        return binary_search(lst, target, mid+1, j)

    return binary_search(lst, target, i, mid-1)


l = list(range(15))

print(binary_search(l, -15, 0, len(l)-1))
for i in range(15):
    print(binary_search(l, i, 0, len(l)-1))
print(binary_search(l, 15, 0, len(l)-1))


# PRACTICE PROBLEM -------------------
# Magic Index: A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# Magic Index: A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.

# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A. # Example:

# magic_index([0, 2, 3, 4, 5]) --> 0
# magic_index([-1, 0, 1, 3, 5]) --> 3
# magic_index([1, 2, 3, 4, 5]) --> -1

# Not making sense? No worries! We've provided a solution in solutions.py, with answers to the above strategy questions as "hints". Work your way down the hints, and if it's still not making sense, "code trace" the final solution in solutions.py.

def magic_index(arr):
    def binary_search(i, j):
        mid = (i + j) // 2

        if i > j or mid > len(arr) - 1:
            return -1

        if arr[mid] == mid:
            return mid

        elif arr[mid] < mid:
            return binary_search(mid+1, j)

        return binary_search(i, mid-1)

    return binary_search(0, len(arr))


print(magic_index([0, 2, 3, 4, 5]))  # 0
print(magic_index([-1, 0, 1, 3, 5]))  # 3
print(magic_index([1, 2, 3, 4, 5]))  # -1, right shifted
print(magic_index([-1, 0, 1, 2, 3]))  # -1, left shifted
