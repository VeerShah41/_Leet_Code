class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = ''
        l1,l2 = len(word1),len(word2)
        m = min(l1,l2)

        for i in range(m):
            s += word1[i] + word2[i]

        s += word1[m:] + word2[m:]
        return s