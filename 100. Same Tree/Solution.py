# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p==q
        if p.val != q.val:
            return False
        return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)
        

    # def bfs(self, root):
    #     if not root:
    #         return []
        
    #     result = []
    #     queue = [root]

    #     while queue:
    #         current = queue.pop(0)
    #         result.append(current.val)
    #         if current.left:
    #             queue.append(current.left)
                
    #         if current.right and not current.left:
    #             result.append(None)

    #         if current.right:
    #             queue.append(current.right)
    #     return result
        
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     p_list = self.bfs(p)
    #     q_list = self.bfs(q)
    #     return p_list == q_list