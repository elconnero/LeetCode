#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None

        tmp = root.left
        root.left  = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
#DFS type problem

def print_tree(root):
    if not root: return "None"
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

sol = Solution()

# test 1: basic tree [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(print_tree(sol.invertTree(root)))

# test 2: two nodes [2,1,3] → [2,3,1]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(print_tree(sol.invertTree(root)))

# test 3: empty tree
print(print_tree(sol.invertTree(None)))

# test 4: single node
root = TreeNode(1)
print(print_tree(sol.invertTree(root)))

# test 5: left-skewed tree [1,2,3,null,null]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(print_tree(sol.invertTree(root)))