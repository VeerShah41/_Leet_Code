class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        
        for i in str(n):
            digit = int(i)
            if digit in d:
                d[digit] += 1
            else:
                d[digit] = 1
        ans = 0
        for i, j in d.items():
            ans += i * j
        
        return ans