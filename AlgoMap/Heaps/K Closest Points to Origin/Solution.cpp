class Solution {
    public:
        vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
            priority_queue<pair<float,int>,vector<pair<float,int>>, greater<pair<float,int>> > distance;
            float d;
            vector<vector<int>> result;
    
            for(int i=0;i<points.size();i++){
                d =  sqrt(pow(points[i][0],2) + pow(points[i][1],2));
                distance.push({d,i});
            }
    
            for(int j=0;j<k;j++){
                result.push_back(points[distance.top().second]);
                distance.pop();
            }
            
            return result;
        }
    };