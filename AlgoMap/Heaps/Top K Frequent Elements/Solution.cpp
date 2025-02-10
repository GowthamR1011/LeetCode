class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            map<int,int> counter;
            vector<int> result;
            priority_queue<pair<int, int> >  priorityQueue; 
    
            for(auto key:nums) counter[key]++;
            
            for(auto p:counter) priorityQueue.push({p.second,p.first});
    
            for(int i=1;i<=k;i++){
                result.push_back(priorityQueue.top().second);
                priorityQueue.pop();
            }
    
            return result;
        }
    };