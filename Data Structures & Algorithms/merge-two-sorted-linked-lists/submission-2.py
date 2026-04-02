# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        new=dummy
        i=list1
        j=list2
        while i and j:
            if i.val<j.val:
                new.next=i
                i=i.next
            else:
                new.next=j
                j=j.next
            new=new.next
        if i:
            new.next=i
        if j:
            new.next=j
        return dummy.next                    

        