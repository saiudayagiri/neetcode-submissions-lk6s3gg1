# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]
        
        
        m = len(lists) //2
        left = self.mergeKLists(lists[:m])
        right = self.mergeKLists(lists[m:])

        return self.merge(left, right)
    
    def merge(self, left, right):
        res = dummy = ListNode()
        while left and right:
            if left.val<=right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        dummy.next = left or right
        return res.next

        