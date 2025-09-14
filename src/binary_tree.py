# %%
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#%%
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode('R')
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG

# %%
    # Test
    print("root.right.left.data:", root.right.left.data)
    print("root.right.left.data:", root.right.right.data)
    print("root.right.left.data:", root.right.right.left.data)
    print("root.right.left.data:", root.right.right.right.data)
# %%
