class TreeNode:
    def __init__(self, value = 0, left = None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        def dfs(root):
            if root is None:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1

        return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)




root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(3)
root.left = t1
root.right = t2
t1.left = t3
t1.right = t4
t3.left = TreeNode(4)
t3.right = TreeNode(4)

"""

root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t2.left = TreeNode(15)
t2.right = TreeNode(7)
root.left = t1
root.right = t2
"""
ib = Solution()
rel = ib.isBalanced(root)
print("rel = ", rel)
#class Solution:
#    def isBalanced(self, root):



"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 0


class Solution:

    def addHeight(self, root):
        if root:
            self.addHeight(root.left)
            self.addHeight(root.right)
            # print(f"node {root.value}")
            # set height for every node
            if root.left == None and root.right == None:
                root.height = 0
            elif root.left is not None and root.right is None:
                root.height = root.left.height + 1
            elif root.left is None and root.right is not None:
                root.height = root.right.height + 1
            else:
                if root.left.height >= root.right.height:
                    root.height = root.left.height + 1
                else:
                    root.height = root.right.height + 1

    def rec_isBalanced(self, root):
        print("come here")

        if root is None:
            #print("root is None")
            return True
        #print(f"node {root.value}, height = {root.height}")
        if root.left is not None and root.right is not None:
            #print(f"node {root.value}, height = {root.height}")
            if abs(root.left.height - root.right.height) > 1:
                return False
            #else:
            #    return True
        elif root.left is None and root.right is not None:
            #print(f"node {root.value}, height = {root.height}")
            if root.right.height >= 1:
                return False
            #else:
            #    return True
        elif root.left is not None and root.right is None:
            #print(f"node {root.value}, height = {root.height}")
            if root.left.height >= 1:
                return False
            #else:
             #   return True
        else: # root.left is None and root.right is Node
            #print(f"node {root.value}, height = {root.height}")
            return True
        return self.rec_isBalanced(root.left) and self.rec_isBalanced(root.right)
        #return self.rec_isBalance(root.left)

    def traveral(self, root):
        if root:
            self.traveral(root.left)
            print(f"node = {root.value}, height = {root.height}")
            self.traveral(root.right)

    def isBalanced(self, root):
        # add height attribute
        self.addHeight(root)
        #self.traveral(root)
        # check is balanced or not
        print("before call rec_isBalanced")
        return self.rec_isBalanced(root)


"""