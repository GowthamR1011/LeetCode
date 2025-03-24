class Solution {
    public:
        int countDays(int days, vector<vector<int>>& meetings) {
            sort(meetings.begin(),meetings.end());
            int curr = 1, res = 0;
            for(auto meet:meetings){
    
                if(meet[0] > curr){
                    res += meet[0] - curr;
                }
    
                curr = max(meet[1] +1,curr);
            }
    
            res += days - curr + 1;
            return res;
        }
    };