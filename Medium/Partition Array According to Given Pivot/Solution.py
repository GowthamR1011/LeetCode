class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        more_than = []
        equal = 0

        for i in nums:
            if i < pivot:
                less_than.append(i)
            elif i > pivot:
                more_than.append(i)
            else:
                equal += 1
        
        return less_than + [pivot] * equal + more_than