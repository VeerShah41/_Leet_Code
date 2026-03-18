class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return nums.index(max(nums))
        l = 0
        r = len(nums)-1
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums) - 1
        
        while l <= r:

            
            mid = (l+r)//2
            left = mid - 1
            right = mid + 1
            
            if nums[mid]>nums[left] and nums[mid]>nums[right]:
                return mid
            if nums[mid]<nums[left]:
                r=mid
            elif nums[mid]<nums[right]:
                l=mid
            
        return 