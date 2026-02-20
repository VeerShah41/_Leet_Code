from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        std = deque(students)
        san = deque(sandwiches)
        att = 0
        while std and att<len(students):
            if std[0]==san[0]:
                san.popleft()
                std.popleft()
                att = 0
            else:
                std.append(std.popleft())
                att += 1
        return len(std)


        