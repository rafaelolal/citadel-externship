def ideal_days(lst):
    best_buy = 0
    index_best_buy = 0
    max_profit = 0
    index_max_profit = 0
    for i in range(len(lst)):
        if lst[i] < best_buy:
            best_buy = lst[i]
            index_best_buy = i

        if lst[i] - best_buy > max_profit:
            max_profit = lst[i] - best_buy
            index_max_profit = i

    return index_best_buy, index_max_profit


print(ideal_days([100, 40, 50, 300, 100, 1000]))
print(ideal_days([12, 40, 50, 3400, 100, 1000]))
print(ideal_days([12, 40, 50, 3400, 0, 1000][::-1]))
print(ideal_days([3400, 1000, 50, 40, 12, 0]))
