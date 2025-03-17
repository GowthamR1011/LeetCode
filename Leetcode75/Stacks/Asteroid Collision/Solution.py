class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        s = []

        for a in asteroids:

            if a > 0 or not s:
                s.append(a)
            else:
                while s and  s[-1] > 0 and s[-1] < abs(a):
                    s.pop()
                if s and s[-1] == abs(a):
                    s.pop()
                elif not s or s[-1] <0 :
                    s.append(a)

            
        return s


           
