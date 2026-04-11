class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vov = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        left = 0
        right = 0
        n = (len(s)-1)//2
        for i in range(len(s)):
            if i<=n:
                if s[i] in vov:
                    left+=1
            else:
                if s[i] in vov:
                    right+=1
        return left==right