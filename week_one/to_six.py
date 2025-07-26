def has_six_reduction(num):
    while num > 9:
        cur_num = num
        reduction = 0
        while cur_num > 0:
            reduction += cur_num % 10
            cur_num //= 10

        num = reduction

    if num == 6:
        return True

    return False


print(has_six_reduction(123))
print(has_six_reduction(99996))
print(has_six_reduction(19929))
