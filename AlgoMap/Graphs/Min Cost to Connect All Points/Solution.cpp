class Solution {
    public:
        int minCostConnectPoints(vector<vector<int>>& points) {
            int edges = -1, cost = 0,d,i,n = points.size();
            
            priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > distHeap;
    
            set<int> seen;
            distHeap.push({0,0});
    
            while(edges < (n-1)){
                d = distHeap.top().first;
                i = distHeap.top().second;
                distHeap.pop();
                if(seen.count(i) == 0){
                    seen.insert(i);
                    cost += d;
                    edges++;
    
                    for(int j=0;j<n;j++){
                        if(seen.count(j) == 0){
                            distHeap.push({abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1]),j });
    
                        }
                    }
                }
    
            }
    
            return cost;
    
        }
    };