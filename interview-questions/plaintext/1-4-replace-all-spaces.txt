# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end of the string
# to hold the additional characters, and that you are given the 'true'
# length of the string.
# e.g.
# Input:  'Mr John Smith    '
# Output: 'Mr%20John%20Smith'

import unittest

def replaceSpaces(s):
    # Edge case: no spaces
    if ' ' not in s:
        return s
    
    return s.replace(' ', '%20')

class Test(unittest.TestCase):
    def test_replaceSpaces(self):
        self.assertEqual(replaceSpaces('abc'), 'abc')
        self.assertEqual(replaceSpaces(' a b c '), '%20a%20b%20c%20')
        
if __name__ == '__main__':
    unittest.main()