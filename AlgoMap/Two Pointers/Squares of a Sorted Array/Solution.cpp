class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int i;
        for(i=0;i<nums.size();i++){
            if(nums[i]>=0)
                break;
        }

        int left = i-1,right = i;
        vector<int> result;

        while(left >=0 && right< nums.size()){
            if(abs(nums[left]) < abs(nums[right]) ){
                result.push_back(nums[left]*nums[left]);
                left--;
            }
            else{
                result.push_back(nums[right]*nums[right]);
                right++;
            }
        }

        while(left>=0){
            result.push_back(nums[left]*nums[left]);
            left--;
        }
        while(right<nums.size()){
            result.push_back(nums[right]*nums[right]);
            right++;
        }

        return result;

    }
};