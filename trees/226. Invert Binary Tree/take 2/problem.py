
class TreeNode:
    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()
result = sol.invertTree(root)

def printTree(node):
    if not node: return
    print(node.val)
    printTree(node.left)
    printTree(node.right)

printTree(result)