class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> stack, answer(temperatures.size(),0);
        int ele;
        for(int i=0;i<temperatures.size();i++){
            while(stack.size()>0 && temperatures[stack.back()] < temperatures[i]){
                ele = stack.back();
                stack.pop_back();

                answer[ele] = i - ele;
            }
            stack.push_back(i);
        }

        return answer;
    }
};