#!/usr/local/bin/python3.7

"""Docstring."""


# 1
def string_times(str, n):
    """Warmup-2 > string_times."""
    return str * n

'''
Given a string and a non-negative int n, return a larger string that is
n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''
# print(string_times('Hi', 2))
# print(string_times('Hi', 3))
# print(string_times('Hi', 1))


# 2
def front_times(str, n):
    """Warmup-2 > front_times."""
    return [str * n, str[:3] * n][len(str) >= 3]

'''
Given a string and a non-negative int n, we'll say that the front of the
string is the first 3 chars, or whatever is there if the string is less than
length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''
# print(front_times('Chocolate', 2))
# print(front_times('Chocolate', 3))
# print(front_times('Abc', 3))


# 3
def string_bits(str):
    """Warmup-2 > string_bits."""
    s2 = []
    for i in range(0, len(str), 2):
        s2.append(str[i])
    return ''.join(s2)

'''
Given a string, return a new string made of every other char starting with
the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''
# print(string_bits('Hello'))
# print(string_bits('Hi'))
# print(string_bits('Heeololeo'))


# 4
def string_splosion(str):
    """Warmup-2 > string_splosion."""
    s = ''
    for i in range(len(str)):
        s += str[:i + 1]
    return s

'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''
# print(string_splosion('Code'))
# print(string_splosion('abc'))
# print(string_splosion('ab'))


# 5
def last2(str):
    """Warmup-2 > last2."""
    c, i = 0, 0
    while i < len(str) - 2:
        if str[i] + str[i + 1] == str[-2:]:
            c += 1
        i += 1
    return c

'''
Given a string, return the count of the number of times that a substring
length 2 appears in the string and also as the last 2 chars of the string,
so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''
# print(last2('hixxhi'))
# print(last2('xaxxaxaxx'))
# print(last2('axxxaaxx'))


# 6
def array_count9(nums):
    """Warmup-2 > array_count9."""
    c = 0
    for num in nums:
        if num == 9:
            c += 1
    return c

'''
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''
# print(array_count9([1, 2, 9]))
# print(array_count9([1, 9, 9]))
# print(array_count9([1, 9, 9, 3, 9]))


# 7
def array_front9(nums):
    """Warmup-2 > front9."""
    return 9 in nums[:4]

'''
Given an array of ints, return True if one of the first 4 elements in the
array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''
# print(array_front9([1, 2, 9, 3, 4]))
# print(array_front9([1, 2, 3, 4, 9]))
# print(array_front9([1, 2, 3, 4, 5]))


# 8
def array123(nums):
    """Warmup-2 > array123."""
    return 1 in nums and 2 in nums and 3 in nums

'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3
appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''
# print(array123([1, 1, 2, 3, 1]))
# print(array123([1, 1, 2, 4, 1]))
# print(array123([1, 1, 2, 1, 2, 3]))


# 9
def string_match(a, b):
    """Warmup-2 > string_match."""
    n = [len(a), len(b)][len(a) > len(b)] - 1
    c, i = 0, 0
    while i < n:
        if a[i] + a[i + 1] == b[i] + b[i + 1]:
            c += 1
        i += 1
    return (c)

'''
Given 2 strings, a and b, return the number of the positions where they
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
since the "xx", "aa", and "az" substrings appear in the same place in both
strings.
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''
# print(string_match('xxcaazz', 'xxbaaz'))
# print(string_match('abc', 'abc'))
# print(string_match('abc', 'axc'))
