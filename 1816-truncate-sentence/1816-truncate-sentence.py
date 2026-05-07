class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = s.split(" ")
        if k<len(l):
            l = l[:k]
        else:
            return " ".join(l)
        return " ".join(l)