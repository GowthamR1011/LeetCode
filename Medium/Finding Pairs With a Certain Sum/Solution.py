class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums2 = nums2
        self.c1  = Counter(nums1) 
        self.c2 = Counter(nums2)


    def add(self, index: int, val: int) -> None:
        self.c2[self.nums2[index]] -= 1  
        self.nums2[index] += val

        self.c2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:

        res = 0
        for val in self.c1:
            res += self.c2[tot - val] * self.c1[val]
        
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)