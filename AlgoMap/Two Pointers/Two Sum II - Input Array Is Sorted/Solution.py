class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        s = set(numbers)

        for i in range(len(numbers)):
            if(target-numbers[i] in s):
                if(target-numbers[i] >= numbers[i]):
                    target_index = self.bsearch(numbers,target-numbers[i],i+1,len(numbers)-1)
                else:
                    target_index = self.bsearch(numbers,target-numbers[i],0,i-1)
                
                return [i+1,target_index+1]
                
    def bsearch(self,numbers:List[int],second_target:int,left:int,right:int) -> int:

       

        while left<=right:
            mid = (left+right)//2
            
            if(numbers[mid] == second_target):
                return mid
            elif(numbers[mid] > second_target):
                right = mid - 1
            else:
                left = mid + 1
            
        return -1