class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l=0,r=0,max_w = 0;
        string sub;
        while(r<s.length()){
            sub = s.substr(l,r-l);
            while(sub.contains(s[r])){
                l++;
                sub = s.substr(l,r-l);
            }
            max_w = max(max_w,r-l+1);
            r++;
        }
        return max_w;
    }
};