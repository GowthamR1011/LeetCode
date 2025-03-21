class Solution {
    public:
        
        
        bool dfs(string product, set<string>& supplies, map<string,vector<string>> &rec_map,set<string>& seen ){
    
            if(supplies.find(product) != supplies.end())
                return true;
            
            if(rec_map.find(product) == rec_map.end() || seen.find(product) != seen.end())
                return false;
            
            seen.insert(product);
    
    
            for(auto ing:rec_map[product]){
                if(!dfs(ing,supplies,rec_map,seen))
                    return false;
            }
            
            supplies.insert(product);
            return true;
        }
        vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
            
            map<string, vector<string>> rec_map;
            set<string> sup,seen;
    
            for(auto s:supplies)
                sup.insert(s);
    
            for(int i=0;i<recipes.size();i++){
                rec_map[recipes[i]] = ingredients[i];
            }
    
            vector<string> res;
    
            for(auto recipe:recipes){
                if(dfs(recipe,sup,rec_map,seen))
                    res.push_back(recipe);
    
            }
    
            return res;
        }
    };