/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class FindElements {
    public:
        set<int> valueSet;
        void setvalue(TreeNode* node, int val){
    
            if(node == nullptr)
                return;
            
            node -> val = val;
            valueSet.insert(val);
    
            setvalue(node->left,2*val+1);
            setvalue(node->right,2*val+2);
        }
        FindElements(TreeNode* root) {
            
            setvalue(root,0);
        }
        
        bool find(int target) {
            return valueSet.count(target);
        }
    };
    
    /**
     * Your FindElements object will be instantiated and called as such:
     * FindElements* obj = new FindElements(root);
     * bool param_1 = obj->find(target);
     */