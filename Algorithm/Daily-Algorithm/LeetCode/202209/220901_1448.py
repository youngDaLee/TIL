"""
class Solution:
    def goodNodes(self, root: list) -> int:
        cnt = 0
        dp = []

        for i in range(len(root)):
            if i == 0:
                # root node exception
                cnt += 1
                dp[0] = root[i]

            parent_idx = (i-1)//2
            root_max = dp[parent_idx]

            if root[i] >= root_max:
                cnt += 1
                dp[i] = root[i]
            else:
                dp[i] = root_max

        return cnt

"""
class Solution:
    cnt = 0

    def findGoodNodes(self, max, node):
        if not node:
            return None

        if node.val >= max:
            self.cnt += 1
            max = node.val

        self.findGoodNodes(max, node.left)
        self.findGoodNodes(max, node.right)


    def goodNodes(self, root: TreeNode) -> int:
        self.findGoodNodes(-(10**4)-1, root)
        return self.cnt
