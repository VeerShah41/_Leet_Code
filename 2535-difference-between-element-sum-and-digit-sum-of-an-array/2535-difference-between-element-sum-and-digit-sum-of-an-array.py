class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele = 0
        digit = 0
        for i in nums:
            ele+=i
            while i>0:
                digit+=(i%10)
                i=i//10
        return ele-digit
