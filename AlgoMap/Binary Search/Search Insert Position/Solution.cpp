class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1, mid;

        while(low<=high){
            
            mid = (low+high) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] > target)
                high = mid - 1;
            else
                low = mid + 1;

        }
        if(nums[mid] > target)
            return mid;
        
        return mid+1;
    }
};