#==============================
# Laby class
# - Create a Binary tree
# - Chose the content of the node by adding attribut
#==============================
import random
import unittest
import tree

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
      self.T = tree.BinaryTree()
      self.root = self.T.addNode(0)
      for i in range(10):
         self.T.insert(self.root,i)

    def test_height(self):
        # make sure that the height of the tree is good
        self.assertEqual(self.T.height(self.root,0),9)

       
if __name__ == '__main__':
    unittest.main()









