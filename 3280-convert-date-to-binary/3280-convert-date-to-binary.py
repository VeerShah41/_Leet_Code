class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        ans = ""
        date = date.split("-")
        for i in date:
            ans += str(bin(int(i))[2:])+"-"
        return ans[:-1]
        