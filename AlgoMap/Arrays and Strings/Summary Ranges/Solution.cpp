using namespace std;
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {

        vector<string> result;

        if(nums.size()==0){
            return result;
        }

        int start = nums[0],end = nums[0];

        for(int i = 1; i<nums.size();i++){
            if(nums[i]==end+1){
                end++;
            }
            else{
                if(start == end)
                    result.push_back(to_string(start));
                else
                    result.push_back(to_string(start)+"->"+to_string(end));
                start = nums[i];
                end = nums[i];
            }
        }
        if(start == end)
            result.push_back(to_string(start));
        else
            result.push_back(to_string(start)+"->"+to_string(end));
        

        return result;
    }
};