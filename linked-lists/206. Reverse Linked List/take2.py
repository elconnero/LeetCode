class ListNode:
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return None

        curr = head
        prev = None

        while curr.next:

            placeholder = curr.next
            curr.next = prev
            prev = curr
            curr = placeholder
        
        curr.next = prev
        return curr
    

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

        