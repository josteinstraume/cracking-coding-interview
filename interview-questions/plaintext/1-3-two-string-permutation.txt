# Given two strings, write a method to decide if one is a permutation of the other.

# Not assuming the permutated string can be a subset of the other
# e.g. 'afg' is not a permutation of 'abcdefg'

import unittest

def isPerm(s1, s2):
    # If the two strings are of unequal length, then we automatically know
    # that one cannot be the anagram of the other.
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

class Test(unittest.TestCase):
    def test_isPerm(self):
        self.assertEqual(isPerm('abc', 'abcd'), False)
        self.assertEqual(isPerm('abc', 'cab'), True)


if __name__ == '__main__':
    unittest.main()
    