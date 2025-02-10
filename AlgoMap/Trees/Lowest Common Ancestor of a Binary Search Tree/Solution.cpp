/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 class Solution {
    public:
        TreeNode* result=nullptr;
        void checkNodeinTree(TreeNode* node,TreeNode* p,TreeNode* q){
    
            if(node == nullptr)
                return;
            
            if(node->val == p->val || node->val == q->val)
                result = node;
            
            else if(node->val > p-> val && node->val < q->val)
                result = node;
            
            else if(node->val < p->val && node-> val > q->val)
                result = node;
            
            else if(node->val < p->val)
                checkNodeinTree(node->right,p,q);
            else
                checkNodeinTree(node->left,p,q);
        }
    
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            
            result = root;
            checkNodeinTree(root,p,q);
            return result;
    
            
        }
    };