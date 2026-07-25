class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi = min(nums)
        ma = max(nums)

        c = 0
        for i in nums:
            if mi < i < ma:
                c += 1
        return c