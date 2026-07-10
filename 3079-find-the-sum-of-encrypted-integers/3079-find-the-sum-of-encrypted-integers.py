class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def encrypt(n):
            ma = 0
            d = 0
            while n>0:
                
                ma = max(ma,n%10)
                n=n//10
                d+=1
            p = 1
            ans = 0 
            while d>0:
                ans += (ma*p)
                p*=10
                d-=1
            return ans

        ans = 0
        for i in nums:
            ans+=encrypt(i)
        return ans
