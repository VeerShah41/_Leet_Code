class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf")
        for i in nums:
            temp = 0
            while i>0:
                temp+=(i%10)
                i=i//10
            if temp<res:
                res = temp
            
        return res