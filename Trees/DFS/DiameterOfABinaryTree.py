class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    diameter = 0

    def longestPath(node):
        if not node:
            return 0

        nonlocal diameter

        # Compute the depth of each subtree
        left_depth = longestPath(node.left)
        right_depth = longestPath(node.right)

        # The diameter at the current node will be the sum of the heights of the left and right subtrees
        diameter = max(diameter, left_depth + right_depth)

        # The height of the current node is the maximum height of its two children, plus 1 for the edge to the child
        return max(left_depth, right_depth) + 1

    longestPath(root)
    return diameter

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameterOfBinaryTree(root))

