# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        l1_curr = list1
        l2_curr = list2
        while l1_curr != None and l2_curr != None:
            smaller = list1
            if l1_curr.val < l2_curr.val:
                smaller = l1_curr
                l1_curr = l1_curr.next
            else:
                smaller = l2_curr
                l2_curr = l2_curr.next
            
            curr.next = smaller
            curr = curr.next

        if l1_curr != None:
            curr.next = l1_curr
        if l2_curr != None:
            curr.next = l2_curr
        return result.next
        