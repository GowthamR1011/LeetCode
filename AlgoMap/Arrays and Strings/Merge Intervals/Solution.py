class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda interval:interval[0])
        results = []
        
        for [start,end] in intervals:
            if results == [] or results[-1][1] < start:
                results.append([start,end])
            elif end > results[-1][1]:
                results[-1][1] = end
            
        
        return results


            