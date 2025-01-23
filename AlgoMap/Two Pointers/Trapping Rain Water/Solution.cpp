class Solution {
public:
    int trap(vector<int>& height) {
        int max_l = 0 ,max_r = 0;
        int n = height.size();
        int left = 0, right = n-1, trapped_water = 0;

        while(left<right){
            if(height[left]<height[right]){
                if(height[left]<max_l)
                    trapped_water += max_l - height[left];
                else
                    max_l = height[left];
                left++;
            }
            else{
                if(height[right] < max_r)
                    trapped_water += max_r - height[right];
                else
                    max_r = height[right];
                right--;
            }
        }
        return trapped_water;
    }
};