class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mc = 0
        st = ""

        for i in s:

            if i in st:
                idx = st.index(i)
                st = st[idx+1:]

            st += i
            mc = max(mc, len(st))

        return mc