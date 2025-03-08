class Solution {
    public:
        int numberOfSubstrings(string s) {
            vector<int> last_seen(3,-1);
    
            int total = 0;
    
            for(int i=0;i<s.size();i++){
                last_seen[s[i] - 'a'] = i;
                if(count(last_seen.begin(),last_seen.end(),-1) == 0){ 
                    total += (1 + *min_element(last_seen.begin(),last_seen.end()));
    
                }
            }
    
            return total;
        }
    };