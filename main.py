#==============================
# Main
#==============================

import tree
import svg

T = tree.BinaryTree()
root = T.addNode(0)
for i in range(10):
	T.insert(root,i)


#T.printTree(root)
max = T.height(root,0)
print("\n" + str(max))
#T.printSVG(root)
