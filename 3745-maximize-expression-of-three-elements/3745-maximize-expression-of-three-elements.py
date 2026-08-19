class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f ,s ,m =float("-inf"),float("-inf"),float("inf")
        for i in nums:
            if i > f:
                s = f
                f = i
            elif i > s:
                s = i
            if i < m:
                m=i
        return f+s-m