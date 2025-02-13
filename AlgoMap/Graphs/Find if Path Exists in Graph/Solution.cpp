class Solution {
    public:
        bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
            
            if(source == destination)
                return true;
            vector<vector<int>> connections(n);
    
            for(auto edge:edges){
                connections[edge[0]].push_back(edge[1]);
                connections[edge[1]].push_back(edge[0]);
            }
    
            vector<int> seen(n,0);
            vector<int> stack;
            int node;
    
            seen[source] = 1;
            stack.push_back(source);
    
            while(stack.size() > 0){
                node = stack.back();
                stack.pop_back();
    
                for(auto nei:connections[node]){
                    if(nei == destination)
                        return true;
                    else if(!seen[nei]){
                        seen[nei] = 1;
                        stack.push_back(nei);
                    }       
                }         
            }
    
            return false;
    
    
        }
    };