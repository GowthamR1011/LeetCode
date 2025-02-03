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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *n_node=head, *curr = head;

        int i = 1;

        while(i<=n){
            n_node = n_node->next;
            i++;
        }

        if(n_node == nullptr)
            return head->next;
        
        while(curr!=nullptr){
            if(n_node->next == nullptr){
                if(curr->next != nullptr){
                    curr->next = curr->next->next;
                    return head;
                }
                else
                    curr->next = nullptr;
            }

            curr = curr->next;
            n_node = n_node->next;
        }
        return head;
    }
};