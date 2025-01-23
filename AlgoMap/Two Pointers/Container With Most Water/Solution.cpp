class Solution {
public:
    int maxArea(vector<int>& height) {
        int maximum_area = 0, left = 0, right= height.size() -1,area;

        while(left<right){

            if(height[left] > height[right]){
                area = (right-left) * height[right];
                right--;
            }
            else{
                area = (right-left)*height[left];
                left++;
            }

            if(maximum_area < area)
                maximum_area = area;
            
        }

        return maximum_area;
    }
};