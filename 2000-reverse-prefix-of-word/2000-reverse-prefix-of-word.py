class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        for i in range(len(word)):
            if word[i]==ch:
                word=word[i::-1]+word[i+1:]
                break
        return word