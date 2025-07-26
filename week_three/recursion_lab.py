# Mild

# 1. Write a function for the factorial of a number
# ex. 3! = 3*2*1 = 6 -- 5! = 5*4*3*2*1 = 120

def factorial(x):
    if x == 1:
        return x

    return x * factorial(x-1)

# for i in range(1, 10):
#   print(factorial(i))

# 2. Write a function that computes the sum of the digits of a number.
# ex. 2148 => (2+1+4+8) = 15


def digit_sum(x):
    if x // 10 == 0:
        return x

    return x % 10 + digit_sum(x//10)

# print(digit_sum(2148))

# 3. Write a function that reverses the order of a list.
# ex. [1, 2, 3, 4, 5] => [5, 4, 3, 2, 1]


def reverse_list(l, i=0):
    if i > len(l) // 2:
        return

    l[i], l[-(i+1)] = l[-(i+1)], l[i]
    reverse_list(l, i+1)


l = [1, 2, 3, 4, 5]
reverse_list(l)
print(l)

# Medium

# 4. Every number can be represented as a "single digit". Write a function that converts any number to it's "single digit" form
# ex. 7 => 7 -- 57 (5+7) => 12 (1+2) => 3 -- 159 => 15 => 6


def to_single_digit(x):
    if x // 10 == 0:
        return x

    return to_single_digit(x % 10 + x//10)

# print(to_single_digit(7))
# print(to_single_digit(57))
# print(to_single_digit(159))


# 5. Would you rather have a million dollars or a penny that doubles in size for a month (30 days)?
# Write a function that finds how much a penny doubled for 30 days is.

def double(value, days):
    if days == 0:
        return value

    return double(value*2, days-1)


print(double(0.01, 30))

# 6. Is the number prime? Can it only be divided by itself and 1? Write a function that determines whether or not a number is prime.
# ex. 7 is prime (factors: 1, 7) but 10 is not (factors: 1, 2, 5, 10)
# Hint: Check 2 first (by default) and work your way up until you hit the original number.


def is_prime(x, i=2):
    if i > x//2:
        return True

    if x % i == 0:
        return False

    return is_prime(x, i+1)

# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))
# print(is_prime(7))
# print(is_prime(11))
# print(is_prime(13))
# print(is_prime(20))
# print(is_prime(37))
