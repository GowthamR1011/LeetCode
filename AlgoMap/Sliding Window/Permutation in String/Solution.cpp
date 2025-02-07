class Solution {
    public:
        bool checkInclusion(string s1, string s2) {
            string s = s1;
            int l=0,r=0,pos;
    
            while(r<s2.length()){
                pos = s.find(s2[r]);
                if( pos != string::npos){
                    s.replace(pos,1,"");
                    if(s.length() == 0)
                        return true;
                }
                else if(s1.find(s2[r]) != string::npos){
                    while(s2[r] != s2[l]){
                        s = s + s2[l];
                        l++;
                    }
                    l++;
                }
                else{
                    l = r+1;
                    s= s1;
                }
                r++;
            }
    
            return false;
    
    
        }
    };