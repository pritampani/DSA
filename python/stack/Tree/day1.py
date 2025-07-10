# Level Order traversal


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def levelOrder(root):
#     if root ==None:
#         return []
#     res=[]
#     queue=[]
#     queue=[root]
    
#     while queue:
#         curr=queue.pop(0)
#         res.append(curr.val)

#         if curr.left!=None:
#             queue.append(curr.left)
#         if curr.right!=None:
#             queue.append(curr.right)
        
#     return res


# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3, None, TreeNode(6))

# print(levelOrder(root))
# root = TreeNode(None)
# print(levelOrder(root))



#level by level order travaesal 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_by_level_Order(root):
    if root ==None:
        return []
    res=[]
    queue=[]
    queue=[root]
    
    while queue:
        pre_res=[]
        for _ in range(len(queue)):
            curr=queue.pop(0)
            pre_res.append(curr.val)

            if curr.left!=None:
                queue.append(curr.left)
            if curr.right!=None:
                queue.append(curr.right)
        res.append(pre_res)
    return res


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

print(level_by_level_Order(root))
root = TreeNode(None)
print(level_by_level_Order(root))