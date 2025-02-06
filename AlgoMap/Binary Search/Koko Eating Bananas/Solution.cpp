class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long total_bananas=0,min_k,max_k,k,time_taken, one = 1;
        
        for(auto p:piles)
            total_bananas += p;

        min_k=  max(total_bananas/h,one);

        max_k =  *max_element(piles.begin(),piles.end());

        while(min_k <= max_k){
            k  =  (min_k+max_k) / 2;
            time_taken = 0;

            for(auto p:piles)    
                time_taken += p/k + (p%k !=0);
            
            if(time_taken<=h)
                max_k = k-1;
            else
                min_k = k+1;
        
        }
        
        return max_k+1;

    }
};