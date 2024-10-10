class MinStack:

    def __init__(self):
        self.qstack = []
        self.minv = []

    def push(self, val: int) -> None:
        self.qstack.append(val)
        min_value = min(val, self.minv[-1] if self.minv else val)
        self.minv.append(min_value)

    def pop(self) -> None:
        self.qstack.pop()
        self.minv.pop()

    def top(self) -> int:
        return self.qstack[-1]

    def getMin(self) -> int:
        return self.minv[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()