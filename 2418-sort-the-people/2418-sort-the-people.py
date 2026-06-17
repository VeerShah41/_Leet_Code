class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        ans = list(zip(heights,names))
        ans.sort(reverse=True)
        return [res for a,res in ans]