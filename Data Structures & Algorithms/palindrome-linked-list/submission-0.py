# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next =None
        first = head
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt
        one = head
        two = prev
        while two:
            if one.val!=two.val:
                return False
            one = one.next
            two = two.next
        return True
        