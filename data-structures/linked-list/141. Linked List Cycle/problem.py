class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None: return False
        if head.next == None: return False

        slow = head
        fast = head.next.next


        while head:
            if slow == fast: return True
            else:
                slow = slow.next
                if fast.next.next == None: return False
                else: fast = fast.next.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

sol = Solution()
print(sol.hasCycle(node1))