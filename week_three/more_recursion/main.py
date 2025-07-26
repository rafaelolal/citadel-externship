from sample_data import finalists, all_students, communications

# 1: Using the `finalists` array, write a function that will return all the ways the players can get placed.


def finalist_placements(lst):
    combs = []

    def helper(cur, rest):
        if len(cur) == len(lst):
            combs.append(cur)

        for cand in rest:
            new_rest = rest.copy()
            new_rest.remove(cand)
            helper(cur + [cand], new_rest)

    helper([], lst.copy())
    return combs


result = finalist_placements(finalists)
print(result)
print(len(result))

# 2:  Write a function that finds all the combinations of last 4 finalists that could have ocurred.


def finalist_combinations(lst):
    subs = []

    def helper(i, cur):
        if len(cur) == 4:
            subs.append(cur)

        for j in range(i, len(lst)):
            helper(j + 1, cur + [lst[j]])

    helper(0, [])
    return subs


result = finalist_combinations(all_students)
# print(result)
print(len(result))
print(len(set([tuple(r) for r in result])))
# 10 choose 4 == 210
# 10!/(4! * (10-4)!)

# 3:


def send_message(start, graph):
    path = []
    final_path = []

    def dfs(cur):
        path.append(cur)

        if len(path) == len(graph):
            final_path.append(path.copy())

        for neighbor in graph[cur]:
            if neighbor not in path:
                dfs(neighbor)

        path.pop()

    dfs(start)
    return final_path[0]


print(send_message("Raven", communications))
