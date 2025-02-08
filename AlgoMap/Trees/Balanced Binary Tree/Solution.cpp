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
        int result = true;
        int height(TreeNode* node){
            int left,right;
            if(node == nullptr)
                return 0;
            
            left = height(node->left);
            right = height(node->right);
    
            if(abs(left-right) > 1)
                result = false;
            
            return (max(left,right) +1);
        }
        bool isBalanced(TreeNode* root) {
        
            height(root);
            return result;
        }
    };