# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        first, last = 0, len(stack)-1
        while first <= last:
            if stack[first] != stack[last]: return False
            first += 1
            last -= 1
        return True
    
#This is the best run time one.
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res == res[::-1]
"""

#This is the best memory:
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr1 = []
        arr2 = []
        org_head = head
        prev_node, curr_node = None, head

        while org_head:
            arr1.append(org_head.val)
            org_head = org_head.next


        while curr_node:
            nxt_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt_node
        
        while prev_node:
            arr2.append(prev_node.val)
            prev_node = prev_node.next
        
        return arr1 == arr2

"""

a = ListNode(1)
b = ListNode(2)
# c = ListNode(2)
# d = ListNode(1)
a.next = b
# b.next = c
# c.next = d

sol = Solution()
print(sol.isPalindrome(a))