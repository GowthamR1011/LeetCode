class UnionFind{
    public:
        vector<int> parent;
    
        UnionFind(int n){
            for(int i =0;i<n;i++){
                parent.push_back(i);
            }
        }
    
        int find(int x){
    
            if( x != parent[x])
                return find(parent[x]);
            
            return x;
        }
    
        void un(int x, int y){    
            parent[find(y)] = find(x);
        }
    };
    
    class Solution {
    public:
        int countCompleteComponents(int n, vector<vector<int>>& edges) {
            
            UnionFind uf(n);
            int res=0;
            map<int,int> nodes, ed;
    
            for(auto edge:edges){
                uf.un(edge[0],edge[1]);
            }
    
            for(int i =0; i < n;i++){
                nodes[uf.find(i)]++;
            }
    
            for(auto edge:edges){
                ed[uf.find(edge[0])]++;
            }
    
            for(int i = 0; i<n;i++){
                if(uf.parent[i] == i && (nodes[i] * (nodes[i] - 1) /2 ) == ed[i])
                    res++;
            }
    
            return res;
    
        }
    };