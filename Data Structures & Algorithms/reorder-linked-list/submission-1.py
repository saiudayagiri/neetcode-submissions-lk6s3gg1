# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        p1 = head
        p2 = head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        second = p1.next
        p1.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first = head
        second = prev
        
        while second:
            p1 = first.next
            p2 = second.next
            first.next = second
            second.next = p1
            first = p1
            second = p2
        


        

        


        