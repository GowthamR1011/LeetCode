/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    public:
        ListNode* mergeKLists(vector<ListNode*>& lists) {
            ListNode *start = new ListNode(-1),*root,*node;
            int i;
            priority_queue<pair<int,ListNode*>> top_process;
    
    
            for(i=0;i<lists.size();i++){
                if(lists[i] != nullptr)
                    top_process.push({-1*lists[i]->val,lists[i]});
            }
            
    
            root = start;
            while(!top_process.empty()){
                node = top_process.top().second;
                top_process.pop();
    
                if(node->next != nullptr){
                    top_process.push({-1*node->next->val,node->next});
                }
                
                
                root->next = node;
                root = root->next;
            }
    
            return start->next;
    
            
        }
    };