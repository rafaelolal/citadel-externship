def is_one_away(orig, other):
    og_len = len(orig)
    ot_len = len(other)
    dif = og_len - ot_len
    if abs(dif) > 1:
        return False

    i, j = 0, 0
    orig_greater = 0
    if dif > 0:
        orig_greater = 1
    elif dif < 0:
        orig_greater = -1

    shorter = min(og_len, ot_len)

    dif_found = False
    while i < shorter and j < shorter:
        if orig[i] != other[j]:
            if dif_found:
                return False

            dif_found = True
            if orig_greater == 1:
                i += 1
            elif orig_greater == -1:
                j += 1
            else:
                i += 1
                j += 1

        else:
            i += 1
            j += 1

    return True


print(is_one_away("pale", "ple"))  # True
print(is_one_away("pales", "pale"))  # True
print(is_one_away("pale", "bale"))  # True
print(is_one_away("pale", "bake"))  # False
print(is_one_away("pale", "paleee"))  # False
print(is_one_away("rafael", "rfel"))  # False
