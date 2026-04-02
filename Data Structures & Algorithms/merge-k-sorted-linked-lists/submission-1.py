from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None  # Edge case: empty list
        if len(lists) == 1:
            return lists[0]  # Only one list, return as is
        
        # Step 1: Divide the lists into two halves
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])  
        right = self.mergeKLists(lists[mid:])  
        
        # Step 2: Merge the two halves
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to start the merged list
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next  # Move the tail pointer forward

        # Attach the remaining elements from either left or right
        tail.next = left if left else right
        
        return dummy.next  # Return the merged list (skip dummy node)
