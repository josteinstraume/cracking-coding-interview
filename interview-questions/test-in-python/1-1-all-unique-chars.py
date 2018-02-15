# 1.1) Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def allUnique(s):
	# Corner case: string has zero characters
    if len(s) == 0:
        return 'String has no characters!'

	# Base case: string has only one character
    if len(s) == 1:
        return 'String has all unique characters!'

    if len(s) == len(set(s)):
        return 'String has all unique characters!'
	
    return 'String does not have all unique characters!'


def allUnique2(s):
    return len(s) == len(set(s))

def allUniqueDictionary(s):
    s = s.replace(' ', '')
    chars = set()
    
    for c in s:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True
    

test1 = ''
test2 = 'a'
test3 = 'abcd'
test4 = 'aabc'

