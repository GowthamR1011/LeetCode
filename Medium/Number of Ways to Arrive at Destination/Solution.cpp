class Solution {
    public:
        int countPaths(int n, vector<vector<int>>& roads) {
            map<long long,vector<pair<long long,long long>>> adj;
            long long u,v,t, mod = pow(10,9) + 7,cost;
            vector<long long> minm(n,1e12), path(n,0), seen(n,0);
            priority_queue<pair<long long,long long> , vector<pair<long long,long long>>, greater<pair<long long,long long>> > min_heap;
        
            for(auto road:roads){
                u = road[0];
                v = road[1];
                t = road[2];
    
                adj[u].push_back({v,t});
                adj[v].push_back({u,t});
            }
    
            
            path[0] = 1;
            minm[0] = 0;
    
            min_heap.push({0,0});
            
            while(!min_heap.empty()){
    
                cost = min_heap.top().first;
                u = min_heap.top().second;
                min_heap.pop();
    
                for(auto nei:adj[u]){
                    v = nei.first;
                    t = nei.second;             
                    if(minm[v] > cost + t ){
                        minm[v] = cost + t;
                        min_heap.push({minm[v],v});
                        path[v] = path[u];
                    }
                    else if(minm[v] == cost + t){
                        path[v] += path[u];
                        path[v] %= mod;
                    }
                }
            }
    
            return path.back();
    
    
    
        }
    };