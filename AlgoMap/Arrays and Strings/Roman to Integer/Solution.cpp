#include <map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> m = {{'I', 1}, {'V', 5},{'X', 10},{'L',50},{'C',100},{'D',500},{'M',1000}};

        int res = 0, i = s.length();
        
        while(i >= 0){
            if(i>0 and m[s[i]] > m[s[i-1]]){
                res += m[s[i]] - m[s[i-1]];
                i--;

            }
            else{
                res += m[s[i]];
            }
            i--;
        }
        
        return res;

    }


    
};