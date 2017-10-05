import sys

def mdarray(initVal, *dims): return [initVal] * dims[0] if len(dims) == 1 else [ mdarray(initVal, *dims[1:]) for _ in xrange(dims[0])]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode<' + str(self.val) + '>'

    def __getitem__(self, idx):
        p = self
        while idx > 0:
            idx -= 1
            p = p.next

        return p


def printlist(head):
    n = head
    vals = []
    while n is not None:
        vals.append(n.val)
        n = n.next
        
    print '->'.join(map(str, vals)) + '->[end]'
    
def makelist(*values):
    if len(values) == 1 and isinstance(values[0], list):
        values = values[0]
        
    if not values: return None
    head = None
    prev = None
    for val in values:
        node = ListNode(val)
        if head is None:
            head = node
            prev = node
        else:
            prev.next = node
            prev = node
    
    return head

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maketree(values):
    if len(values) == 1 and isinstance(values[0], list):
        values = values[0]
        
    if not values: return None
    root = TreeNode(values[0])
    next = 1
    deepest = [root]
    
    while next < len(values):
        assert deepest, (deepest, values)
        new_deepest = []
        for node in deepest:
            node.left = TreeNode(values[next]) if next < len(values) and values[next] is not None else None
            node.right = TreeNode(values[next+1]) if next+1 < len(values) and values[next+1] is not None else None
            if node.left: 
                new_deepest.append(node.left)
            if node.right: 
                new_deepest.append(node.right)
                
            next += 2
        
        deepest = new_deepest
    
    return root

def printtree(root):
    if root is None: print 'EMPTY TREE'
    _printtree(root, 0)
    
def _printtree(root, level):
    if root is None: return 
     
    print ('\t' * level) + str(root.val)
    _printtree(root.left, level+1)
    _printtree(root.right, level+1)
    
