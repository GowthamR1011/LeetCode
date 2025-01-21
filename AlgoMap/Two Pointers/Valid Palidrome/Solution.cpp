class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0,end = s.length()-1;

        while(start<end){
            while(!iswalnum(s[start]) && start<end)
                start++;
            while(!iswalnum(s[end]) && start<end)
                end--;
            
            if(tolower(s[end]) != tolower(s[start]))
                return false;
            
            start++;
            end--;
        }
        return true;
    }
};