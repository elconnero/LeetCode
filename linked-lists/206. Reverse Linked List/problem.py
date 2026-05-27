# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return None  # guard against empty list

        curr = head  # curr starts at the head of the list
        prev = None  # prev starts as None because the first node will point to None when reversed

        while curr.next:  # keep going until we reach the last node

            pholder = curr.next  # save the next node before we lose it by flipping the arrow
            curr.next = prev     # flip the arrow, curr now points backwards to prev
            prev = curr          # move prev forward to where curr is
            curr = pholder       # move curr forward to the next node we saved
        
        curr.next = prev  # flip the last node
        return curr       # last node is now the new head
                    

def make_list(vals):
    if not vals: return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

sol = Solution()
print_list(sol.reverseList(make_list([1, 2, 3, 4, 5])))  # 5 -> 4 -> 3 -> 2 -> 1 -> None
print_list(sol.reverseList(make_list([1, 2])))            # 2 -> 1 -> None
print_list(sol.reverseList(make_list([1])))               # 1 -> None
print_list(sol.reverseList(make_list([])))     