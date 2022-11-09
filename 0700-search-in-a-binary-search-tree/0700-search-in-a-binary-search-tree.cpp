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

// Version 01. DFS - Recursion(BST)
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (root == NULL) return NULL;
        if (val == root->val) return root;
        if (val < root->val) return searchBST(root->left, val);
        else return searchBST(root->right, val);
    }
};

// Version 02. Iteration(BST)
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root == NULL) return NULL;
        while (root != NULL && root->val != val) {
            if (val < root->val) root = root->left;
            else root = root->right;
        }
        return root;
    }
};
