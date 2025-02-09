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
        int count;
        int result;
        void inorder(TreeNode* node){
            if(node == nullptr)
                return;
            
            inorder(node->left);
    
            if(count == 1)
                result = node -> val;
            count--;
    
            if(count >= 1)
                inorder(node->right);
        }
        int kthSmallest(TreeNode* root, int k) {
            count = k;
            inorder(root);
            return result;
        }
    };