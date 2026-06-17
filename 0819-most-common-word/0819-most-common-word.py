class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.lower().split()

        d = {}

        for word in words:
            if word not in banned:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1

        ans = ""
        ma = 0

        for word, cnt in d.items():
            if cnt > ma:
                ma = cnt
                ans = word

        return ans