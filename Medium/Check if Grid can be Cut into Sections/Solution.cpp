class Solution {
    public:
        bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
            vector<pair<int,int>> x, y;
            int cuts,curr;
            for(auto pts:rectangles){
                x.push_back({pts[0],pts[2]});
                y.push_back({pts[1],pts[3]});
            }
    
            sort(x.begin(),x.end());
    
            cuts = 1;
            curr = x[0].second;
    
            for(int i=1;i<x.size();i++){
                if(x[i].first >= curr){
                    cuts++;
                    if(cuts > 2)
                        return true;
                }    
                curr = max(x[i].second,curr);
            }
    
            sort(y.begin(),y.end());
    
            curr = y[0].second;
            cuts = 1;
    
            for(int i=1;i<y.size();i++){
                if(y[i].first >= curr){
                    cuts++;
                    if(cuts>2)
                        return true;
                    }            
                curr = max(y[i].second,curr);          
            }
            return false;
        }
    };