class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)

        ans = 0
        for num in nums:
            if mn < num < mx:
                ans += 1
        return ans