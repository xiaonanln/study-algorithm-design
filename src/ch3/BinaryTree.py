

class TreeNode(object):
	__slots__ = ('val', 'left', 'right', 'parent')
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None

def Search(root, val):
	if root is None or root.val == val:
		return root

	elif val < root.val:
		return Search(root.left, val)
	else:
		return Search(root.right, val)

def Insert(root, val):
	if root is None:
		return TreeNode(val)

	if val < root.val:
		root.left = Insert(root.left, val)
	elif val > root.val:
		root.right = Insert(root.right, val)

	return root

def Remove(root, val):
	if root is None:
		return None

	if val == root.val:
		if root.left is None and root.right is None:
			return None
		elif root.left is None:
			return root.right
		elif root.right is None:
			return root.left
		else:
			root.val = removeLeftMost(root.right, root, False)
			return root
	elif val < root.val:
		root.left = Remove(root.left, val)
	else:
		root.right = Remove(root.right, val)

	return root

def removeLeftMost(root, parent, isLeftChild):
	while root.left is not None:
		root, parent = root.left, root
		isLeftChild = True

	if isLeftChild:
		parent.left = root.right
	else:
		parent.right = root.right

	return root.val

def InOrder(root, f):
	if root is None:
		return

	InOrder(root.left, f)
	f(root.val)
	InOrder(root.right, f)

def PreOrder(root, f):
	if root is None:
		return

	f(root.val)
	PreOrder(root.left, f)
	PreOrder(root.right, f)

def PostOrder(root, f):
	if root is None:
		return

	PostOrder(root.left, f)
	PostOrder(root.right, f)
	f(root.val)




