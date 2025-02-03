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
    ListNode* reverseList(ListNode* head) {
        ListNode *x = head, *prev = head, *next_node;

        while(x != nullptr){
            next_node = x->next;

            if(x==head)
                x->next = nullptr;
            else
                x->next = prev;
            
            prev = x;
            x = next_node;
        }

        return prev;
    }
};