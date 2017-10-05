# coding: utf8
# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring ( i.e., “waterbottle” is a rotation of “erbottlewat”).


def isRotation(s1, s2):
	return len(s1) == len(s2) and s1 in s2+s2

print isRotation("abc", "cab")
print isRotation("abc", "cba")