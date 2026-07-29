class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n , p = 0 , 0
        for i in nums:
            if i>0:
                p+=1
            elif i<0:
                n+=1
        return max(n,p)