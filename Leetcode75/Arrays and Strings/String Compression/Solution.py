class Solution:
    def compress(self, chars: List[str]) -> int:
        
        count = 1
        index_to_write = 0
        for i in range(1,len(chars)):
            if chars[i-1] != chars[i]:
                chars[index_to_write] = chars[i-1]
                index_to_write += 1
                if count > 1:
                    for ch in str(count):
                        chars[index_to_write] = ch
                        index_to_write += 1
                    
                count = 1
            else:
                count += 1



        chars[index_to_write] = chars[-1]
        index_to_write += 1

        if count > 1:
            for ch in str(count):
                chars[index_to_write] = ch
                index_to_write += 1


        return index_to_write