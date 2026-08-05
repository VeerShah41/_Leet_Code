class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ma = max(nums)
        mi = min(nums)
        ans = []
        for i in range(mi,ma+1):
            if i not in nums:
                ans.append(i)

        return ans