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
        bool result = false;
        bool hasPathSum(TreeNode* root, int targetSum) {
    
            if(root == nullptr)
                return false;
            
            if(root->left==nullptr && root->right==nullptr)
                if(targetSum-root->val == 0)
                    result = true;
            
            hasPathSum(root->left,targetSum-root->val);
            hasPathSum(root->right,targetSum-root->val);
    
    
            return result;
            
        }
    };