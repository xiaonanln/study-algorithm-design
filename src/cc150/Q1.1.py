"""
Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
"""

def isUnique(s):
	exists = [False] * 256
	for c in s:
		oc = ord(c)
		if exists[oc]:
			return False
		exists[oc] = True

	return True

assert isUnique("abc") == True
assert isUnique("abcc") == False