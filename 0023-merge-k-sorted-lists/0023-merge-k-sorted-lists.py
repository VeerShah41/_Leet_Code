# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        arr = []
        for i in lists:
            while i:
                arr.append(i.val)
                i=i.next
        arr.sort()
        dum = ListNode(0)
        cur = dum
        for j in arr:
            cur.next=ListNode(j)
            cur = cur.next
        return dum.next