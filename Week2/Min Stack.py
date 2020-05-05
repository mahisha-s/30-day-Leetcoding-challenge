#Python3
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr=[]
        

    def push(self, x: int) -> None:
        self.arr+=[x]
        return None
        

    def pop(self) -> None:
        self.arr.pop()
        return None
        

    def top(self) -> int:
        return self.arr[len(self.arr)-1]
        

    def getMin(self) -> int:
        return min(self.arr)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
