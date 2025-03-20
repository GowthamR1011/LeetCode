class UnionFind{
    public:
        vector<int> parent;
        vector<long long> size;
    
        UnionFind(int n){
            for(int i=0;i<n;i++){
                parent.push_back(i);
                size.push_back(1);
            }
        }
        int find(int x){
            if(parent[x]!=x)
                return find(parent[x]);
            
            return x;
        }
    
        void unio(int x,int y){
    
            int p1 = find(x);
            int p2 = find(y);
    
            if(p1 != p2){
                if(size[p1] < size[p2]){
                    parent[p1] = p2;
                    size[p2] += size[p1];
                }
                else{
                    parent[p2] = p1;
                    size[p1] += size[p2];
                }
            }
        }
    
    
    };
    
    class Solution {
    public:
        vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
            
            UnionFind uf(n);
            vector<int> res;
            map<int,int> cost;
            int p1,p2;
    
            for(auto e:edges){
                uf.unio(e[0],e[1]);
            }
    
            for(auto e:edges){
                int p1 = uf.find(e[0]);
    
                if(cost.find(p1) == cost.end())
                    cost[p1] = e[2];
                else
                    cost[p1] &= e[2];
    
            }
    
    
            for(auto q:query){
                p1 = uf.find(q[0]);
                p2 = uf.find(q[1]);
    
                if(p1 == p2){
                    res.push_back(cost[p1]);
    
                }
                else
                    res.push_back(-1);
            }
    
            return res;
    
        }
    };