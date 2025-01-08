class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        
        int result = 0;
        for(auto ch:jewels)
            result += count(stones.begin(),stones.end(),ch);
        return result;
    }
};