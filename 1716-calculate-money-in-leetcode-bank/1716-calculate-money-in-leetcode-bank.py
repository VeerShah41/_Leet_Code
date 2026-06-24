class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        ans = 0
        while n>0:
            
            for i in range(min(7,n)):
                ans += (a+i)
            a+=1
            n-=7
        return ans


