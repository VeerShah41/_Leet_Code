class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1 :
            return 0
        
        for i in range(len(nums)):
            x = max(nums[:i+1]) - min(nums[i:])
            if x <= k:
                return i
        return -1