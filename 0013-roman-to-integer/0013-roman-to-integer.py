class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        su=0
        for i in range(len(s)):
            if i+1 < len(s) and val[s[i]]<val[s[i+1]]:
                su-=val[s[i]]
            else:
                su+=val[s[i]]
        return su