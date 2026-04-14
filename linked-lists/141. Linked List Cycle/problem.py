class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        # initialize slow and fast pointers
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


        # while loop - think about when fast can no longer move safely
            
            # move slow one step

            # move fast two steps

            # check if slow and fast have met, if so return True
        
        # if we exit the while loop, what does that mean? return that

# Test 1 - cycle exists
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b  # cycle back to b

# # Test 2 - no cycle
# a = ListNode(1)
# b = ListNode(2)
# a.next = b

# # Test 3 - single node no cycle
# a = ListNode(1)

sol = Solution()
print(sol.hasCycle(a))  # False