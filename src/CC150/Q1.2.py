#coding: utf8
"""
Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)
"""


def reverseCStyleString(s):
	i, j = 0, 0
	while s[j] != '\0':
		j += 1

	j -= 1
	while i < j:
		s[i], s[j] = s[j], s[i]
		i += 1; j -= 1
	return s

print reverseCStyleString(['a', 'b', 'c', '\0'])