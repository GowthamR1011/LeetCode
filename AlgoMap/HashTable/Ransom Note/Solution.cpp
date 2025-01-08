class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        set<char> s(ransomNote.begin(),ransomNote.end());

        for(char ch:s){
            if(count(ransomNote.begin(),ransomNote.end(),ch) > count(magazine.begin(),magazine.end(),ch))
                return false;
        
        }
        return true;
    }
};