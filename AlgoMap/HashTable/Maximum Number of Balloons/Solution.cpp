#include<unordered_map>
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char,int> counter;
        int result = 0;
        for(char ch:text){
            if(counter.find(ch) == counter.end()){
                counter[ch] = 1;
            }
            else{
                counter[ch]++;
            }
        }
        
        while(true){
            if(counter['b']>=1 && counter['a']>=1 && counter['l']>=2 && counter['o']>=2 && counter['n']>=1){
                result++;
                counter['b']--;
                counter['a']--;
                counter['l'] -=2;
                counter['o'] -= 2;
                counter['n']--;
            }
            else
                break;
        }
        return result;
    }
};