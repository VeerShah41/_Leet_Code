class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for i,j in enumerate(s):
            if j.isdigit():
                ans.pop()
            else:
                ans.append(j)
        return "".join(ans)