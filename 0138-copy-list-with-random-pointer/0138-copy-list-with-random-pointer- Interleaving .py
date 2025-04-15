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
        t = head
        while t:
            curr = Node(t.val)
            curr.next = t.next
            t.next = curr
            t = curr.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        ans = Node(0)
        temp = ans
        while curr:
            temp.next = curr.next
            curr = curr.next.next
            temp = temp.next

        return ans.next
        

        