class Solution {
    public:
        int networkDelayTime(vector<vector<int>>& times, int n, int k) {
            int minTime = 0,t,i;
                
            priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > timeHeap;
        
            set<int> seen;
            vector<vector<int>> adj(n, vector<int>(n, -1));
    
            for(int j=0;j<times.size();j++)
                adj[times[j][0]-1][times[j][1]-1] = times[j][2]; 
    
            timeHeap.push({0,k-1});
        
            while(!timeHeap.empty()){
    
                t = timeHeap.top().first;
                i = timeHeap.top().second;
                timeHeap.pop();
    
                if(seen.count(i) == 0){
                    seen.insert(i);
                    minTime= max(minTime,t);
        
                    for(int j=0;j<n;j++){
                        if(seen.count(j) == 0 and adj[i][j] != -1){
                            timeHeap.push({minTime+adj[i][j],j});
                            }
                    }
                }
        
            }
        
            if(seen.size() == n)
                return minTime;
                
            return -1;
        }
    };