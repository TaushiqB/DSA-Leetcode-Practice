# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        
        while list1:
            ans.append(list1.val)
            list1 = list1.next
        while list2:
            ans.append(list2.val)
            list2 = list2.next
        ans = sorted(ans)

        if ans == []:
            return None

        a = ListNode(ans[0])
        curr = a
        for i in range(1, len(ans)):
            curr.next = ListNode(ans[i])
            curr = curr.next
        return a