class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        for i in range(len(s)):
            if s[i]=="*":
                l.pop()
            else:
                l.append(s[i])
        return "".join(l)


        