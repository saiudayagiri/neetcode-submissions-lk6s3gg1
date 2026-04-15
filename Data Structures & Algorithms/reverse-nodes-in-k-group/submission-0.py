# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            while node:
                nxt  = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        
        def kthNode(node,k):
            while node and k>1:
                node = node.next
                k-=1
            return node
        prev = None
        tmp = head
        while tmp :
            kth = kthNode(tmp,k)
            if not kth :
                if prev:
                    prev.next =tmp
                break
            nxt = kth.next
            kth.next = None
            reverse(tmp)
            if tmp==head:
                head=kth
                prev = tmp
                tmp=nxt
            else:
                prev.next=kth
                prev=tmp
                tmp = nxt
                
        return head


        