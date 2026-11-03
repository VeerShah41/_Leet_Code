class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)
        # ans = 0
        # for i in nums:
        #     ans += n-i
        # return ans
        s = sum(nums)
        l = len(nums)
        return (l*n)-s