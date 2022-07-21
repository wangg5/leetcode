class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(4)
t6 = TreeNode(3)
root.left = t1
root.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
t3.right = TreeNode(5)
t6.left = TreeNode(5)

mp = Solution()
rel = mp.maxDepth(root)
print("rel = ", rel)