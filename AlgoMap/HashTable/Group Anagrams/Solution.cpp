#include<unordered_map>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> dict;
        vector<vector<string>> result;
        string key;

        for(string st:strs){
            key= st;
            sort(key.begin(),key.end());
            dict[key].push_back(st);
        }


        for(auto kv:dict)
            result.push_back(kv.second);
        
        return result;
    }
};