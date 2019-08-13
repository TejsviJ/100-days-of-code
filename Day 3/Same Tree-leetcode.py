class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True;
        if not q or not p:
            return False;
        if q.val!=p.val:
            return False;
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
