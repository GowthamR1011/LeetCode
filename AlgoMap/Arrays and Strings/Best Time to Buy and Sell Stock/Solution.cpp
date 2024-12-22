#include <cmath>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        float min_val = INFINITY;

        for(auto i:prices){
            if(i<min_val){
                min_val = i;
            }

            if(max_profit < (i-min_val)){
                max_profit = i - min_val;
            }
        }

        return max_profit; 


    }
};