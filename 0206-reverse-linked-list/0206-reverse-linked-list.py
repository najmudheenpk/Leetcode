# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 

        current = head 
        previous = None 


        while current:
            near = current.next
            current.next = previous
            previous = current
            current = near

        return previous