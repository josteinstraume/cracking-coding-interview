import unittest

def reverse(s):
    return s[::-1]

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse(''), '')
        self.assertEqual(reverse('abc'), 'cba')
        self.assertEqual(reverse('zz-1'), '1-zz')

if __name__ == '__main__':
    unittest.main()

