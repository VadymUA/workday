#! /usr/bin/python2.7
#

"""
Maintainer: VadymT <help2any1@gmail.com>
"""

import sys
from string import join
from itertools import combinations


class Keymap():
    def __init__(self, numbers):
        self.numbers = numbers
        self.keymap = [_s for _i in range(2, self.__len__()) for _s in combinations(range(0, self.__len__()), _i)]

    def __iter__(self):
        return self.keymap.__iter__()

    def __len__(self):
        return len(self.numbers)


class Matrix():
    def __init__(self, numbers, target, keymap, limit):
        self.numbers = numbers
        self.target = target
        self.keymap = keymap
        self.limit = limit
        self.matrix = {_key: self.multiply(_key) for _key in self.keymap}

    def get_key(self):
        """Return a key from the matrix"""
        _diff = (self.limit - 1) * (self.limit - 2)  # max value (1023*1022)
        key = ''
        for _k, _v in self.matrix.iteritems():
            if _v == self.target:
                return _k
            deviation = abs(self.target - _v)
            if deviation < _diff:
                _diff = deviation
                key = _k
        return key

    def multiply(self, combination, value=1):
        """Return a result of multiplying for specified combination"""
        for _c in combination:
            value *= self.numbers[_c]
        return value


class Calculator():
    def __init__(self, numbers, target, matrix):
        self.numbers = numbers
        self.target = target
        self.matrix = matrix

    def get_result(self):
        """Return a key from the matrix"""
        return self.format_result(self.matrix.get_key())

    def format_result(self, key):
        """Return the formatted result as *number + number (+ number) = target*"""
        res = [self.numbers[key[_k]] for _k in range(len(key))]
        return ('%s = %s' % (' * '.join(map(str, res)), self.target))
