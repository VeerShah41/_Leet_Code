from collections import deque
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        queue = deque(nums)
        k = k % len(nums)
        for i in range(k):
            queue.appendleft(queue.pop())

        for i in range(len(queue)):
            nums[i]=queue[i]     