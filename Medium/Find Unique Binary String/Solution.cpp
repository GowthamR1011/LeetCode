class Solution {
    public:
        int binaryToDecimal(string n) 
        { 
            int dec_value = 0, base = 1;
    
            while (n.length()>0) { 
                int last_digit =  n.back() - '0'; 
                n.pop_back();
    
                dec_value += last_digit * base; 
                base = base * 2; 
            } 
        
            return dec_value; 
        } 
      
        string findDifferentBinaryString(vector<string>& nums) {
            
    
            set<int> s;
            const int n = nums[0].length();
            for(auto st:nums)
                s.insert(binaryToDecimal(st));
    
            for(int i=0;i<pow(2,n);i++)
                if(s.count(i) == 0)
                    return bitset<64>(i).to_string().substr(64-n);
            return "01";
        }
    };