class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetic(self, root):
        # push value of every node to a list
        node_value = []
        self.value_list(root, node_value)
        while len(node_value) > 1:
            if node_value[0] != node_value[len(node_value)-1]:
                return False
            else:
                node_value = node_value[1:len(node_value)-1]
        return True

    def value_list(self, root, node_value):
        if root:
            self.value_list(root.left, node_value)
            node_value.append(root.val)
            self.value_list(root.right, node_value)

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

isy = Solution()
rel = isy.isSymmetic(root)
print("rel = ", rel)