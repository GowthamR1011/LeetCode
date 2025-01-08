#include<unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> umap_t,umap_s;

        for(char ch:s){
            if(umap_s.find(ch) != umap_s.end()){
                umap_s[ch]++;
            }
            else{
                umap_s[ch] = 1;
            }
        }

        for(char ch:t){
            if(umap_t.find(ch) != umap_t.end()){
                umap_t[ch]++;
            }
            else{
                umap_t[ch] = 1;
            }
        }

        return umap_t == umap_s;
    }
};