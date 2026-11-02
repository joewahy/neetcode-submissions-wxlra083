# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        while list1 != None and list2 != None:
            smaller = list1
            if list1.val < list2.val:
                smaller = list1
                list1 = list1.next
            else:
                smaller = list2
                list2 = list2.next
            
            curr.next = smaller
            curr = curr.next

        if list1 != None:
            curr.next = list1
        if list2 != None:
            curr.next = list2
        return result.next
        