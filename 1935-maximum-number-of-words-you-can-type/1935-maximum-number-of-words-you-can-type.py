class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text=text.split(" ")
        ans = len(text)
       
        for i in text:
            for j in brokenLetters:
                if j in i:
                    ans-=1
                    break
        return ans
            