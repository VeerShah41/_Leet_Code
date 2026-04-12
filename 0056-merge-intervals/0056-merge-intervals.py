class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = merged[-1]
            
            if curr[0] <= last[1]:   # overlap
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)
        
        return merged
