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
        TreeNode* recoverFromPreorder(string traversal) {
            vector<pair<int,int>> tree;
    
            int curr_count = 0, curr_number = 0;
            traversal += '-';
    
    
            for(auto &ch:traversal){
                if(ch == '-'){
                    if(curr_number>0){
                        tree.push_back({curr_number,curr_count});
                        curr_count = 1;
                        curr_number = 0;
                    }
                    else{
                        curr_count++;
                    }
                }
                else{
                    curr_number = curr_number*10 + (ch-'0');
                }
            }
    
    
            vector<pair<TreeNode*,int>> stack;
    
            TreeNode *root;
            for(auto p:tree){
                
                int val = p.first, d = p.second;
                TreeNode *node= new TreeNode(val), *parent;
    
                while(!stack.empty() && stack.back().second >= d)
                    stack.pop_back();
                
                if(!stack.empty()){
                    parent = stack.back().first;
                    
                    if(parent->left==nullptr)
                        parent->left = node;
                    else
                        parent->right = node;
                }
                else
                    root= node;
                
                stack.push_back({node,d});
            }
    
            return root;
        }
    };