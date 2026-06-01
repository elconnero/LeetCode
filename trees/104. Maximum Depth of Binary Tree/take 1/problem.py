# # #Recursive Way DFS
# # # Definition for a binary tree node.
# # # class TreeNode:
# # #     def __init__(self, val=0, left=None, right=None):
# # #         self.val = val
# # #         self.left = left
# # #         self.right = right
# # class Solution:
# #     def maxDepth(self, root: Optional[TreeNode]) -> int:
# #         if not root: return 0
# #         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# #BFS Solution
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0

#         level = 0 
#         q = deque([root])

#         while q:
#             node = q.popleft()
#             if node.left(): q.append(node.left)
#             if node.right(): q.append(node.right)

#         level += 1

#         return level 

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):  # process entire level at once
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1  # increment after each level is done

        return level

# test cases
sol = Solution()

# test 1: [3,9,20,null,null,15,7] → expected 3
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.maxDepth(root))  # 3

# test 2: [1,null,2] → expected 2
root = TreeNode(1)
root.right = TreeNode(2)
print(sol.maxDepth(root))  # 2

# test 3: single node → expected 1
root = TreeNode(1)
print(sol.maxDepth(root))  # 1

# test 4: empty tree → expected 0
print(sol.maxDepth(None))  # 0