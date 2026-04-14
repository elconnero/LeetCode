# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.output = []

        def dfs(node, path, sum):
            sum += node.val
            temp = path + [node.val]

            if node.left:  dfs(node.left,  temp, sum)
            if node.right: dfs(node.right, temp, sum)
            if not node.right and not node.left and sum == targetSum:
                self.output.append(temp) 
        if not root: return []
        dfs(root, [], 0)
        return self.output

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

test = Solution()
output = test.pathSum(root, 22)
print(output)  # Expected: [[5,4,11,2], [5,8,4,5]]