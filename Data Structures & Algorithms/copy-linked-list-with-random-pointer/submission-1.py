"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        cur = head
        original_to_duplicate = {}
        while cur:
            original_to_duplicate[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                original_to_duplicate[cur].next = original_to_duplicate[cur.next]
            if cur.random:
                original_to_duplicate[cur].random = original_to_duplicate[cur.random]
            cur = cur.next
        return original_to_duplicate[head]
        