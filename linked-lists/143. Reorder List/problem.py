# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head: return None

        counter = 1
        curr = head
        n = None

        while curr.next:
            counter += 1
            curr = curr.next
        print(counter)



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

sol = Solution()
sol.reorderList(node1)

curr = node1
while curr:
    print(f"current value{curr.val}")
    curr = curr.next