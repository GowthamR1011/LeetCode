using namespace std;
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
        string res = "";

        int l= 0, r = 0;

        while (l < word1.length() && r < word2.length()){
            res = res + word1[l] + word2[l];

            l += 1;
            r += 1;
        }

        while(l < word1.length()){
            res = res + word1[l];

            l += 1;
        }

        while(r < word2.length()){
            res = res + word2[r];

            r += 1;
        }

        return res;
    }
};