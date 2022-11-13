from functools import reduce


def str2float(s):
    DIGITS = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }
    L = s.split('.')

    def fn(x, y):
        return x * 10 + y

    def str_int(i):
        return DIGITS[i]

    return reduce(fn, map(
        str_int, L[0])) + reduce(fn, map(str_int, L[1])) / (10**len(L[1]))
