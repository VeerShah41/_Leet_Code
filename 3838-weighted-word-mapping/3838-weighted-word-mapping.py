class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """

        ans = ""
        
        for word in words:
            su = 0
            for ch in word:
                su += weights[ord(ch) - ord('a')]

            mod = su % 26
            

            ans += chr(ord('z')-mod)
        return ans
