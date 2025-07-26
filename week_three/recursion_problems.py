# START OF PROBLEMS WITH HINTS + SOLUTIONS ========

# IF YOU'RE STUCK, APPLY THE FOLLOWING STRATEGY
# A strategy to help you think it through:
# 1. Can you write out simple examples? Think about the problem in a different way from how it was explicity described?
# 2. What is your base case?
# 3. How can you break the problem down into smaller steps? = When are recursing and what are we putting in as the argument, i.e calling the func_name(...) inside of itself?
# 4. How do we recombine them? = How are we manipulating func_name(...) calls in count ways, if at all?

# Not making sense? No worries! We've provided a solution to the following questions in solution.py, with answers to the above strategy questions as "hints".

# Work your way down the hints, and if it's still not making sense, "code trace" the final solution in solution.py.

# One problem is Medium and the other is Spicy. The solutions are meant to demonstrate how one might go about solving a recursion problem of medium and spicy difficulty.

# PROBLEM 1 (Medium) -------------------
# Staircase Steps: A child is running up a staircase and can walk up 1, 2, or 3 steps at a time. What are all the possible combinations of ways the child can run up the staircase, ending on the final step?

# Example:
# count_ways(1) --> 1
# count_ways(4) --> 7
# count_ways(20) --> 66012

from math import sqrt, floor


def count_ways(num_stairs):
    if num_stairs == 0:
        return 1

    if num_stairs < 0:
        return 0

    return count_ways(num_stairs-1) + count_ways(num_stairs-2) + count_ways(num_stairs-3)


print("count_ways", "-"*20)
for i in range(1, 20):
    print(f"1 {i}: {count_ways(i)}")

# PROBLEM 2 (Spicy) --------------------
# Algebraic Division: Given a string that is a combination of only "(", ")", "/", and integers, evaluate the final value of an algebraic string in the right order based on order of operations (parentheses are evaluated first, and division is done from left to right if there are none). You may not use eval() or any other built in functions. You may assume that all inputs are well formatted (i.e, parentheses are always closed properly, no other characters, etc).
# Examples:
# astr_add("10") --> 10
# astr_add("10/5") --> 2
# astr_add("10/5/2") --> 1
# astr_add("10/(5/2)") --> 4


def astr_div(astr):
    pass  # delete pass and code your solution here

# START OF PROBLEMS WITHOUT SOLUTIONS ========

# PROBLEM 1 (Mild) --------------------
# Recursive Multiply: Write a recursive function to multiply two positive integers a and b without using the * operator.
# Examples:
# r_mult(2, 8) --> 16
# r_mult(10, 20) --> 200


def r_mult(a, b):
    if b == 1:
        return a

    return a + r_mult(a, b-1)


print("r_mult", "-"*20)
print(r_mult(2, 8))
print(r_mult(10, 20))

# PROBLEM 2 (Medium) --------------------
# Coins: Given an infinite number of quarters, dimes, nickels, and pennies, write code to calculate the number of ways of representing n cents.
# Examples:
# make_change(1) --> 1
# make_change(10) --> 4
# make_change(100) --> 293


def make_change(n):
    ways = [0]
    coins = [1, 5, 10, 25]

    def helper(i, s):
        if s == n:
            ways[0] += 1
            return

        if i >= len(coins) or s > n:
            return

        helper(i, s + coins[i])
        helper(i+1, s)

    helper(0, 0)
    return ways[0]


print("make_change", "-"*20)
for i in range(10, 21):
    print(f"{i}: {make_change(i)}")

# PROBLEM 3 (Spicy) --------------------
# Power Set: Given a list of integers and strings, return all possible "subsets" of that list as a list of lists. The order of the subsets does not matter, but you may not have "duplicate" lists (i.e have two lists that contain the same elements in a different order)
# Examples:
# power_set(["hi", 1]) --> [["hi"], [1]]
# power_set([1, "hi", 3]) --> [["hi"], [1], [3], [1, "hi"], [1, 3], ["hi", 3]]


def power_set(lst):
    subs = []

    def helper(i, cur):
        if cur and len(cur) != len(lst):
            subs.append(cur)

        for j in range(i, len(lst)):
            helper(j + 1, cur + [lst[j]])

    helper(0, [])
    return subs


print("power_set", "-"*20)
print(power_set(["hi", 1]))
print(power_set([1, 2, 3]))
print(power_set([1, 2, 3, 4, 5]))

# PROBLEM 4 (Spicy) --------------------
# Parentheses: You are given n number of open and close parenthesis. Return a list of all of the possible combinations of valid parentheses.
# Examples:
# valid_parens(1) --> ["()"]
# valid_parens(2) --> ["()()", "(())"]
# valid_parens(3) --> ["()()()", "(())()", "((()))", "(()())", "()(())"]


def valid_parens(n):
    combs = []

    def helper(o, c, cur):
        if len(cur) == 2*n:
            combs.append(cur)
            return

        if o:
            helper(o-1, c, cur + "(")
        if o < c:
            helper(o, c-1, cur + ")")

    helper(n, n, "")
    return combs


print("valid_parens", "-"*20)
print(valid_parens(1))
print(valid_parens(2))
print(valid_parens(3))

# PROBLEM 5 (Medium - Spicy) --------------------
# Consider the following one player game. An instance of the game is defined by two integers n and m where m < n.
# The game begins with a number n written on a board. At each step of the game, the player can choose any number k on the board and take one of the following actions:
# (1) Replace k with floor(k/3) and k - floor(k/3),
# (2) Replace k with floor(sqrt(k)) and k - floor(sqrt(k))
# note: floor() means squaring down
# The player wins if the number m appears on the board.

# Example:
# n = 100, m = 10
# Board: 100
# Perform action (2) on n:
# Board is now: 100 sqrt(100) 100 - sqrt(100)
# Board is now: 100 10 90
# It is possible to win the game since we have reached 10.

# Write the function can_win(n, m), which determines whether it is possible for a player to win the game given n and m.
# (Spicy) Instead of determining whether the player can win, instead determine the minimum number of steps it would take to win.
# Examples
# can_win(100, 10) --> True
# 100 -(1)-> 90 10
# can_win(100, 90) --> True
# 100 -(1)-> 90 10
# can_win(100, 80) --> False
# 100 -(1)-> 90 10
# 90 -(1)-> 9 81
# 81 -(1)-> 9 72...
# 100 -(2)-> 33 66...


def can_win(n, m):
    if n == m:
        return True

    if n < m:
        return False

    return (can_win(floor(n/3), m)
            or can_win(n - floor(n/3), m)
            or can_win(floor(sqrt(n)), m)
            or can_win(n - floor(sqrt(n)), m))


print("can_win", "-"*20)
print(can_win(100, 90))
