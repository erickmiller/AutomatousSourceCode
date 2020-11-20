# Quick Sort

def sort(t):
    if t == []:
        return []
    else:
        pivot = t[0]
        left = [x for x in t if x < pivot]
        right = [x for x in t[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]
    
def sorted(t):
# inorder traversal of BST
    return [] if t == [] else sorted(t[0]) + [t[1]] + sorted(t[2])
        
def search(t, x):
    return len(_search(t,x)) > 0

def insert(t, x):
    subtree = _search(t, x)
    if subtree == []:	
    	subtree += [[], x, []]

def _search(t, x):
    # search helper function
    if t == [] or x == t[1]:
        return t
    elif x < t[1]:
        return _search(t[0], x)
    else:
        return _search(t[2], x)

print ">>> tree = sort([4,2,6,3,5,7,1,9])"
tree = sort([4,2,6,3,5,7,1,9])
print tree
print ">>> sorted(tree)"
print sorted(tree)
print ">>> search(tree, 6)"
print search(tree, 6)
print ">>> search(tree, 6.5)"
print search(tree, 6.5)
print ">>> insert(tree, 6.5)"
print insert(tree, 6.5)
print ">>> tree"
print tree
print ">>> insert(tree, 3)"
print insert(tree, 3)
print ">>> tree"
print tree
print
print
print ">>> tree = sort([4,2,6,3,5,7,1,9])"
tree = sort([4,2,6,3,5,7,1,9])
print tree
print ">>> _search(tree, 3)"
print _search(tree, 3)
print ">>> _search(tree, 0)"
print _search(tree, 0)
print ">>> _search(tree, 6.5)"
print _search(tree, 6.5)
print ">>> _search(tree, 0) is _search(tree, 6.5)"
print _search(tree, 0) is _search(tree, 6.5)
print ">>> _search(tree, 0) == _search(tree, 6.5)"
print _search(tree, 0) == _search(tree, 6.5)





