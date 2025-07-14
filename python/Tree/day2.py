class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_node_distance_k(root,k):
    if root ==None:
        return []
    res=[]
    queue=[]
    queue=[root]
    c=0
    while queue:
        pre_res=[]
        for _ in range(len(queue)):
            curr=queue.pop(0)
            pre_res.append(curr.val)

            if curr.left!=None:
                queue.append(curr.left)
            if curr.right!=None:
                queue.append(curr.right)
        if c==k:
            return pre_res
        c+=1
    return -1


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))
print(print_node_distance_k(root, 0))  # [1]
print(print_node_distance_k(root, 1))  # [2, 3]
print(print_node_distance_k(root, 2))  # [4, 5, 6]
print(print_node_distance_k(root, 3))  # -1   (tree isn’t that deep)