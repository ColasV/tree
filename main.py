#==============================
# Main
#==============================

import tree
import svg

#T = tree.BinaryTree()
#root = T.addNode(0)
#for i in range(10):
#	T.insert(root,i)
#
#
##T.printTree(root)
#max = T.height(root,0)
#print("\n" + str(max))
##T.printSVG(root)

B = tree.BinarySearchTree()
root = B.addNode(5)
B.insert(root,7)
B.insert(root,3)
B.insert(root,10)
B.insert(root,5)
B.insert(root,2)
B.printSVG(root,'test.svg')
B.delete(root,-1)
B.printSVG(root,'delete.svg')

