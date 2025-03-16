class Solution {
    public:
        bool isPossible(vector<int>& ranks, long long cars,long long t){
            long long count =0;
            
            for(auto r:ranks){
                count += sqrt(t/r);
                if(count >= cars)
                    return true;
            }
    
            return false;
        }
    
        long long repairCars(vector<int>& ranks, int cars) {
            
            long long c = cars;
            long long l = 1, r = *min_element(ranks.begin(),ranks.end()) *  c *  c, mid,res = r;
    
            while(l <= r){
    
                mid = (l+r) /2;
    
                if(isPossible(ranks,c,mid)){
                    r = mid - 1;
                    res = min(res,mid);
                }
                else{
                    l = mid + 1;
                }
            }
    
            return res;
    
    
        }
    };