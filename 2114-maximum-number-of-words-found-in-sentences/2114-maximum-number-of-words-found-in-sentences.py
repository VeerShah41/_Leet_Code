class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans = 0
        for i in sentences:
            ans = max(ans , len(i.split(" ")))
        return ans
