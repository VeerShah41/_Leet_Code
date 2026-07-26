class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = 0
        p = 0
        while i < len(nums) - 1:
            if nums[i]==nums[i+1]:
                p+=1
                i+=2
            else:
                i+=1
        return [p,len(nums) - 2*p]


