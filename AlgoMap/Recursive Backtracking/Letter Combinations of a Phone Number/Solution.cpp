class Solution {
    public:
        vector<string> keypad;
        vector<string> res;
        string sol;
        void backtrack(int index,string digits){
    
            if(index == digits.size()){
                res.push_back(sol);
                return;
            }
            
            for(auto ch:keypad[int(digits[index]) - 50]){
                sol += ch;
                backtrack(index+1,digits);
                sol.pop_back();
            }
    
    
                
        }
        vector<string> letterCombinations(string digits) {
    
            if(digits == "")
                return {};
    
            keypad.push_back("abc");
            keypad.push_back("def");
            keypad.push_back("ghi");
            keypad.push_back("jkl");
            keypad.push_back("mno");
            keypad.push_back("pqrs");
            keypad.push_back("tuv");
            keypad.push_back("wxyz");
            sol = "";
    
    
            backtrack(0,digits);
            return res;
    
    
        }
    };