class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        opt = []
        return self.treeTraversal(root, opt)
    def treeTraversal(self, root, opt):
        if root:
            self.treeTraversal(root.left, opt)
            opt.append(root.val)
            self.treeTraversal(root.right, opt)
        return opt
t3 = TreeNode(3)
t2 = TreeNode(2, t3, None)
root = TreeNode(1, None, t2)
it = Solution()
rel = it.inorderTraversal(root)
print("rel = ", rel)