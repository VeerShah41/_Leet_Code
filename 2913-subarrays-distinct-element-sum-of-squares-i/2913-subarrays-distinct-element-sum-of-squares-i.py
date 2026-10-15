class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            seen = []
            d = 0
            for j in nums[i:]:
                if j not in seen:
                    seen.append(j)
                    d+=1
                ans += d*d
        return ans
