class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(nums)
        if s%k==0:
            return 0
        else:

            s=s%k
            
            return s