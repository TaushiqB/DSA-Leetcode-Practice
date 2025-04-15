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
        if head == None:
            return None
        h = {}
        t = head

        while t:
            n = Node(t.val)
            h[t] = n
            t = t.next

        t = head
        while t:
            c = h[t]
            c.next = h.get(t.next)
            c.random = h.get(t.random)
            t = t.next

        return h[head]
        