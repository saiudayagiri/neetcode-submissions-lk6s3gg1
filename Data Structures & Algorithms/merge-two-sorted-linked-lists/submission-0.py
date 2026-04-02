# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i=list1
        j=list2
        k=dummy=ListNode(0)
        while i and j:
            if i.val<=j.val:
                k.next=i
                i=i.next
                k=k.next
            else:
                k.next=j
                j=j.next
                k=k.next
        if i:
            k.next=i
        if j:
            k.next=j            
        return dummy.next            

        