class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ans = ""
        flag = False
        if ch not in word:
            return word
        for i in range(len(word)):
            if flag:
                ans += word[i]
            else:
                if word[i]==ch:
                    ans = word[i]+ans
                    flag= True
                else:
                    ans = word[i]+ans
        return ans