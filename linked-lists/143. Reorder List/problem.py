# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head: return None

        slow = head
        fast = head
        prev = None

        # step 1: find the middle using slow/fast pointers
        # when fast reaches the end, slow is at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        med = slow  # med starts at the middle

        # step 2: reverse the second half of the list
        # same reverse technique you practiced earlier
        while med:
            place_holder = med.next  # save next node before flipping
            med.next = prev          # flip the pointer backwards
            prev = med               # advance prev to current node
            med = place_holder       # advance to next node we saved

        # prev is now the head of the reversed second half
        first = head   # pointer walking through the first half
        second = prev  # pointer walking through the reversed second half

        # step 3: interleave the two halves together
        # stop when second.next is None meaning we've merged everything
        while second.next:
            one_place_holder = first.next   # save next node in first half
            first.next = second             # connect first half node to second half node
            first = one_place_holder        # advance first half pointer

            two_place_holder = second.next  # save next node in second half
            second.next = first             # connect second half node to next first half node
            second = two_place_holder       # advance second half pointer




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
    print(f"current value: {curr.val}")
    curr = curr.next