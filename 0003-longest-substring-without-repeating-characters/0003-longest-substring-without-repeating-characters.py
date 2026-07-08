class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        st = ""
        for i in s:
            if i in st:
                idx = st.index(i)
                st = st[idx+1:]
            st+=i
            ans = max(ans,len(st))
        return ans
