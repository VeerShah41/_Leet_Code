class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def help(n):
            n = len(str(n))
            if n%2==0:
                return 1
            return 0
        ans = 0
        for i in nums:
            ans += help(i)
        return ans
