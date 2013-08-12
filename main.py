#==============================
# Main
#==============================

import tree
import svg

T = tree.BinaryTree()
root = T.addNode(2)
T.insert(root,-2)
T.insert(root,3)
T.insert(root,4)
T.insert(root,4)
T.insert(root,6)
T.insert(root,3)

T.insert(root,7)
T.printTree(root)
max = T.height(root,0)
print("\n" + str(max))
T.printSVG(root)
