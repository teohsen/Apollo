from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        r_val = root.val

        r = self.tree2str(root.right)
        l = self.tree2str(root.left)

        if root.left is None and root.right is None:
            return f"{r_val}"
        elif root.left is None and root.right is not None:
            return f"{r_val}()({r})"
        elif root.left is not None and root.right is None:
            return f"{r_val}({l})"

        return f"{r_val}({l})({r})"

    def test_case(self):
        # input_val = [1,2,3,4]
        input_val = TreeNode(1, TreeNode(2, 4), TreeNode(3))
        result = self.tree2str(input_val)
        return result == "1(2(4))(3)"


print(Solution().test_case())