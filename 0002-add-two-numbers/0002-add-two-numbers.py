# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def help(carry , l1 ,l2):
            if not l1 and not l2 and carry==0:
                return 
            if l1 and l1.val:
                val1=l1.val
            else:
                val1=0
            if l2 and l2.val:
                val2=l2.val
            else:
                val2=0
            total = val1 + val2 + carry
            carry = total//10
            node = ListNode(total%10)
            if l1 and l1.next:
                next1=l1.next
            else:
                next1=None
            if l2 and l2.next:
                next2=l2.next
            else:
                next2=None

            node.next=help(carry,next1,next2)
            return node
        return help(0,l1,l2)

