import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if self.pos.__contains__(val):
            return False

        self.pos[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if not self.pos.__contains__(val):
            return False

        i = self.pos.get(val)
        self.values[i], self.values[-1] = self.values[-1], self.values[i]  # Swap i-th and last index
        self.pos[self.values[i]] = i
        self.values.pop(-1)
        self.pos.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(list(self.values))



# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()