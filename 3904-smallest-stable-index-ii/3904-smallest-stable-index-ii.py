class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        suffix = [0]*n
        suffix[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i]=min(nums[i],suffix[i+1])
        ma = 0
        for j in range(n):
            ma = max(ma,nums[j])
            if ma - suffix[j] <= k:
                return j
        return -1