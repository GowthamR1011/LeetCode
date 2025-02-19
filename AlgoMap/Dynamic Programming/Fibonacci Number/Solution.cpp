class Solution {
    public:
        int fib(int n) {
            int prev=0,curr=1,temp;
    
            if(n==0)
                return 0;
            
            if(n == 1)
                return 1;
            
            for(int i=1;i<=n-1;i++)
            {
                temp = curr;
                curr += prev;
    
                prev = temp;
            }
    
            return curr;
        }
    };