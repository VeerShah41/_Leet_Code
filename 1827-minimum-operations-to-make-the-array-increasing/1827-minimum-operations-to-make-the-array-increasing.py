class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = nums[0]
        ans = 0
        for i in range(1,len(nums)):
            if nums[i]<=prev:
                ans += (prev+1-nums[i])
                prev += 1 
            else:
                prev = nums[i]
        return ans