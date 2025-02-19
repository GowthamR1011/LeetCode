class Solution {
    public:
        int climbStairs(int n) {
    
            if(n==1)
                return 1;
            
            int curr=2,prev = 1, temp;
    
            for(int i=1;i<n-1;i++){
                temp = curr;
                curr += prev;
                prev = temp;
            }
            
            return curr;
            
        }
    };