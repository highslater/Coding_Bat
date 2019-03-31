#!/usr/local/bin/python3.7

"""Docstring."""


# 1
def sleep_in(weekday, vacation):
    """Warmup-1 > sleep_in."""
    return not weekday or vacation

'''
The parameter weekday is True if it is a weekday, and the parameter vacation
is True if we are on vacation. We sleep in if it is not a weekday or we're
on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
# print(sleep_in(False, False))
# print(sleep_in(True, False))
# print(sleep_in(False, True))


# 2
def monkey_trouble(a_smile, b_smile):
    """Warmup-1 > monkey_trouble."""
    return (a_smile and b_smile) or (not a_smile and not b_smile)

'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
if each is smiling. We are in trouble if they are both smiling or if neither
of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''
# print(monkey_trouble(True, True))
# print(monkey_trouble(False, False))
# print(monkey_trouble(True, False))


# 3
def sum_double(a, b):
    """Warmup-1 > sum_double."""
    return [a + b, 2 * (a + b)][a == b]

'''
Given two int values, return their sum. Unless the two values are the same,
then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''
# print(sum_double(1, 2))
# print(sum_double(3, 2))
# print(sum_double(2, 2))


# 4
def diff21(n):
    """Warmup-1 > diff21."""
    a = abs(n - 21)
    return [a, a * 2][n > 21]

'''
Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''
# print(diff21(19))
# print(diff21(10))
# print(diff21(21))


# 5
def parrot_trouble(talking, hour):
    """Warmup-1 > parrot_trouble."""
    return talking and (7 > hour or hour > 20)

'''
We have a loud talking parrot. The "hour" parameter is the current hour time
in the range 0..23. We are in trouble if the parrot is talking and the hour
is before 7 or after 20. Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
'''
# print(parrot_trouble(True, 6))
# print(parrot_trouble(True, 7))
# print(parrot_trouble(False, 6))


# 6
def makes10(a, b):
    """Warmup-1 > makes10."""
    return (a == 10 or b == 10) or a + b == 10

'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''
# print(makes10(9, 10))
# print(makes10(9, 9))
# print(makes10(1, 9))


# 7
def near_hundred(n):
    """Warmup-1 > near_hundred."""
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

'''
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''
# print(near_hundred(93))
# print(near_hundred(90))
# print(near_hundred(89))


# 8
def pos_neg(a, b, negative):
    """Warmup-1 > pos_neg."""
    return [a < 0 and b > 0 or a > 0 and b < 0,
            a < 0 and b < 0][negative]

'''
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True,
then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''
# print(pos_neg(1, -1, False))
# print(pos_neg(-1, 1, False))
# print(pos_neg(-4, -5, True))


# 9
def not_string(str):
    """Warmup-1 > not_str."""
    return ['not ' + str, str][str.startswith('not')]

'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
'''
# print(not_string('candy'))
# print(not_string('x'))
# print(not_string('not bad'))


# 10
def missing_char(str, n):
    """Warmup-1 > missing_char."""
    return str[:n] + str[n + 1:]

'''
Given a non-empty string and an int n, return a new string where the char at
index n has been removed. The value of n will be a valid index of a char in
the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
'''


# 11
def front_back(str):
    """Warmup-1 > front_back."""
    if len(str) >= 2:
        f = str[0]
        b = str[-1]
        m = str[1:-1]
        return b + m + f
    else:
        return str

'''
Given a string, return a new string where the first and last chars have
been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''
# print(front_back('code'))
# print(front_back('a'))
# print(front_back('ab'))


# 12
def front3(str):
    """Warmup-1 > front3."""
    if len(str) >= 3:
        return (str[0:3]) * 3
    else:
        return str * 3

'''
Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there.
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
'''
# print(front3('Java'))
# print(front3('Chocolate'))
# print(front3('abc'))
