class Solution {
    public:
        int minimumIndex(vector<int>& nums) {
            
            map<int,int> counter;
            int n = nums.size(), max_count = 1, max_element = nums[0], low_count=0;
    
            for(auto num:nums){
                counter[num]++;
    
                if(counter[num] > max_count){
                    max_element = num;
                    max_count = counter[num];
                }
            }
    
            for(int i=0;i<n-1;i++){
                if(nums[i] == max_element){
                    max_count--;
                    low_count++;
                }
    
                if(low_count > (i+1)/2 && max_count > (n-1-i)/2)
                    return i;
            }
    
            return -1;
    
        }
    };