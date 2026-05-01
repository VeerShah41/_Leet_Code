class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans = float("-inf")
        for i in accounts:
            ans = max(ans , sum(i))
        return ans
