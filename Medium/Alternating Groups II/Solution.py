class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        n = len(colors)

        left = 0
        right = 1
        seen = set()
        res = 0
        while True:
            if (left,right) in seen:
                break

            seen.add((left,right))

            if colors[right] != colors[right-1]:
                if (right > left and right - left == k-1) or (right < left and n-left + right  == k-1):
                    res += 1
                    left += 1
                
                right += 1
            else:
                left = right 
                right += 1

            right %= n
            left %= n
        
        return res