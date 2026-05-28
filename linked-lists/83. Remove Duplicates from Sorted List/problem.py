# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val: curr.next = curr.next.next
            else: curr = curr.next
        return head

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
print_list(sol.deleteDuplicates(make_list([1, 1, 2])))        # 1 -> 2 -> None
print_list(sol.deleteDuplicates(make_list([1, 1, 2, 3, 3]))) # 1 -> 2 -> 3 -> None
print_list(sol.deleteDuplicates(make_list([1, 1, 1])))        # 1 -> None
print_list(sol.deleteDuplicates(make_list([1, 2, 3])))        # 1 -> 2 -> 3 -> None
print_list(sol.deleteDuplicates(make_list([])))               # None