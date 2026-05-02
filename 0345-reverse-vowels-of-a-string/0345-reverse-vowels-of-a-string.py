class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        v = ['a','e','i','o','u','A','E','I','O','U']
        i = []
        s = list(s)
        for j in range(len(s)):
            if s[j] in v:
                l.append(s[j])
                i.append(j)
        l = l[::-1]

        for k in range(len(i)):
            s[(i[k])]=l[k]
        return ''.join(s)
