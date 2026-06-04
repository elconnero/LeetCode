# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head: return None
        
        dummy = ListNode(0)
        left, right = dummy, dummy
        dummy.next = head

        for i in range(n+1): right = right.next # This is to create the spacing between left and right. This will help ensure that we remove the Nth node from the list. 

        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
    
# Test 1: remove 2nd node from end of [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
result = sol.removeNthFromEnd(head, 2)

curr = result
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
# expected: 1 -> 2 -> 3 -> 5 -> None

# Test 2: remove head (n = length of list)
head2 = ListNode(1)
head2.next = ListNode(2)

result2 = sol.removeNthFromEnd(head2, 2)

curr = result2
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
# expected: 2 -> None

# Test 3: single node
head3 = ListNode(1)
result3 = sol.removeNthFromEnd(head3, 1)
print(result3)
# expected: None





"""
Things I need to think about:

Create a left & right pointer that can move through the link list with the space of N. 
Once right reaches the end of the linked list, left should be at the Nth spot for removal. 

Once at that point we need to think about how we are able to connect the nodes that are between N. 

Also some edge cases we need to think about are lists that are 0 or 1 nodes only. 

"""

"""
PSEDOCODE:

left, right = pointers

create a for loop that iterates through the loop n times so that can create the distance for the right node. 

create a while loop that pushes left and right at the same momentum so it knows where to stop. 

think of a safe way to attach nodes from the left and right together. 

"""