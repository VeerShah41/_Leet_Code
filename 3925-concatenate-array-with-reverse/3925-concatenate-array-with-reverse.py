class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        z = len(nums)
        for i in range(z-1,-1,-1):
            nums.append(nums[i])
        return nums
