#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class Testing(unittest.TestCase):

    def basic_test(self):
        testcase = "Faizan, Muhammad"
        expected = "Muhammad Faizan"
        self.assertEqual(rearrange_name(testcase), expected)

    def empty_test(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase =  "Companiz Ltd., Faiziz"
        expected = "Faiziz Companiz Ltd."
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase =  "Palindrome"
        expected = "Palindrome"
        self.assertEqual(rearrange_name(testcase), expected)

# Run the testing to the file:
if __name__ == "__main__":
    unittest.main()
