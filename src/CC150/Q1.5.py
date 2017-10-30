# coding: utf8
# Write a method to replace all spaces in a string with ‘%20’.

def replaceAllSpaces(s):
	return ''.join( c if c != ' ' else '%20' for c in s )

print replaceAllSpaces("a b c")