class Solution {
    public:
        vector<int> partitionLabels(string s) {
            unordered_map<char,int> last;
            vector<int> res;
            for(int i=0;i<s.length();i++)
                last[s[i]] = i;
            
    
            int r = 0,start = 0;
    
            for(int l=0;l<s.length();l++){
                r = max(r, last[s[l]]);
                if(r == l){
                    res.push_back( l - start  + 1);
                    start = r + 1;
                }
            }
    
            return res;
        }
    };