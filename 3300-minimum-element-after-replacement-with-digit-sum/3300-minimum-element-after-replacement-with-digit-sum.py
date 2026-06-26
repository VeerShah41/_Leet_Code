class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in nums:
            temp = 0
            while i>0:
                temp+=(i%10)
                i=i//10
            res.append(temp)
        return min(res)