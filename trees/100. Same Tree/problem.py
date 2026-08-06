# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q: return True   # both None → same
            if not p or not q: return False   # one None, one not → different
            if p.val != q.val: return False   # different values → different
            
            # recurse both sides simultaneously
            left  = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            
            return left and right  # both sides must match
        return dfs(p, q)
    #Keep it up