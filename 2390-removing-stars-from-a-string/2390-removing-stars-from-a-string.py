class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=''
        for i in range(len(s)):
            j = s[i]
            if j!="*":
                l+=j
            else:
                if l:
                    l = l[:-1]
        return l


        