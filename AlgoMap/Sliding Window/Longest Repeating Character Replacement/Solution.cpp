
class Solution {
    public:
        int characterReplacement(string s, int k) {
            unordered_map<char,int> char_count;
            int l=0,r=0,max_w = 0, max_char_count = 0;
    
            while(r<s.length()){
                
                char_count[s[r]]++;
                max_char_count = max(max_char_count,char_count[s[r]]);
    
                if((r-l+1 - max_char_count) > k){
                    char_count[s[l]]--;
                    l++;
                }
    
                r++;
                max_w = max(max_w,r-l);
            }
            return max_w;
    
        }
    };