class Solution {
    public:
        map<int,int> bob_path;


        bool getBobPath(int curr_pos,int t, vector<bool>& visited, map<int,vector<int>>& adj){
            
            visited[curr_pos] = true;
            bob_path[curr_pos] = t;
    
            if(curr_pos == 0)
                return true;
    
            
            for(auto next_pos:adj[curr_pos]){
                if(!visited[next_pos]){
                    if(getBobPath(next_pos,t+1,visited,adj))
                        return true;
                }
            }
    
            bob_path.erase(curr_pos);
            return false;
    
        }
        int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
            
            int n = amount.size(),max_amt = INT_MIN,amt,t,curr;

            map<int,vector<int>> adj;
    
            for(auto ed:edges){
                adj[ed[0]].push_back(ed[1]);
                adj[ed[1]].push_back(ed[0]);
            }
    


            vector<bool> visited(n,false);
    
            getBobPath(bob,0,visited,adj);
    
            fill(visited.begin(),visited.end(),false);
    
            queue<vector<int>> q;
    
            q.push({0,0,0});
    
            while(!q.empty()){
                curr = q.front()[0];
                t = q.front()[1];
                amt = q.front()[2];
    
                q.pop();
                visited[curr] = true;
                
                if(bob_path.find(curr) == bob_path.end() || bob_path[curr] > t )
                    amt += amount[curr];
                
                else if(bob_path[curr] == t)
                    amt += (amount[curr]/2);
                
                bool leaf = true;
    
                for(auto next_pos:adj[curr]){
                    if(!visited[next_pos]){
                        q.push({next_pos,t+1,amt});
                        leaf = false;
                    }
                }
                if(leaf)
                    max_amt = max(amt,max_amt);
            }
    
            return max_amt;
    
    
    
        }
    };