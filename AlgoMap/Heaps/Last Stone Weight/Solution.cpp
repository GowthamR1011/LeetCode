class Solution {
    public:
        int lastStoneWeight(vector<int>& stones) {
            
            // for(auto i;i<stones.size();i++)
            //     stones[i] = -1 * stones[i];
            int x,y;
            make_heap(stones.begin(),stones.end());
    
            while(stones.size()>1){
    
                y = stones[0];
                pop_heap(stones.begin(),stones.end());
                stones.pop_back();
    
                x = stones[0];
                pop_heap(stones.begin(),stones.end());
                stones.pop_back();
                
                if(x!=y){
                    stones.push_back(y-x);
                    push_heap(stones.begin(),stones.end());
                }
        
            }
    
            if(stones.size() == 1)
                return stones[0];
            return 0;
        }
    };