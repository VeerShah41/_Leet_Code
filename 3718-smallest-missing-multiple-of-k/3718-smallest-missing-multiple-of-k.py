class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mul = 1

        n = k
        while n in nums:
        
            n = k*mul
            mul+=1
        return n
        