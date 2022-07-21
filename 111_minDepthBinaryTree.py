class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        minD = []
        q = [(root, 1)]
        while q:
            n, d = q.pop(0)
            if n.left is None and n.right is None:
                minD.append(D)
            elif n.left is not None and n.right is None:
                q.insert(0, (n.left, d+1))
            elif n.left is None and n.right is not None:
                q.insert(0, (n.right, d+1))
            elif n.left is not None and n.right is not None:
                q.insert(0, (n.right, d+1))
                q.insert(0, (n.left, d+1))
        rel = minD[0]
        for i in range(len(minD)):
            if minD[i] <= rel:
                rel = minD[i]

        return rel