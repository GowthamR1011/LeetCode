/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node *new_head = new Node(0),*prev;

        map<Node*,Node*> visited, random;

        prev=new_head;

        while(head != NULL){
            
            
            Node *new_node = new Node(head -> val);

            prev -> next = new_node;

            visited[head] = new_node;

            if(head -> random == nullptr)
                new_node -> random = nullptr;
            
            else if(visited.count(head -> random) > 1)
                new_node ->random = visited[head->random];
            
            else
                random[head] = new_node;
            
            prev = prev -> next;
            head = head -> next;
        }

        for(auto k:random){
            k.second->random = visited[k.first->random];
        }

        return new_head-> next;

    }
};