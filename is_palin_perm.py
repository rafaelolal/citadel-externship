def is_palin_perm(s):
    s = s.lower().replace(' ', '')

    count = [0]*26
    for c in s:
        count[ord(c)-97] += 1

    odd_found = False
    for elem in count:
        if elem % 2 == 1:
            if odd_found:
                return False

            odd_found = True

    return True


print(is_palin_perm("Tact Coa"))
