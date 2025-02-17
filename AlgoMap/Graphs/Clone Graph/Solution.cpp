/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
    public:
        Node* cloneGraph(Node* node) {
            map<Node*, Node*> visit;
            if(node == nullptr)
                return nullptr;
            vector<Node*> stack = {node};
            Node *curr, *n;
            while(!stack.empty()){
                
                curr = stack.back();
                stack.pop_back();
    
                n = new Node(curr->val);
                visit[curr] = n;
    
                for(auto nei:curr->neighbors){
                    if(visit.count(nei) == 0)
                        stack.push_back(nei);
                }
    
            }
    
            for(auto k:visit){
                for(auto nei:k.first->neighbors)
                    k.second->neighbors.push_back(visit[nei]);
            }
    
            return visit[node];
        }
    };