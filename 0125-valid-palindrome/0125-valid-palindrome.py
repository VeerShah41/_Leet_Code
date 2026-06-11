class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = ''
        for i in s:
            if i.isalnum():
                ans+=lower(i)
        return ans==ans[::-1]
        