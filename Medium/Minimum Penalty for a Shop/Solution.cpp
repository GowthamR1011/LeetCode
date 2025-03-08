class Solution {
    public:
        int bestClosingTime(string customers) {
            int n = customers.size(), max_j = n, pen, min_pen = 0;
    
            for(int i = 0;i<n;i++){
                if(customers[i] == 'N')
                    min_pen++;
            }
    
            pen = min_pen;
    
            for(int j = n-1;j>=0;j--){
                if(customers[j] == 'N')
                    pen--;
                else
                    pen++;
                
                if(pen<=min_pen){
                    min_pen = pen;
                    max_j = j;
                }
            }
    
            return max_j;
        }
    };