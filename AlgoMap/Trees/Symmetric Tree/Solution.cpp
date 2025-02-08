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
    bool checkEqual(TreeNode* p, TreeNode* q) {
                
                if(p == nullptr && q == nullptr)
                    return true;
        
                if(p==nullptr)
                    return false;
                
                if(q==nullptr)
                    return false;
                
                return(p->val == q->val && checkEqual(p->left,q->right) && checkEqual(p->right,q->left));
            }
        
        bool isSymmetric(TreeNode* root) {
            return checkEqual(root->left,root->right);
        }
    };