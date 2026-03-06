class Solution(object):
    def searchRange(self, nums, target):
        lis = [-1, -1]
        
        for i in range(len(nums)):
            if nums[i] == target:
                lis[0] = i
                j = i + 1
                
                while j < len(nums) and nums[j] == target:
                    j += 1
                    
                lis[1] = j - 1
                break
                
        return lis