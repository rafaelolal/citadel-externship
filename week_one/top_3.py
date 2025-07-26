def top_3(nums):
    top = [float('-inf'), float('-inf'), float('-inf')]
    for n in nums:
        for i, t in enumerate(top):
            if n not in top and n > t:
                top.insert(i, n)
                top.pop()
                break

    return top


print(top_3([1, 2, 3, 4, 5]))
print(top_3([100, 101, 101, 101, 102, 102, 103]))
