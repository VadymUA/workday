#! /usr/bin/python2.7
#

"""Maintainer: VadymT <help2any1@gmail.com>"""

import sys
import unittest
from app_lib import Calculator, Matrix, Keymap
import app_cli as __unit__


class MyTestCase(unittest.TestCase):
    def test_calculator(self):
        """Checking for the correct answer"""
        numbers = [1, 2, 3, 4, 5, 6]
        target = 12
        expected = '1 * 2 * 6 = 12'
        limit = 1024
        calculator = Calculator(numbers, target, Matrix(numbers, target, Keymap(numbers), limit))
        self.assertEqual(expected, calculator.get_result())

    def test_deviation(self):
        """Checking for the deviated answer"""
        numbers = [1, 2, 3, 4, 5, 6]
        target = 13
        expected = '1 * 2 * 6 = 13'
        limit = 1024
        calculator = Calculator(numbers, target, Matrix(numbers, target, Keymap(numbers), limit))
        self.assertEqual(expected, calculator.get_result())

    def test_cli_calculator(self):
        """Checking CLI for the correct answer"""
        sys.argv = ['app_cli.py', '1', '2', '3', '4', '5', '6', '12']
        expected = '1 * 2 * 6 = 12'
        self.assertEqual(expected, __unit__.main())

    def test_cli_deviation(self):
        """Checking CLI for the deviated answer"""
        sys.argv = ['app_cli.py', '1', '2', '3', '4', '5', '6', '13']
        expected = '1 * 2 * 6 = 13'
        self.assertEqual(expected, __unit__.main())

    def test_cli_missing_parameters(self):
        """Checking CLI for an error for missing parameters"""
        sys.argv = ['app_cli.py']
        expected = 'Usage: app_cli.py 1 2 3 4 5 6 7'
        self.assertEqual(expected, __unit__.main())

    def test_cli_absent_input_number(self):
        """Checking CLI for an error for the absent input number"""
        sys.argv = ['app_cli.py', '1', '2', '3', '4', '5', '6']
        expected = 'Number of arguments is not as expected (6 instead of 7)'
        with self.assertRaises(ValueError) as context:
            __unit__.main()
        self.assertTrue(expected in context.exception)

    def test_cli_excessive_number(self):
        """Checking CLI for an error for the excessive input number"""
        sys.argv = ['app_cli.py', '1025', '2', '3', '4', '5', '6', '12']
        expected = 'All input numbers should be under 1024'
        with self.assertRaises(ValueError) as context:
            __unit__.main()
        self.assertTrue(expected in context.exception)

    def test_cli_excessive_target(self):
        """Checking CLI for an error for the excessive target number"""
        sys.argv = ['app_cli.py', '1', '2', '3', '4', '5', '6', '1025']
        expected = 'All input numbers should be under 1024'
        with self.assertRaises(ValueError) as context:
            __unit__.main()
        self.assertTrue(expected in context.exception)


if __name__ == '__main__':
    del sys.argv[1:]
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
