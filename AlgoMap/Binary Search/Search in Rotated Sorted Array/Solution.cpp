class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low=0, high = nums.size() - 1,mid, result = -1; 

        while(nums[low]>nums[high]){
            mid = (low+high) / 2;

             if(nums[mid] > nums[mid+1]){
                result = mid + 1;;
                break;
             }
            
            if(nums[mid-1] > nums[mid]){
                result = mid;
                break;
            }
            
            if(nums[mid] > nums[low])
                low = mid + 1;
            else
                high = mid - 1;
        }

        if(result == -1){
            low = 0;
            high = nums.size() -1;
         }
        else if(nums[nums.size()- 1]>=target){
            low = result;
            high = nums.size() - 1;
        }
        else{
            low = 0;
            high = result - 1;
        }

        while(low<=high){
            mid = (low+high) /2;

            if(nums[mid] == target)
                return mid;
            
            if(nums[mid] > target)
                high = mid - 1;
            else
                low = mid+ 1;
        }
        return -1;

    }
};