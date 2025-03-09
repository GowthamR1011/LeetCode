class Solution {
    public:
        int numberOfAlternatingGroups(vector<int>& colors, int k) {
            
            colors.insert(colors.end(),colors.begin(),colors.begin()+k-1);
    
            int length = 1,count = 0;
    
            for(int i=1;i<colors.size();i++){
                
                if(colors[i]!=colors[i-1]){
                    length++;
                }
    
                else{
                    length = 1;
                }
               
                if(length >= k)
                    count++;
            }
            return count;
            
        }
    };