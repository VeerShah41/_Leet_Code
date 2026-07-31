class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = 0
        s = 0
        for i in gain:
            s+=i
            ans = max(ans,s)
        return ans