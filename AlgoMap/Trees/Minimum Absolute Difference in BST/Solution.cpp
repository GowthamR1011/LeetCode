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
        int min = -1;
        void difference(TreeNode* node){
            if(node == nullptr)
                return;
            
            difference(node->left);
    
            if(prev!=nullptr)
                if(abs(prev->val - node->val) < min || min == -1)
                    min = abs(prev->val-node->val);
            
            prev = node;
    
            difference(node->right);
        }
        int getMinimumDifference(TreeNode* root) {
            difference(root);
    
            return min;
    
        }
    };