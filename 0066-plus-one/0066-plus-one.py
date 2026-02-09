class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        d=int("".join(map(str, digits)))
        d+=1
        return list(map(int, str(d)))
