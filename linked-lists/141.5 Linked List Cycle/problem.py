# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True
        return False
    

def make_list(vals):
    if not vals: return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head, curr  # return tail too so we can create a cycle

sol = Solution()

# No cycle
head, tail = make_list([1, 2, 3, 4])
print(sol.hasCycle(head))  # False

# Cycle: tail points back to head
head, tail = make_list([1, 2, 3, 4])
tail.next = head
print(sol.hasCycle(head))  # True

# Cycle: tail points back to middle
head, tail = make_list([1, 2, 3, 4])
tail.next = head.next
print(sol.hasCycle(head))  # True

# Single node no cycle
head, tail = make_list([1])
print(sol.hasCycle(head))  # False