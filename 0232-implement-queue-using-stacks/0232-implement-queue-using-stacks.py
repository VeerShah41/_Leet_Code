class MyQueue(object):

    def __init__(self):
        self.l=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.l.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.l[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.l)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()