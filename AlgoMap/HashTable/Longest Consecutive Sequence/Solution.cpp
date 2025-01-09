class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest_count = 0,count,j;
        set<int> s(nums.begin(),nums.end());
        

        for(int i:s){
            if(s.contains(i-1))
                continue;
            else{
                j = i+1;
                count = 1;
                while(true){
                    if(s.contains(j)){
                        j++;
                        count++;
                    }
                    else
                        break;
                }
                if(count>longest_count)
                    longest_count = count;
            }
        }

        return longest_count;
    }
};