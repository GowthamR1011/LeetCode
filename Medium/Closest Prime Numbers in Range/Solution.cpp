class Solution {
    public:
        vector<int> closestPrimes(int left, int right) {
            vector<bool> sieve(right+1,true);
            vector<int> primes;
            long long j,i;
            for(i=2;i<right+1;i++){
                if(sieve[i]){
                    if(i>=left)
                        primes.push_back(i);
    
                    for(j=i*i;j<=right;j+=i){
                        sieve[j] = false;
                    }
                }
            }
    
            if(primes.size() < 2)
                return {-1,-1};
            
            int a = primes[0], b = primes[1], min_val = b-a;
    
            for(int k=1;k<primes.size()-1;k++){
                if((primes[k+1] - primes[k]) < min_val){
                    b = primes[k+1];
                    a = primes[k];
                    min_val = b-a;
                }
    
            }
    
            return {a,b};
    
            
        }
    };