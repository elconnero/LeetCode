from collections import deque

class TreeNode:
    def __init__(self, data):
        
        self.data  = data
        self.left  = None
        self.right = None

def printTree(root):
    if not root: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

qtyTreeNode = int(input("How many leaves we making son?"))
prev = None
parent = None

for i in range(qtyTreeNode):
    node = TreeNode(i)
    if i == 0:
        root = node
        parent = root
    elif i % 2 == 1:  # odd = left child
        parent.left = node
    elif i % 2 == 0:  # even = right child
        parent.right = node
        parent = parent.left  # move to next parent after assigning both children
printTree(root)