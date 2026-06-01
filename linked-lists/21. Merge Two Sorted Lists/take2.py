class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        while list1 and list2: #n
            if list1.val < list2.val: #n
                tail.next = list1 #n
                list1 = list1.next #n
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1: tail.next = list1
        elif list2: tail.next = list2

        return dummy