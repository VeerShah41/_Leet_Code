class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        x = nums[len(nums)//2]
        return sum(abs(i - x) for i in nums)