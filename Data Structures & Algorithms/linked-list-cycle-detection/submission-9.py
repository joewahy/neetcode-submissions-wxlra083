# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast != None:
            if fast.next == None:
                return False
            if fast.next != None:
                fast = fast.next.next
                slow = slow.next
            if fast != None and slow.val == fast.val:
                return True
        return False