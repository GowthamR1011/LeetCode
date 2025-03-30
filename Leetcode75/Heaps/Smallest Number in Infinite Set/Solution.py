class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.added = set()

    def popSmallest(self) -> int:
        
        if self.added:
            res = min(self.added)
            self.added.remove(res)
            return res


        self.curr += 1
        return self.curr - 1

    def addBack(self, num: int) -> None:
        if self.curr > num:
            self.added.add(num) 


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)