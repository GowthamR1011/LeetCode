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
class Solution {
    public:
        TreeNode* prev = nullptr;
        bool result = true;
    
        void checkBST(TreeNode* node){
            
            if(node == nullptr)
                return;
            
            if(result)
                checkBST(node->left);
            
            if(prev != nullptr)
                if(prev->val >= node->val)
                    result = false;
            prev = node;
            if(result)
                checkBST(node->right);
        }
    
        bool isValidBST(TreeNode* root) {
            
            checkBST(root);
            return result;
        }
    };