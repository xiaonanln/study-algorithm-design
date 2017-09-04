
class TrieNode(object):

	__slots__ = ('val', 'children')

	def __init__(self, val):
		self.val = val
		self.children = [None] * 26

	def set(self, s, val, idx):
		if idx < len(s):
			c = ord(s[idx]) - ord('a')
			if self.children[c] is None:
				self.children[c] = TrieNode(None)
			self.children[c].set( s, val, idx+1 )
		else:
			self.val = val

	def get(self, s, idx):
		if idx < len(s):
			c = ord(s[idx]) - ord('a')
			if self.children[c] is None:
				return None

			return self.children[c].get( s, idx+1 )
		else:
			return self.val

	def unset(self, s, idx):
		if idx < len(s):
			c = ord(s[idx]) - ord('a')
			if self.children[c] is not None:
				self.children[c] = self.children[c].unset(s, idx+1)

			return self
		else:
			self.val = None
			if not any(self.children): # leaf with val=None should be stripped
				return None

			return self

	def stringsStartWith(self, prefix, idx):
		if idx < len(prefix):
			c = ord(prefix[idx]) - ord('a')
			if self.children[c] is None:
				return {}
			return self.children[c].stringsStartWith(prefix, idx+1)
		else:
			res = {}
			self.getAllStrings(prefix, res)
			return res

	def getAllStrings(self, prefix, res):
		if self.val is not None:
			res[prefix] = self.val

		for c, child in enumerate(self.children):
			if child is None: continue
			child.getAllStrings(prefix+chr(c+ ord('a') ), res)

class Trie(object):

	def __init__(self):
		self.root = TrieNode(None)

	def set(self, s, val):
		self.root.set(s, val, 0)

	def get(self, s):
		return self.root.get(s, 0)

	def stringsStartWith(self, prefix):
		return self.root.stringsStartWith(prefix, 0)

	def unset(self, s):
		self.root.unset(s, 0)

import unittest
class TestTrie(unittest.TestCase):

	def testTrieBasic(self):
		t = Trie()
		t.set('abc', 3)
		t.set('a', 1)
		t.set('abcde', 5)

		print t.get('a')
		print t.get('ab')
		print t.get('abc')
		print t.get('abcd')
		print t.get('abcde')

		print t.stringsStartWith('a')
		print t.stringsStartWith('ab')
		print t.stringsStartWith('abcd')
		print t.stringsStartWith('abcdef')

		t.unset('abcde')
		print t.stringsStartWith('ab')

if __name__ == '__main__':
	unittest.main()
