# Implement a mathod to perform basic string compression using the counts
# of repeated characters. For example, the string aabccccaaa would become 
# a2b1c5a3. If the 'compressed' string would not become smaller than the
# original string, your method should return the original string. You can assume
# the string has only uppper and lower case letters (a - z)

import unittest

def compress(s):
    # Base case: not compressible
    # In other words, given string has only 1 of each letter
    if len(s) == len(set(s)):
        return s
    
    # Build dictionary for the counts of each letter
    counts = dict()
    for i in range(len(s)):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
        
    result = ''
    for d in counts:
        result += str(d) + str(counts[d])
    
    return result


class Test(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress('abc'),'abc')
        self.assertEqual(compress('abbcccdddd'),'a1b2c3d4')


if __name__ == '__main__':
    unittest.main()
    

#
#
#s = 'abbcccdddd'
#counts = dict()
#for i in range(len(s)):
#    if s[i] not in counts:
#        counts[s[i]] = 1
#    else:
#        counts[s[i]] += 1
#
#result = ''
#for d in counts:
#    result += str(d) + str(counts[d])
#
#print(result)
#
#print(str(counts))
#
#
#result.append('blah').append('hey')
#print(result)