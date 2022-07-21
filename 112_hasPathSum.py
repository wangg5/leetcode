class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        q = [(root, targetSum-root.val)]
        #print("before loop q=", q)
        while q:
            n, v = q.pop(0)
            print(f"node= {n.val}, sum = {v}")
            if n.left is None and n.right is None:
                #print("leaf node = ", n.val)
                if v == 0:
                    return True
            elif n.left is None and n.right is not None:
                q.insert(0, (n.right, v-n.right.val))
            elif n.left is not None and n.right is None:
                q.insert(0, (n.left, v-n.left.val))
            elif n.left is not None and n.right is not None:
                #print("1 here")
                q.insert(0, (n.right, v - n.right.val))
                q.insert(0, (n.left, v - n.left.val))
        return False



"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
"""

root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
t3 = TreeNode(4)
t4 = TreeNode(5)
root.left = t1
root.right = t2
t1.left = t3
t1.right = t4
t3.left = TreeNode(6)
t3.right = TreeNode(7)



hp =Solution()
rel = hp.hasPathSum(root, 3)
print("rel = ", rel)