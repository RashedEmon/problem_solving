class MinStack:
    
    def __init__(self):
        self.arr = []
        self.min = (2 ** 31) - 1

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.arr.append((val, self.min))

    def pop(self) -> None:
        if self.arr[-1][0] == self.min:
            self.min = self.arr[-2][1] if len(self.arr) > 1 else self.min
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

