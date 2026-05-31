class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        words = words[left:right+1]
        vovels=['a','e','i','o','u']
        c=0
        for i in words:
            if i[0] in vovels and i[-1] in vovels:
                c+=1
        return c