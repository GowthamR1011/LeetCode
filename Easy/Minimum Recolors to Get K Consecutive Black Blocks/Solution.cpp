class Solution {
    public:
        int minimumRecolors(string blocks, int k) {
            
            int count =0; 
    
            for(int i=0;i<k;i++){
                if(blocks[i] == 'W')
                    count++;
            }
    
            int res = count;
    
            for(int j=k;j<blocks.size();j++){
                if(blocks[j]=='W')
                    count++;
                
                if(blocks[j-k]=='W')
                    count--;
                
                res = min(res,count);
            }
    
            return res;
        }
    };