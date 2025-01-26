class Solution {
public:
    int calPoints(vector<string>& operations) {

        int x;
        vector<int> result;

        for(auto ch:operations){
            char i = ch[0];
            if(i == 'D'){
                x = result.back() * 2;
                result.push_back(x);
            }
            else if(i == 'C')
                result.pop_back();
            else if(i == '+')
                result.push_back(result[result.size()-2]+result.back());
            else{
                x = stoi(ch);
                result.push_back(x);
            }

            

        }
        int sum = 0;
        for(auto j:result)
            sum += j;
        return sum;



    }
};