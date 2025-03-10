class Solution {
    public:
        bool allvowelspresent(map<char,long long> &vowel){
            for(auto it:vowel){
                if(it.second == 0)
                    return false;
            }
    
            return true;
        }
        long long countOfSubstrings(string word, int k) {
            map<char,long long> count = {{'a',0},{'e',0},{'i',0},{'o',0},{'u',0}};
            char ch, left_ch;
            long long left = 0,right = 0, con_count = 0, res_count = 0, res = 0;
    
            for(;right<word.size();right++){
                ch = word[right];
                
                if(count.count(ch) == 0){
                    con_count++;
                    res_count = 0;
                }
                else{
                    count[ch]++;
                }
    
                while(con_count > k){
                    left_ch = word[left];
    
                    if(count.count(left_ch) == 0){
                        con_count--;
                    }
                    else{
                        count[left_ch]--;
                    }
                    left++;
                }
    
    
                while(con_count == k && allvowelspresent(count)){
                    res_count++;
                    left_ch = word[left];
    
                    if(count.count(left_ch) == 0){
                        con_count--;
                    }
                    else{
                        count[left_ch]--;
                    }
                    left++;
                }
    
                res += res_count;
            }
    
            return res;
        }
    };