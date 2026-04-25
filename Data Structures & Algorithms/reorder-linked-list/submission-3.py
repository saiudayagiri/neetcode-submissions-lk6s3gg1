# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev

            prev = second
            second = nxt
        second = prev
        final = dummy = ListNode()
        while first and second:
            temp1 = first.next
            temp2 = second.next
            dummy.next = first
            dummy.next.next = second
            first = temp1
            second = temp2
            dummy = dummy.next.next
        dummy.next = first or second
        head = dummy.next


        