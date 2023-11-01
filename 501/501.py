from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0
        self.max_count = 0

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, counter):
            if not node:
                return

            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)

        self.count = defaultdict(int)
        dfs(root, self.count)
        self.max_count = max(self.count.values())
        return [k for k, v in self.count.items() if v == self.max_count]


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    s = Solution()
    print(s.findMode(root))
