class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        
        def help(n):
            a = 0
            while n>0:
                if n%10==digit:
                    a+=1
                n = n//10
            return a
        ans = 0
        for i in nums:
            ans+=help(i)
        return ans 

        

            