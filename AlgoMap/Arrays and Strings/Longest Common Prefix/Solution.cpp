class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        int i = 0;
        char ch;
        while(true){
            if(i==strs[0].length()){
                return strs[0];
            }
            ch = strs[0][i];

            for(auto s:strs){
                if((i==s.length()) || (s[i] != ch)){
                    return s.substr(0,i);
                }
            }

            i++;
        }
    }
};