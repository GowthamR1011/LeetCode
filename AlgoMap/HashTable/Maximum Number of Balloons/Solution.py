from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)

        result = 0

        while True:

            if counter['b'] > 0 and counter['a'] > 0 and counter['l'] > 1 and counter['o'] > 1 and counter['n'] > 0:
                result += 1
                counter['b'] -= 1
                counter['a'] -= 1
                counter['l'] -= 2
                counter['o'] -= 2
                counter['n'] -= 1
            else:
                break
        
        return result