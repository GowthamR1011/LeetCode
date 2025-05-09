class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        dist_speed = [(target - position[i],speed[i]) for i in range(len(speed))]

        dist_speed.sort()

        stack = [dist_speed[0][0] / dist_speed[0][1]]
        
        for i in range(1,len(speed)):
            time = dist_speed[i][0] / dist_speed[i][1]
            if  time > stack[-1] :
                stack.append(time)
        
        return len(stack)


            
