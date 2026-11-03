class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        x = nums[len(nums)//2]
        n = len(nums)
        ans = 0
        for i in nums:
            ans += abs(x-i)
        return ans