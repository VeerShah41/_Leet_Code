class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        i = {"type": 0, "color": 1, "name": 2}
        c = 0
        for j in items:
            if j[i[ruleKey]]==ruleValue:
                c+=1
        return c