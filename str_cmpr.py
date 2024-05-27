def str_cmpr(s):
    prev = s[0]
    count = 1
    out = ""
    for c in s[1:]:
        if c != prev:
            out += prev + (str(count) if count > 1 else "")
            prev = c
            count = 1
        else:
            count += 1

    out += prev + (str(count) if count > 1 else "")

    return out


print(str_cmpr("aaaabbbbcccdddd"))
print(str_cmpr("aabbaabb"))
print(str_cmpr("rafael"))
