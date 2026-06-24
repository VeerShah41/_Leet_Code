class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def help(st,pos):
            pos = pos%26
            return chr(ord(st)+pos)
        ans = s[0]
        for i in range(1,len(s)):
            if s[i].isdigit():
                ans += help(s[i-1],int(s[i]))
            else:
                ans += s[i]
        return ans            
