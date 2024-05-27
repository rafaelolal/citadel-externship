def rotate_str(s, n):
    l = list(s)
    n = n % len(s)
    return s[-n:] + s[:-n]


print(rotate_str("hello world", 2))
