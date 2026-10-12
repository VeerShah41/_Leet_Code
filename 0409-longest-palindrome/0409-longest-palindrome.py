class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = {}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        ans = 0
        flag = True
        for i,j in f.items():
            if j%2==0:
                ans += j 
            else:
                if (j-1)%2==0 and j!=1:
                    if flag:
                        ans+=j
                        flag=False
                    else:
                        ans+=j-1
                if flag:
                    ans+=1
                    flag=False
        return ans
