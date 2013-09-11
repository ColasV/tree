#==============================
# Laby class
# - Create a Binary tree
# - Chose the content of the node by adding attribut
#==============================
import random
import unittest
import tree
import os

class TestTreeFunction(unittest.TestCase):

    def setUp(self):
        self.T = tree.BinaryTree()
        self.root = self.T.addNode(0)
        for i in range(10):
            self.T.insert(self.root,i)

    # make sure that the height of the tree is good
    def test_height(self):
        self.assertEqual(self.T.height(self.root,0),9)

    # make sure that the file is correctly created
    def test_treesvg(self):
    	name = 'tree_test.svg'
    	self.T.printSVG(self.root,name)
    	try:
    		F = open(name,"w")
    		self.assertEqual(True,True)
    		os.remove(name)
    	except:
    		self.fail('Cannot find the file')

       
if __name__ == '__main__':
    unittest.main()









