class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing = True
        decreasing = True 
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                increasing = False
            if nums[i-1] < nums[i]:
                decreasing =False
        return increasing or decreasing