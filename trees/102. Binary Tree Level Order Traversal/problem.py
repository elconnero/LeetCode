from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return None

        
        q = deque([root])
        res = []
        
        

        while q:
            level_size = len(q)
            level_list = []
            for i in range(level_size):
                node = q.popleft()
                level_list.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_list)
            

        return res


# test cases
sol = Solution()

# test 1: [3,9,20,null,null,15,7] → expected 3
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.levelOrder(root))  # 3
