class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        s = nums[0]
        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                s+=nums[i]
            
            else:
                break
        while s in nums:
            s+=1
        return s 