class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = "1"
        def helper(s):
            ans = ""
            c = 1
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    c+=1
                else:
                    ans+=str(c) + s[i-1]
                    c=1
            ans += str(c) + s[-1]    
            return ans
        for i in range(1,n):
            start = helper(start)
        return start

                
                