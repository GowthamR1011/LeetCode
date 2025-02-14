class Solution {
    public:
        vector<int> result;
    
        bool dfs(int node, vector<int>& visited, vector<vector<int>>& connections){
                if(visited[node] == 2)
                    return true;
                if(visited[node] == 1)
                    return false;
        
                visited[node] = 1;
                for(auto j:connections[node]){
                    if(!dfs(j,visited,connections))
                        return false;
                }
                result.push_back(node);
                visited[node] = 2;
                return true;
            }
        
        vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
            vector<int> visited(numCourses,0);
            vector<vector<int>> connections(numCourses);
        
                for(auto& p:prerequisites){
                    connections[p[0]].push_back(p[1]);
                }
                
                for(int i=0;i<numCourses;i++){
                    if(!dfs(i,visited,connections))
                        return {};
                }
        
                return result;
        }
    };