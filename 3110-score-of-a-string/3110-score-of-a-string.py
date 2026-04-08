class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i=0
        j=1
        while j<len(s):
            ans+=abs(ord(s[i])-ord(s[j]))
            i+=1
            j+=1
        return ans